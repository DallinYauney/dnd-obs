const outline = document.querySelector("#health .box-outline")
const fill = document.querySelector("#health .box-fill")
const bonus = document.querySelector("#health .bonus-fill")
const number = document.querySelector("#health .number")

async function getHealthData() {
    const response = await fetch("http://localhost:7979").then((response) => {
            // When the page is loaded convert it to text
            let nums = response.text()
            nums.then((nums) => {
                nums = nums.split(" ")

                let bonusHP = ""
                if(nums[2] > "0") {
                    bonusHP = `(+${nums[2]})`
                }

                number.innerText = `${nums[0]} / ${nums[1]} ${bonusHP}`
                fill.style.width = `calc(${100 * nums[0] / nums[1]}% - var(--border-calc))`
                bonus.style.width = `calc(${100 * nums[2] / nums[1]}% - var(--border-calc))`
            })
        })
        .catch(function(err) {  
            console.log('Failed to fetch data: ', err);  
        });
}
getHealthData()
setInterval(getHealthData, 1000)