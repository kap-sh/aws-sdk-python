from typing import TYPE_CHECKING, Optional

import aws_sdk_deadline._auth._signers
import aws_sdk_deadline._auth._sigv4
from aws_sdk_deadline._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.create_monitor_request
    import aws_sdk_deadline.types.create_monitor_response
    import aws_sdk_deadline.types.delete_monitor_request
    import aws_sdk_deadline.types.delete_monitor_response
    import aws_sdk_deadline.types.get_monitor_request
    import aws_sdk_deadline.types.get_monitor_response
    import aws_sdk_deadline.types.get_monitor_settings_request
    import aws_sdk_deadline.types.get_monitor_settings_response
    import aws_sdk_deadline.types.iam_role_arn
    import aws_sdk_deadline.types.identity_center_instance_arn
    import aws_sdk_deadline.types.list_monitors_request
    import aws_sdk_deadline.types.list_monitors_response
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.monitor_id
    import aws_sdk_deadline.types.monitor_summary
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.region
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.settings_map
    import aws_sdk_deadline.types.subdomain
    import aws_sdk_deadline.types.tags
    import aws_sdk_deadline.types.update_monitor_request
    import aws_sdk_deadline.types.update_monitor_response
    import aws_sdk_deadline.types.update_monitor_settings_request
    import aws_sdk_deadline.types.update_monitor_settings_response
    from aws_sdk_deadline._services.async_deadline import (
        AsyncdeadlineClient,
        AsyncdeadlineClientConfig,
    )
    from aws_sdk_deadline._services.deadline import deadlineClient, deadlineClientConfig


