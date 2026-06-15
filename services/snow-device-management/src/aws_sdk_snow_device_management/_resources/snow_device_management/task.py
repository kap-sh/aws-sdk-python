from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_snow_device_management._auth._signers
import aws_sdk_snow_device_management._auth._sigv4
from aws_sdk_snow_device_management._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.cancel_task_input
    import aws_sdk_snow_device_management.types.cancel_task_output
    import aws_sdk_snow_device_management.types.command
    import aws_sdk_snow_device_management.types.create_task_input
    import aws_sdk_snow_device_management.types.create_task_output
    import aws_sdk_snow_device_management.types.describe_task_input
    import aws_sdk_snow_device_management.types.describe_task_output
    import aws_sdk_snow_device_management.types.idempotency_token
    import aws_sdk_snow_device_management.types.list_tasks_input
    import aws_sdk_snow_device_management.types.list_tasks_output
    import aws_sdk_snow_device_management.types.max_results
    import aws_sdk_snow_device_management.types.next_token
    import aws_sdk_snow_device_management.types.tag_map
    import aws_sdk_snow_device_management.types.target_list
    import aws_sdk_snow_device_management.types.task_description_string
    import aws_sdk_snow_device_management.types.task_id
    import aws_sdk_snow_device_management.types.task_state
    import aws_sdk_snow_device_management.types.task_summary
    from aws_sdk_snow_device_management._services.async_snow_device_management import (
        AsyncSnowDeviceManagementClient,
        AsyncSnowDeviceManagementClientConfig,
    )
    from aws_sdk_snow_device_management._services.snow_device_management import (
        SnowDeviceManagementClient,
        SnowDeviceManagementClientConfig,
    )


