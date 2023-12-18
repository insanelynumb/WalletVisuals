document.addEventListener("DOMContentLoaded", function () {
    var ctx = document.getElementById("myChart");

    if (ctx) {
        ctx = ctx.getContext("2d");

        const getRandomType = () => {
            const types = [
                "bar",
                "horizontalBar",
                "pie",
                "line",
                "radar",
                "doughnut",
                "polarArea",
            ];
            return types[Math.floor(Math.random() * types.length)];
        };

        const displayChart = (data, labels) => {
            const type = getRandomType();
            var myChart = new Chart(ctx, {
                type: type,
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: `Amount  (${type} View)`,
                            data: data,
                            backgroundColor: [
                                "rgba(255, 99, 132, 0.2)",
                                "rgba(54, 162, 235, 0.2)",
                                "rgba(255, 99, 132,0.7)",
                                "rgba(75, 192, 192, 0.2)",
                            ],
                            borderColor: [
                                "rgba(255, 99, 132, 1)",
                                "rgba(54, 162, 235, 1)",
                                "rgba(255, 99, 132,0.7)",
                                "rgba(75, 192, 192, 1)",
                            ],
                            borderWidth: 1,
                        },
                    ],
                },
                options: {
                    title: {
                        display: true,
                        text: "Expense Distribution Per Category For The Current Month",
                        fontSize: 25,
                    },
                    legend: {
                        display: true,
                        position: "right",
                        labels: {
                            fontColor: "#000",
                        },
                    },
                },
            });
        };

        const getExpenseCategoryData = () => {
            fetch("http://127.0.0.1:8000/authentication/expense_category_summary/")
                .then((res) => res.json())
                .then((res1) => {
                    const results = res1.expense_category_data;
                    const [labels, data] = [Object.keys(results), Object.values(results)];
                    console.log("data", data);
                    displayChart(data, labels);
                });
        };

        getExpenseCategoryData();
    }
});
