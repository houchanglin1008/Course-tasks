function gettime(){
			$.ajax({
				url:"/time",
				timeout:10000,
				success:function(data){
					$("#t1").html(data)
				},
				Error:function(xhr,type,errorThrown){
				}
			});
		}
		
function getl1num(){
			$.ajax({
				url:"/l1",
				success:function(data){
					$(".num h2").eq(0).text(data.data[0].pigprice + "元/公斤");
					$(".num h2").eq(1).text(data.data[1].pig_in + "元/公斤");
					$(".num h2").eq(2).text(data.data[2].pig_local + "元/公斤");
					$(".num h2").eq(3).text(data.data[3].maize + "元/吨");
					$(".num h2").eq(4).text(data.data[4].bean + "元/吨");
				},
				error:function(xhr,type,errorThrown){
				}
			});
		}
		
function getb1(){
			$.ajax({
				url:"/b",
				success:function(data){
					ec_b1_option.xAxis.data=data.date;
					ec_b1_option.series[0].data=data.pigprice;
					ec_b1_option.series[1].data=data.pig_in;
					ec_b1_option.series[2].data=data.pig_local;
					ec_b1.setOption(ec_b1_option);
				},
				error:function(xhr,type,errorThrown){
				}
			});
		}
		
function getb2(){
			$.ajax({
				url:"/b",
				success:function(data){
					ec_b2_option.xAxis.data=data.date;
					ec_b2_option.series[0].data=data.maize;
					ec_b2_option.series[1].data=data.bean;
					ec_b2.setOption(ec_b2_option);
				},
				error:function(xhr,type,errorThrown){
				}
			});
		}
		
function getmap(){
			$.ajax({
				url:"/map",
				success:function(data){
					ec_map_option.series[0].data=data.data
					ec_map.setOption(ec_map_option);
				},
				error:function(xhr,type,errorThrown){
				}
			});
			$.ajax({
				url:"/b",
				success:function(data){
					ec_map_option.title.text=data.date[365]+"全国部分省市生猪价格";
					ec_map.setOption(ec_map_option);
				},
				error:function(xhr,type,errorThrown){
				}
			});
		}

function getback(){
			$.ajax({
				url:"/l1",
				success:function(data){
					var da = (data.data[0].pigprice/(data.data[3].maize/500)).toFixed(3);
					var num = (data.data[0].pigprice-data.df[0].pigprice).toFixed(3);
					if (num>0)
					{
						//这个是判断它是不是大于0
						$(".id").eq(1).text('+'+(data.data[0].pigprice-data.df[0].pigprice).toFixed(3)+'元/公斤');
						$(".id").eq(1).css("color","#ec2918");
					}
					else
					{//这个是判断它是不是小于0
						$(".id").eq(1).text((data.data[0].pigprice-data.df[0].pigprice).toFixed(3)+'元/公斤');
						$(".id").eq(1).css("color","#00e700"); 
						//添加颜色，可以是具体色值。如：#f60
					}
					if (da>6)
					{
						//这个是判断它是不是大于0
						$(".id").eq(0).text((data.data[0].pigprice/(data.data[3].maize/500)).toFixed(3));
						$(".id").eq(0).css("color","#ec2918");
					}
					else
					{//这个是判断它是不是小于0
						$(".id").eq(0).text((data.data[0].pigprice/(data.data[3].maize/500)).toFixed(3));
						$(".id").eq(0).css("color","#00e700"); 
						//添加颜色，可以是具体色值。如：#f60
					}
				},
				error:function(xhr,type,errorThrown){
				}
			});
		}


function getr3(){
			$.ajax({
				url:"/r3",
				success:function(data){
					ec_r3_option.xAxis.data=data.date;
					ec_r3_option.series[0].data=data.pigprice;
					ec_r3_option.series[1].data=data.pig_in;
					ec_r3_option.series[2].data=data.pig_local;
					ec_r3.setOption(ec_r3_option);
				},
				error:function(xhr,type,errorThrown){
				}
			});
		}
window.onload  = function() {
	var q=document.getElementsByClassName("shengshi");
	for(var i = 0; i < q.length;i++){
		q[i].index = i;
		q[i].onclick = function() {
			var id = $(".shengshi").eq(this.index).attr('id');
			var pro = $(".shengshi").eq(this.index).text();
			q[this.index].style.background = "deepskyblue";
			for(var j=0;j<q.length;j++){
				if(j != this.index){
					q[j].style.backgroundColor='limegreen';
				}
			}
			$.ajax({
				url:"/tasks/"+id,
				success:function(data){
					$(".iu").eq(0).text(pro+"猪粮比");
					$(".iu").eq(1).text(pro+"外三元");
					var da = (data.pigprice[29]/(data.maize[29]/500)).toFixed(3);
					var num = (data.pigprice[29]-data.pigprice[28]).toFixed(3)
					if (num>0)
					{
						//这个是判断它是不是大于0
						$(".id").eq(1).text('+'+(data.pigprice[29]-data.pigprice[28]).toFixed(3)+'元/公斤');
						$(".id").eq(1).css("color","#ec2918");
					}
					else
					{//这个是判断它是不是小于0
						$(".id").eq(1).text((data.pigprice[29]-data.pigprice[28]).toFixed(3)+'元/公斤');
						$(".id").eq(1).css("color","#00e700"); 
						//添加颜色，可以是具体色值。如：#f60
					}
					if (da>6)
					{
						//这个是判断它是不是大于0
						$(".id").eq(0).text((data.pigprice[29]/(data.maize[29]/500)).toFixed(3));
						$(".id").eq(0).css("color","#ec2918");
					}
					else
					{//这个是判断它是不是小于0
						$(".id").eq(0).text((data.pigprice[29]/(data.maize[29]/500)).toFixed(3));
						$(".id").eq(0).css("color","#00e700"); 
						//添加颜色，可以是具体色值。如：#f60
					}
					ec_r3_option.title.text='本月'+pro+"生猪价格变化趋势";
					ec_r3_option.xAxis.data=data.date;
					ec_r3_option.series[0].data=data.pigprice;
					ec_r3_option.series[1].data=data.pig_in;
					ec_r3_option.series[2].data=data.pig_local;
					ec_r3.setOption(ec_r3_option);
				},
				error:function(xhr,type,errorThrown){
				}
			});
			}
	}
}

setInterval(gettime,1000)
getl1num()
getb1()
getb2()
getmap()
getback()
getr3()