class Task:
    def __init__(self, service: SnowDeviceManagementClient) -> None:
        self._service = service

    def create(
        self,
        targets: "aws_sdk_snow_device_management.types.target_list.TargetList",
        command: "aws_sdk_snow_device_management.types.command.Command",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        description: Optional[
            "aws_sdk_snow_device_management.types.task_description_string.TaskDescriptionString"
        ] = None,
        tags: Optional["aws_sdk_snow_device_management.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_snow_device_management.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "aws_sdk_snow_device_management.types.create_task_output.CreateTaskOutput":
        """<p>Instructs one or more devices to start a task, such as unlocking or rebooting.</p>

        Args:
            targets: <p>A list of managed device IDs.</p>
            command: <p>The task to be performed. Only one task is executed on a device at a time.</p>
            description: <p>A description of the task and its targets.</p>
            tags: <p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment. </p>
            client_token: <p>A token ensuring that the action is called only once with the specified details.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_snow_device_management.types.create_task_input.CreateTaskInput]",
        ) -> OperationResponse[
            "aws_sdk_snow_device_management.types.create_task_output.CreateTaskOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.create_task

            output, http_response = (
                aws_sdk_snow_device_management._operations.snow_device_management.create_task.create_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.create_task_input.CreateTaskInput = {}  # type: ignore[typeddict-item]
        input_["targets"] = targets
        input_["command"] = command
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        task_id: "aws_sdk_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "aws_sdk_snow_device_management.types.describe_task_output.DescribeTaskOutput":
        """<p>Checks the metadata for a given task on a device. </p>

        Args:
            task_id: <p>The ID of the task to be described.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_snow_device_management.types.describe_task_input.DescribeTaskInput]",
        ) -> OperationResponse[
            "aws_sdk_snow_device_management.types.describe_task_output.DescribeTaskOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.describe_task

            output, http_response = (
                aws_sdk_snow_device_management._operations.snow_device_management.describe_task.describe_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.describe_task_input.DescribeTaskInput = {}  # type: ignore[typeddict-item]
        input_["task_id"] = task_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        state: Optional[
            "aws_sdk_snow_device_management.types.task_state.TaskState"
        ] = None,
        max_results: Optional[
            "aws_sdk_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_snow_device_management.types.list_tasks_output.ListTasksOutput":
        """<p>Returns a list of tasks that can be filtered by state.</p>

        Args:
            state: <p>A structure used to filter the list of tasks.</p>
            max_results: <p>The maximum number of tasks per page.</p>
            next_token: <p>A pagination token to continue to the next page of tasks.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_snow_device_management.types.list_tasks_input.ListTasksInput]",
        ) -> OperationResponse[
            "aws_sdk_snow_device_management.types.list_tasks_output.ListTasksOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.list_tasks

            output, http_response = (
                aws_sdk_snow_device_management._operations.snow_device_management.list_tasks.list_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.list_tasks_input.ListTasksInput = {}  # type: ignore[typeddict-item]
        if state is not None:
            input_["state"] = state
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def cancel_task(
        self,
        task_id: "aws_sdk_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "aws_sdk_snow_device_management.types.cancel_task_output.CancelTaskOutput":
        """<p>Sends a cancel request for a specified task. You can cancel a task only if it's still in a <code>QUEUED</code> state. Tasks that are already running can't be cancelled.</p> <note> <p>A task might still run if it's processed from the queue before the <code>CancelTask</code> operation changes the task's state.</p> </note>

        Args:
            task_id: <p>The ID of the task that you are attempting to cancel. You can retrieve a task ID by using the <code>ListTasks</code> operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_snow_device_management.types.cancel_task_input.CancelTaskInput]",
        ) -> OperationResponse[
            "aws_sdk_snow_device_management.types.cancel_task_output.CancelTaskOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.cancel_task

            output, http_response = (
                aws_sdk_snow_device_management._operations.snow_device_management.cancel_task.cancel_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.cancel_task_input.CancelTaskInput = {}  # type: ignore[typeddict-item]
        input_["task_id"] = task_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTask:
    def __init__(self, service: AsyncSnowDeviceManagementClient) -> None:
        self._service = service

    async def create(
        self,
        targets: "aws_sdk_snow_device_management.types.target_list.TargetList",
        command: "aws_sdk_snow_device_management.types.command.Command",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
        description: Optional[
            "aws_sdk_snow_device_management.types.task_description_string.TaskDescriptionString"
        ] = None,
        tags: Optional["aws_sdk_snow_device_management.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "aws_sdk_snow_device_management.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "aws_sdk_snow_device_management.types.create_task_output.CreateTaskOutput":
        """<p>Instructs one or more devices to start a task, such as unlocking or rebooting.</p>

        Args:
            targets: <p>A list of managed device IDs.</p>
            command: <p>The task to be performed. Only one task is executed on a device at a time.</p>
            description: <p>A description of the task and its targets.</p>
            tags: <p>Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment. </p>
            client_token: <p>A token ensuring that the action is called only once with the specified details.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.create_task_input.CreateTaskInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_snow_device_management.types.create_task_output.CreateTaskOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.create_task

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.create_task.async_create_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.create_task_input.CreateTaskInput = {}  # type: ignore[typeddict-item]
        input_["targets"] = targets
        input_["command"] = command
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        task_id: "aws_sdk_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> "aws_sdk_snow_device_management.types.describe_task_output.DescribeTaskOutput":
        """<p>Checks the metadata for a given task on a device. </p>

        Args:
            task_id: <p>The ID of the task to be described.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.describe_task_input.DescribeTaskInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_snow_device_management.types.describe_task_output.DescribeTaskOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.describe_task

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.describe_task.async_describe_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.describe_task_input.DescribeTaskInput = {}  # type: ignore[typeddict-item]
        input_["task_id"] = task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
        state: Optional[
            "aws_sdk_snow_device_management.types.task_state.TaskState"
        ] = None,
        max_results: Optional[
            "aws_sdk_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_snow_device_management.types.list_tasks_output.ListTasksOutput":
        """<p>Returns a list of tasks that can be filtered by state.</p>

        Args:
            state: <p>A structure used to filter the list of tasks.</p>
            max_results: <p>The maximum number of tasks per page.</p>
            next_token: <p>A pagination token to continue to the next page of tasks.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.list_tasks_input.ListTasksInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_snow_device_management.types.list_tasks_output.ListTasksOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.list_tasks

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.list_tasks.async_list_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.list_tasks_input.ListTasksInput = {}  # type: ignore[typeddict-item]
        if state is not None:
            input_["state"] = state
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def cancel_task(
        self,
        task_id: "aws_sdk_snow_device_management.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> "aws_sdk_snow_device_management.types.cancel_task_output.CancelTaskOutput":
        """<p>Sends a cancel request for a specified task. You can cancel a task only if it's still in a <code>QUEUED</code> state. Tasks that are already running can't be cancelled.</p> <note> <p>A task might still run if it's processed from the queue before the <code>CancelTask</code> operation changes the task's state.</p> </note>

        Args:
            task_id: <p>The ID of the task that you are attempting to cancel. You can retrieve a task ID by using the <code>ListTasks</code> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_snow_device_management.types.cancel_task_input.CancelTaskInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_snow_device_management.types.cancel_task_output.CancelTaskOutput"
        ]:
            import aws_sdk_snow_device_management._operations.snow_device_management.cancel_task

            (
                output,
                http_response,
            ) = await aws_sdk_snow_device_management._operations.snow_device_management.cancel_task.async_cancel_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_snow_device_management.types.cancel_task_input.CancelTaskInput = {}  # type: ignore[typeddict-item]
        input_["task_id"] = task_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
