from typing import TYPE_CHECKING, Optional

import aws_sdk_scheduler._auth._signers
import aws_sdk_scheduler._auth._sigv4
from aws_sdk_scheduler._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.client_token
    import aws_sdk_scheduler.types.create_schedule_group_input
    import aws_sdk_scheduler.types.create_schedule_group_output
    import aws_sdk_scheduler.types.delete_schedule_group_input
    import aws_sdk_scheduler.types.delete_schedule_group_output
    import aws_sdk_scheduler.types.get_schedule_group_input
    import aws_sdk_scheduler.types.get_schedule_group_output
    import aws_sdk_scheduler.types.list_schedule_groups_input
    import aws_sdk_scheduler.types.list_schedule_groups_output
    import aws_sdk_scheduler.types.max_results
    import aws_sdk_scheduler.types.next_token
    import aws_sdk_scheduler.types.schedule_group_name
    import aws_sdk_scheduler.types.schedule_group_name_prefix
    import aws_sdk_scheduler.types.schedule_group_summary
    import aws_sdk_scheduler.types.tag_list
    from aws_sdk_scheduler._services.async_scheduler import (
        AsyncSchedulerClient,
        AsyncSchedulerClientConfig,
    )
    from aws_sdk_scheduler._services.scheduler import (
        SchedulerClient,
        SchedulerClientConfig,
    )


