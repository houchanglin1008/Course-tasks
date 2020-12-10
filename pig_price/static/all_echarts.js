var ec_map = echarts.init(document.getElementById('main'));
function randomValue() {
	return Math.round(Math.random()*1000);
}
var ec_map_option = {
	tooltip: {
		formatter:function(params,ticket, callback){
			return params.seriesName+'<br />'+params.name+'：'+params.value+" 元/公斤"
		}//数据格式化
	},
	title: {
	    text: '',
		left:'center'
	},
	visualMap: {
		min: 25,
		max: 35,
		left: 'left',
		top: 'bottom',
		text: ['高','低'],//取值范围的文字
		inRange: {
		color: ['#e0ffff', '#006edd'],//取值范围的颜色		
		},
		show:true,//图注
		precision:2
	},
	geo: {
		map: 'china',
		roam: false,//不开启缩放和平移
		zoom:1.23,//视角缩放比例
		label: {
			normal: {
				show: true,
				fontSize:'10',
				color: 'rgba(0,0,0,0.7)'
			}
		},
		itemStyle: {
			normal:{
				borderColor: 'rgba(0, 0, 0, 0.2)'
			},
			emphasis:{
				areaColor: '#F3B329',//鼠标选择区域颜色
				shadowOffsetX: 0,
				shadowOffsetY: 0,
				shadowBlur: 20,
				borderWidth: 0,
				shadowColor: 'rgba(0, 0, 0, 0.5)'
			}
		}
	},
	series : [
		{
			name: '生猪价格(外三元)',
			type: 'map',
			geoIndex: 0,
			data:[]
		}
	]
};
ec_map.setOption(ec_map_option);

var ec_r3=echarts.init(document.getElementById('r3'));
var ec_r3_option = {
    title: {
        text: '本月全国生猪价格变化趋势'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['外三元', '内三元', '土杂猪'],
		right: 0,
		top: 30,
		itemGap:5,
		symbolKeepAspect:true
		
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: [],
		axisLabel: {
		      fontSize: 10
		    }
    },
    yAxis: {
        type: 'value',
		name: "价格:元/公斤",
		min:function (value) {
			return value.min - 1;
		}
    },
    series: [
        {
            name: '外三元',
            type: 'line',
            data: []
        },
        {
            name: '内三元',
            type: 'line',
            data: []
        },
        {
            name: '土杂猪',
            type: 'line',
            data: []
        }
    ]
};

ec_r3.setOption(ec_r3_option)


var ec_b2=echarts.init(document.getElementById('b2'));
// 指定图表的配置项和数据
var ec_b2_option = {
    title: {
        text: '全国生猪价格变化趋势'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['玉米', '豆粕'],
		right: 0,
		top: 30,
		itemGap:5,
		symbolKeepAspect:true
		
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: [],
		axisLabel: {
		      fontSize: 10
		    }
    },
    yAxis: {
        type: 'value',
		name: "价格:元/吨",
		min:function (value) {
			return value.min - 100;
		}
    },
    series: [
        {
            name: '玉米',
            type: 'line',
            data: []
        },
        {
            name: '豆粕',
            type: 'line',
            data: []
        }
    ]
};
ec_b2.setOption(ec_b2_option);// 基于准备好的dom，初始化 echarts 实例并绘制图表。

var ec_b1=echarts.init(document.getElementById('b1'));
// 指定图表的配置项和数据
var ec_b1_option = {
    title: {
        text: '全国生猪价格变化趋势'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['外三元', '内三元', '土杂猪'],
		right: 0,
		top: 30,
		itemGap:5,
		symbolKeepAspect:true
		
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: [],
		axisLabel: {
		      fontSize: 10
		    }
    },
    yAxis: {
        type: 'value',
		name: "价格:元/公斤",
		min:function (value) {
			return value.min - 1;
		}
    },
    series: [
        {
            name: '外三元',
            type: 'line',
            data: []
        },
        {
            name: '内三元',
            type: 'line',
            data: []
        },
        {
            name: '土杂猪',
            type: 'line',
            data: []
        }
    ]
};
ec_b1.setOption(ec_b1_option);// 基于准备好的dom，初始化 echarts 实例并绘制图表。