class MonitorResource:
    def __init__(self, service: deadlineClient) -> None:
        self._service = service

    def create(
        self,
        display_name: "aws_sdk_deadline.types.resource_name.ResourceName",
        identity_center_instance_arn: "aws_sdk_deadline.types.identity_center_instance_arn.IdentityCenterInstanceArn",
        subdomain: "aws_sdk_deadline.types.subdomain.Subdomain",
        role_arn: "aws_sdk_deadline.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        identity_center_region: Optional["aws_sdk_deadline.types.region.Region"] = None,
        tags: Optional["aws_sdk_deadline.types.tags.Tags"] = None,
    ) -> "aws_sdk_deadline.types.create_monitor_response.CreateMonitorResponse":
        """<p>Creates an Amazon Web Services Deadline Cloud monitor that you can use to view your farms, queues, and fleets. After you submit a job, you can track the progress of the tasks and steps that make up the job, and then download the job's results. </p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The name that you give the monitor that is displayed in the Deadline Cloud console.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            identity_center_instance_arn: <p>The Amazon Resource Name of the IAM Identity Center instance that authenticates monitor users.</p>
            identity_center_region: <p>The Region where IAM Identity Center is enabled. Required when IAM Identity Center is in a different Region than the monitor.</p>
            subdomain: <p>The subdomain to use when creating the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.</p>
            role_arn: <p>The Amazon Resource Name of the IAM role that the monitor uses to connect to Deadline Cloud. Every user that signs in to the monitor using IAM Identity Center uses this role to access Deadline Cloud resources.</p>
            tags: <p>The tags to add to your monitor. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.create_monitor_request.CreateMonitorRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.create_monitor_response.CreateMonitorResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_monitor

            output, http_response = (
                aws_sdk_deadline._operations.deadline.create_monitor.create_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_monitor_request.CreateMonitorRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["display_name"] = display_name
        input_["identity_center_instance_arn"] = identity_center_instance_arn
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region
        input_["subdomain"] = subdomain
        input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_monitor_response.GetMonitorResponse":
        """<p>Gets information about the specified monitor.</p>

        Args:
            monitor_id: <p>The unique identifier for the monitor. This ID is returned by the <code>CreateMonitor</code> operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.get_monitor_request.GetMonitorRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.get_monitor_response.GetMonitorResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_monitor

            output, http_response = (
                aws_sdk_deadline._operations.deadline.get_monitor.get_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_monitor_request.GetMonitorRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        subdomain: Optional["aws_sdk_deadline.types.subdomain.Subdomain"] = None,
        display_name: Optional[
            "aws_sdk_deadline.types.resource_name.ResourceName"
        ] = None,
        role_arn: Optional["aws_sdk_deadline.types.iam_role_arn.IamRoleArn"] = None,
    ) -> "aws_sdk_deadline.types.update_monitor_response.UpdateMonitorResponse":
        """<p>Modifies the settings for a Deadline Cloud monitor. You can modify one or all of the settings when you call <code>UpdateMonitor</code>.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor to update.</p>
            subdomain: <p>The new value of the subdomain to use when forming the monitor URL.</p>
            display_name: <p>The new value to use for the monitor's display name.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            role_arn: <p>The Amazon Resource Name of the new IAM role to use with the monitor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.update_monitor_request.UpdateMonitorRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.update_monitor_response.UpdateMonitorResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_monitor

            output, http_response = (
                aws_sdk_deadline._operations.deadline.update_monitor.update_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_monitor_request.UpdateMonitorRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id
        if subdomain is not None:
            input_["subdomain"] = subdomain
        if display_name is not None:
            input_["display_name"] = display_name
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_monitor_response.DeleteMonitorResponse":
        """<p>Removes a Deadline Cloud monitor. After you delete a monitor, you can create a new one and attach farms to the monitor.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor to delete. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>GetMonitor</code> operation.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.delete_monitor_request.DeleteMonitorRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.delete_monitor_response.DeleteMonitorResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_monitor

            output, http_response = (
                aws_sdk_deadline._operations.deadline.delete_monitor.delete_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_monitor_request.DeleteMonitorRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_monitors_response.ListMonitorsResponse":
        """<p>Gets a list of your monitors in Deadline Cloud.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.list_monitors_request.ListMonitorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.list_monitors_response.ListMonitorsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_monitors

            output, http_response = (
                aws_sdk_deadline._operations.deadline.list_monitors.list_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_monitors_request.ListMonitorsRequest = {}  # type: ignore[typeddict-item]
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

    def get_monitor_settings(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse":
        """<p>Gets the settings for a Deadline Cloud monitor.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>ListMonitors</code> operation.</p>

        Examples:
            Get monitor settings

            >>> client.get_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_monitor_settings

            output, http_response = (
                aws_sdk_deadline._operations.deadline.get_monitor_settings.get_monitor_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_monitor_settings(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        settings: "aws_sdk_deadline.types.settings_map.SettingsMap",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse":
        """<p>Updates the settings for a Deadline Cloud monitor. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor to update settings for.</p>
            settings: <p>The monitor settings to update as key-value pairs. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.</p>

        Examples:
            Update monitor settings

            >>> client.update_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef', settings={'idcApplicationArn': 'arn:aws:sso::123456789012:application/ins-1234567890abcdef/apl-1234567890abcdef'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_monitor_settings

            output, http_response = (
                aws_sdk_deadline._operations.deadline.update_monitor_settings.update_monitor_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id
        input_["settings"] = settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncMonitorResource:
    def __init__(self, service: AsyncdeadlineClient) -> None:
        self._service = service

    async def create(
        self,
        display_name: "aws_sdk_deadline.types.resource_name.ResourceName",
        identity_center_instance_arn: "aws_sdk_deadline.types.identity_center_instance_arn.IdentityCenterInstanceArn",
        subdomain: "aws_sdk_deadline.types.subdomain.Subdomain",
        role_arn: "aws_sdk_deadline.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        client_token: Optional[
            "aws_sdk_deadline.types.client_token.ClientToken"
        ] = None,
        identity_center_region: Optional["aws_sdk_deadline.types.region.Region"] = None,
        tags: Optional["aws_sdk_deadline.types.tags.Tags"] = None,
    ) -> "aws_sdk_deadline.types.create_monitor_response.CreateMonitorResponse":
        """<p>Creates an Amazon Web Services Deadline Cloud monitor that you can use to view your farms, queues, and fleets. After you submit a job, you can track the progress of the tasks and steps that make up the job, and then download the job's results. </p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The name that you give the monitor that is displayed in the Deadline Cloud console.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            identity_center_instance_arn: <p>The Amazon Resource Name of the IAM Identity Center instance that authenticates monitor users.</p>
            identity_center_region: <p>The Region where IAM Identity Center is enabled. Required when IAM Identity Center is in a different Region than the monitor.</p>
            subdomain: <p>The subdomain to use when creating the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.</p>
            role_arn: <p>The Amazon Resource Name of the IAM role that the monitor uses to connect to Deadline Cloud. Every user that signs in to the monitor using IAM Identity Center uses this role to access Deadline Cloud resources.</p>
            tags: <p>The tags to add to your monitor. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.create_monitor_request.CreateMonitorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.create_monitor_response.CreateMonitorResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.create_monitor

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.create_monitor.async_create_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.create_monitor_request.CreateMonitorRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["display_name"] = display_name
        input_["identity_center_instance_arn"] = identity_center_instance_arn
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region
        input_["subdomain"] = subdomain
        input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_monitor_response.GetMonitorResponse":
        """<p>Gets information about the specified monitor.</p>

        Args:
            monitor_id: <p>The unique identifier for the monitor. This ID is returned by the <code>CreateMonitor</code> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.get_monitor_request.GetMonitorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.get_monitor_response.GetMonitorResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_monitor

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.get_monitor.async_get_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_monitor_request.GetMonitorRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        subdomain: Optional["aws_sdk_deadline.types.subdomain.Subdomain"] = None,
        display_name: Optional[
            "aws_sdk_deadline.types.resource_name.ResourceName"
        ] = None,
        role_arn: Optional["aws_sdk_deadline.types.iam_role_arn.IamRoleArn"] = None,
    ) -> "aws_sdk_deadline.types.update_monitor_response.UpdateMonitorResponse":
        """<p>Modifies the settings for a Deadline Cloud monitor. You can modify one or all of the settings when you call <code>UpdateMonitor</code>.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor to update.</p>
            subdomain: <p>The new value of the subdomain to use when forming the monitor URL.</p>
            display_name: <p>The new value to use for the monitor's display name.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            role_arn: <p>The Amazon Resource Name of the new IAM role to use with the monitor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.update_monitor_request.UpdateMonitorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.update_monitor_response.UpdateMonitorResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_monitor

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.update_monitor.async_update_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_monitor_request.UpdateMonitorRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id
        if subdomain is not None:
            input_["subdomain"] = subdomain
        if display_name is not None:
            input_["display_name"] = display_name
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.delete_monitor_response.DeleteMonitorResponse":
        """<p>Removes a Deadline Cloud monitor. After you delete a monitor, you can create a new one and attach farms to the monitor.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor to delete. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>GetMonitor</code> operation.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.delete_monitor_request.DeleteMonitorRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.delete_monitor_response.DeleteMonitorResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.delete_monitor

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.delete_monitor.async_delete_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.delete_monitor_request.DeleteMonitorRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
        next_token: Optional["aws_sdk_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["aws_sdk_deadline.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_deadline.types.list_monitors_response.ListMonitorsResponse":
        """<p>Gets a list of your monitors in Deadline Cloud.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.list_monitors_request.ListMonitorsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.list_monitors_response.ListMonitorsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.list_monitors

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.list_monitors.async_list_monitors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.list_monitors_request.ListMonitorsRequest = {}  # type: ignore[typeddict-item]
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

    async def get_monitor_settings(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse":
        """<p>Gets the settings for a Deadline Cloud monitor.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>ListMonitors</code> operation.</p>

        Examples:
            Get monitor settings

            >>> await client.get_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.get_monitor_settings

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.get_monitor_settings.async_get_monitor_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_monitor_settings(
        self,
        monitor_id: "aws_sdk_deadline.types.monitor_id.MonitorId",
        settings: "aws_sdk_deadline.types.settings_map.SettingsMap",
        *,
        config_overrides: Optional[AsyncdeadlineClientConfig] = None,
    ) -> "aws_sdk_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse":
        """<p>Updates the settings for a Deadline Cloud monitor. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor to update settings for.</p>
            settings: <p>The monitor settings to update as key-value pairs. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.</p>

        Examples:
            Update monitor settings

            >>> await client.update_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef', settings={'idcApplicationArn': 'arn:aws:sso::123456789012:application/ins-1234567890abcdef/apl-1234567890abcdef'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse"
        ]:
            import aws_sdk_deadline._operations.deadline.update_monitor_settings

            (
                output,
                http_response,
            ) = await aws_sdk_deadline._operations.deadline.update_monitor_settings.async_update_monitor_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["monitor_id"] = monitor_id
        input_["settings"] = settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
