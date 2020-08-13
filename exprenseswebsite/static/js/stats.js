const renderChart = (data, labels) => {
    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
        // type: "doughnut",
        type: 'bar',

        data: {
            labels: labels,
            datasets: [
                {
                    label: "Last 6 months expenses",
                    data: data,
                    backgroundColor: [
                        "rgba(255, 99, 132)",
                        "rgba(54, 162, 235)",
                        "rgba(255, 206, 86)",
                        "rgba(75, 192, 192)",
                        "rgba(153, 102, 255)",
                        "rgba(255, 159, 64)",
                    ],
                    borderColor: [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                        "rgba(255, 206, 86, 1)",
                        "rgba(75, 192, 192, 1)",
                        "rgba(153, 102, 255, 1)",
                        "rgba(255, 159, 64, 1)",
                    ],
                    borderWidth: 1,
                },
            ],
        },
        options: {
            title: {
                display: true,
                text: "Expenses per category",
            },
        },
    });
};

const getChartData = () => {
    console.log("fetching");
    fetch("/expense_category_summary")
        .then((res) => res.json())
        .then((results) => {
            console.log("results", results);
            const category_data = results.expense_category_data;
            const [labels, data] = [
                Object.keys(category_data),
                Object.values(category_data),
            ];

            renderChart(data, labels);
        });
};

document.onload = getChartData();
