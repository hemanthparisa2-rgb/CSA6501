async function generate() {

    const module =
        document.getElementById(
            "module"
        ).value;


    const strategy =
        document.getElementById(
            "strategy"
        ).value;


    const task =
        document.getElementById(
            "task"
        ).value;


    const examples =
        document.getElementById(
            "examples"
        ).value;


    if (!task.trim()) {

        alert(
            "Please enter an engineering task."
        );

        return;
    }


    document.getElementById(
        "response"
    ).innerText =
        "Ollama is generating...";


    try {

        const result =
            await fetch(
                "/api/generate",
                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body:
                        JSON.stringify({

                            module:
                                module,

                            strategy:
                                strategy,

                            task:
                                task,

                            examples:
                                examples

                        })

                }
            );


        const data =
            await result.json();


        if (!data.success) {

            document.getElementById(
                "response"
            ).innerText =
                "Error: " +
                data.error;

            return;
        }


        document.getElementById(
            "prompt"
        ).innerText =
            data.prompt;


        document.getElementById(
            "response"
        ).innerText =
            data.response;


        document.getElementById(
            "model"
        ).innerText =
            data.model;


        document.getElementById(
            "strategyResult"
        ).innerText =
            data.strategy;


        document.getElementById(
            "latency"
        ).innerText =
            data.latency +
            " sec";


        document.getElementById(
            "tokens"
        ).innerText =
            data.tokens;

    }

    catch (error) {

        document.getElementById(
            "response"
        ).innerText =
            "Backend connection error: " +
            error.message;

    }

}