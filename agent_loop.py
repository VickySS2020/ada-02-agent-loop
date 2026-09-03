#--------------------------------------
# AGENT LOOP
#--------------------------------------

while not finished:
    # The agent receives a task
    task = get_task()

    # The agent decides what action to take next
    action = decide_action(task)

    # The agent calls a tool depending on the action
    match action.type:
    case "READ":
        result = view_file(action.file)
    case "WRITE":
        result = create_file(action.file, action.content)
    case "EDIT":
        result = edit_file(action.file, action.changes)
    case "BASH":
        result = run_command(action.command)

    # Update context based on the results of the action taken
    update_context(result)

    # Check if the task is finished
    finished = check_if_finished(result)