class ScheduleGroup:
    def __init__(self, service: SchedulerClient) -> None:
        self._service = service

    def put(
        self,
        name: "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        tags: Optional["aws_sdk_scheduler.types.tag_list.TagList"] = None,
        client_token: Optional[
            "aws_sdk_scheduler.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_scheduler.types.create_schedule_group_output.CreateScheduleGroupOutput"
    ):
        """<p>Creates the specified schedule group.</p>

        Args:
            name: <p>The name of the schedule group that you are creating.</p>
            tags: <p>The list of tags to associate with the schedule group.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_scheduler.types.create_schedule_group_input.CreateScheduleGroupInput]",
        ) -> OperationResponse[
            "aws_sdk_scheduler.types.create_schedule_group_output.CreateScheduleGroupOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.create_schedule_group

            output, http_response = (
                aws_sdk_scheduler._operations.aws_chronos_service.create_schedule_group.create_schedule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.create_schedule_group_input.CreateScheduleGroupInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
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
        name: "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
    ) -> "aws_sdk_scheduler.types.get_schedule_group_output.GetScheduleGroupOutput":
        """<p>Retrieves the specified schedule group.</p>

        Args:
            name: <p>The name of the schedule group to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_scheduler.types.get_schedule_group_input.GetScheduleGroupInput]",
        ) -> OperationResponse[
            "aws_sdk_scheduler.types.get_schedule_group_output.GetScheduleGroupOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.get_schedule_group

            output, http_response = (
                aws_sdk_scheduler._operations.aws_chronos_service.get_schedule_group.get_schedule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.get_schedule_group_input.GetScheduleGroupInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        name: "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_scheduler.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_scheduler.types.delete_schedule_group_output.DeleteScheduleGroupOutput"
    ):
        """<p>Deletes the specified schedule group. Deleting a schedule group results in EventBridge Scheduler deleting all schedules associated with the group. When you delete a group, it remains in a <code>DELETING</code> state until all of its associated schedules are deleted. Schedules associated with the group that are set to run while the schedule group is in the process of being deleted might continue to invoke their targets until the schedule group and its associated schedules are deleted.</p> <note> <p> This operation is eventually consistent. </p> </note>

        Args:
            name: <p>The name of the schedule group to delete.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_scheduler.types.delete_schedule_group_input.DeleteScheduleGroupInput]",
        ) -> OperationResponse[
            "aws_sdk_scheduler.types.delete_schedule_group_output.DeleteScheduleGroupOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.delete_schedule_group

            output, http_response = (
                aws_sdk_scheduler._operations.aws_chronos_service.delete_schedule_group.delete_schedule_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.delete_schedule_group_input.DeleteScheduleGroupInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SchedulerClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_scheduler.types.schedule_group_name_prefix.ScheduleGroupNamePrefix"
        ] = None,
        next_token: Optional["aws_sdk_scheduler.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_scheduler.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_scheduler.types.list_schedule_groups_output.ListScheduleGroupsOutput":
        """<p>Returns a paginated list of your schedule groups.</p>

        Args:
            name_prefix: <p>The name prefix that you can use to return a filtered list of your schedule groups.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            max_results: <p>If specified, limits the number of results returned by this operation. The operation also returns a <code>NextToken</code> which you can use in a subsequent operation to retrieve the next set of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_scheduler.types.list_schedule_groups_input.ListScheduleGroupsInput]",
        ) -> OperationResponse[
            "aws_sdk_scheduler.types.list_schedule_groups_output.ListScheduleGroupsOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.list_schedule_groups

            output, http_response = (
                aws_sdk_scheduler._operations.aws_chronos_service.list_schedule_groups.list_schedule_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.list_schedule_groups_input.ListScheduleGroupsInput = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncScheduleGroup:
    def __init__(self, service: AsyncSchedulerClient) -> None:
        self._service = service

    async def put(
        self,
        name: "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
        tags: Optional["aws_sdk_scheduler.types.tag_list.TagList"] = None,
        client_token: Optional[
            "aws_sdk_scheduler.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_scheduler.types.create_schedule_group_output.CreateScheduleGroupOutput"
    ):
        """<p>Creates the specified schedule group.</p>

        Args:
            name: <p>The name of the schedule group that you are creating.</p>
            tags: <p>The list of tags to associate with the schedule group.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_scheduler.types.create_schedule_group_input.CreateScheduleGroupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_scheduler.types.create_schedule_group_output.CreateScheduleGroupOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.create_schedule_group

            (
                output,
                http_response,
            ) = await aws_sdk_scheduler._operations.aws_chronos_service.create_schedule_group.async_create_schedule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.create_schedule_group_input.CreateScheduleGroupInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
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
        name: "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
    ) -> "aws_sdk_scheduler.types.get_schedule_group_output.GetScheduleGroupOutput":
        """<p>Retrieves the specified schedule group.</p>

        Args:
            name: <p>The name of the schedule group to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_scheduler.types.get_schedule_group_input.GetScheduleGroupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_scheduler.types.get_schedule_group_output.GetScheduleGroupOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.get_schedule_group

            (
                output,
                http_response,
            ) = await aws_sdk_scheduler._operations.aws_chronos_service.get_schedule_group.async_get_schedule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.get_schedule_group_input.GetScheduleGroupInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        name: "aws_sdk_scheduler.types.schedule_group_name.ScheduleGroupName",
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
        client_token: Optional[
            "aws_sdk_scheduler.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "aws_sdk_scheduler.types.delete_schedule_group_output.DeleteScheduleGroupOutput"
    ):
        """<p>Deletes the specified schedule group. Deleting a schedule group results in EventBridge Scheduler deleting all schedules associated with the group. When you delete a group, it remains in a <code>DELETING</code> state until all of its associated schedules are deleted. Schedules associated with the group that are set to run while the schedule group is in the process of being deleted might continue to invoke their targets until the schedule group and its associated schedules are deleted.</p> <note> <p> This operation is eventually consistent. </p> </note>

        Args:
            name: <p>The name of the schedule group to delete.</p>
            client_token: <p> Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, EventBridge Scheduler uses a randomly generated token for the request to ensure idempotency. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_scheduler.types.delete_schedule_group_input.DeleteScheduleGroupInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_scheduler.types.delete_schedule_group_output.DeleteScheduleGroupOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.delete_schedule_group

            (
                output,
                http_response,
            ) = await aws_sdk_scheduler._operations.aws_chronos_service.delete_schedule_group.async_delete_schedule_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.delete_schedule_group_input.DeleteScheduleGroupInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSchedulerClientConfig] = None,
        name_prefix: Optional[
            "aws_sdk_scheduler.types.schedule_group_name_prefix.ScheduleGroupNamePrefix"
        ] = None,
        next_token: Optional["aws_sdk_scheduler.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_scheduler.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_scheduler.types.list_schedule_groups_output.ListScheduleGroupsOutput":
        """<p>Returns a paginated list of your schedule groups.</p>

        Args:
            name_prefix: <p>The name prefix that you can use to return a filtered list of your schedule groups.</p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            max_results: <p>If specified, limits the number of results returned by this operation. The operation also returns a <code>NextToken</code> which you can use in a subsequent operation to retrieve the next set of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_scheduler.types.list_schedule_groups_input.ListScheduleGroupsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_scheduler.types.list_schedule_groups_output.ListScheduleGroupsOutput"
        ]:
            import aws_sdk_scheduler._operations.aws_chronos_service.list_schedule_groups

            (
                output,
                http_response,
            ) = await aws_sdk_scheduler._operations.aws_chronos_service.list_schedule_groups.async_list_schedule_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_scheduler.types.list_schedule_groups_input.ListScheduleGroupsInput = {}  # type: ignore[typeddict-item]
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
