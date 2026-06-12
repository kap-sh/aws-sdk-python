from typing import TYPE_CHECKING, Optional

from aws_sdk_backup_gateway._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.activation_key
    import aws_sdk_backup_gateway.types.associate_gateway_to_server_input
    import aws_sdk_backup_gateway.types.associate_gateway_to_server_output
    import aws_sdk_backup_gateway.types.create_gateway_input
    import aws_sdk_backup_gateway.types.create_gateway_output
    import aws_sdk_backup_gateway.types.day_of_month
    import aws_sdk_backup_gateway.types.day_of_week
    import aws_sdk_backup_gateway.types.delete_gateway_input
    import aws_sdk_backup_gateway.types.delete_gateway_output
    import aws_sdk_backup_gateway.types.disassociate_gateway_from_server_input
    import aws_sdk_backup_gateway.types.disassociate_gateway_from_server_output
    import aws_sdk_backup_gateway.types.gateway_arn
    import aws_sdk_backup_gateway.types.gateway_type
    import aws_sdk_backup_gateway.types.get_gateway_input
    import aws_sdk_backup_gateway.types.get_gateway_output
    import aws_sdk_backup_gateway.types.host
    import aws_sdk_backup_gateway.types.hour_of_day
    import aws_sdk_backup_gateway.types.list_gateways_input
    import aws_sdk_backup_gateway.types.list_gateways_output
    import aws_sdk_backup_gateway.types.max_results
    import aws_sdk_backup_gateway.types.minute_of_hour
    import aws_sdk_backup_gateway.types.name
    import aws_sdk_backup_gateway.types.next_token
    import aws_sdk_backup_gateway.types.password
    import aws_sdk_backup_gateway.types.put_maintenance_start_time_input
    import aws_sdk_backup_gateway.types.put_maintenance_start_time_output
    import aws_sdk_backup_gateway.types.server_arn
    import aws_sdk_backup_gateway.types.tags
    import aws_sdk_backup_gateway.types.test_hypervisor_configuration_input
    import aws_sdk_backup_gateway.types.test_hypervisor_configuration_output
    import aws_sdk_backup_gateway.types.update_gateway_information_input
    import aws_sdk_backup_gateway.types.update_gateway_information_output
    import aws_sdk_backup_gateway.types.update_gateway_software_now_input
    import aws_sdk_backup_gateway.types.update_gateway_software_now_output
    import aws_sdk_backup_gateway.types.username
    from aws_sdk_backup_gateway._services.async_backup_gateway import (
        AsyncBackupGatewayClient,
        AsyncBackupGatewayClientConfig,
    )
    from aws_sdk_backup_gateway._services.backup_gateway import (
        BackupGatewayClient,
        BackupGatewayClientConfig,
    )


class GatewayResource:
    def __init__(self, service: BackupGatewayClient) -> None:
        self._service = service

    def create(
        self,
        activation_key: "aws_sdk_backup_gateway.types.activation_key.ActivationKey",
        gateway_display_name: "aws_sdk_backup_gateway.types.name.Name",
        gateway_type: "aws_sdk_backup_gateway.types.gateway_type.GatewayType",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        tags: Optional["aws_sdk_backup_gateway.types.tags.Tags"] = None,
    ) -> "aws_sdk_backup_gateway.types.create_gateway_output.CreateGatewayOutput":
        """<p>Creates a backup gateway. After you create a gateway, you can associate it with a server using the <code>AssociateGatewayToServer</code> operation.</p>

        Args:
            activation_key: <p>The activation key of the created gateway.</p>
            gateway_display_name: <p>The display name of the created gateway.</p>
            gateway_type: <p>The type of created gateway.</p>
            tags: <p>A list of up to 50 tags to assign to the gateway. Each tag is a key-value pair.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.create_gateway_input.CreateGatewayInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.create_gateway_output.CreateGatewayOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.create_gateway

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.create_gateway.create_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.create_gateway_input.CreateGatewayInput = {}  # type: ignore[typeddict-item]
        input["activation_key"] = activation_key
        input["gateway_display_name"] = gateway_display_name
        input["gateway_type"] = gateway_type
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.get_gateway_output.GetGatewayOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.get_gateway_input.GetGatewayInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.get_gateway_output.GetGatewayOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_gateway

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_gateway.get_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.get_gateway_input.GetGatewayInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        gateway_display_name: Optional["aws_sdk_backup_gateway.types.name.Name"] = None,
    ) -> "aws_sdk_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput":
        """<p>Updates a gateway's name. Specify which gateway to update using the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to update.</p>
            gateway_display_name: <p>The updated display name of the gateway.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information.update_gateway_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn
        if gateway_display_name is not None:
            input["gateway_display_name"] = gateway_display_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput":
        """<p>Deletes a backup gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.delete_gateway_input.DeleteGatewayInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.delete_gateway_input.DeleteGatewayInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        max_results: Optional[
            "aws_sdk_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_backup_gateway.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_backup_gateway.types.list_gateways_output.ListGatewaysOutput":
        """<p>Lists backup gateways owned by an Amazon Web Services account in an Amazon Web Services Region. The returned list is ordered by gateway Amazon Resource Name (ARN).</p>

        Args:
            max_results: <p>The maximum number of gateways to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.list_gateways_input.ListGatewaysInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.list_gateways_output.ListGatewaysOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_gateways

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.list_gateways_input.ListGatewaysInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_gateway_to_server(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        server_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput":
        """<p>Associates a backup gateway with your server. After you complete the association process, you can back up and restore your VMs through the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            server_arn: <p>The Amazon Resource Name (ARN) of the server that hosts your virtual machines.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server.associate_gateway_to_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn
        input["server_arn"] = server_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_gateway_from_server(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput":
        """<p>Disassociates a backup gateway from the specified server. After the disassociation process finishes, the gateway can no longer access the virtual machines on the server.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to disassociate.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server.disassociate_gateway_from_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_maintenance_start_time(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        hour_of_day: "aws_sdk_backup_gateway.types.hour_of_day.HourOfDay",
        minute_of_hour: "aws_sdk_backup_gateway.types.minute_of_hour.MinuteOfHour",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        day_of_week: Optional[
            "aws_sdk_backup_gateway.types.day_of_week.DayOfWeek"
        ] = None,
        day_of_month: Optional[
            "aws_sdk_backup_gateway.types.day_of_month.DayOfMonth"
        ] = None,
    ) -> "aws_sdk_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput":
        """<p>Set the maintenance start time for a gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) for the gateway, used to specify its maintenance start time.</p>
            hour_of_day: <p>The hour of the day to start maintenance on a gateway.</p>
            minute_of_hour: <p>The minute of the hour to start maintenance on a gateway.</p>
            day_of_week: <p>The day of the week to start maintenance on a gateway.</p>
            day_of_month: <p>The day of the month start maintenance on a gateway.</p> <p>Valid values range from <code>Sunday</code> to <code>Saturday</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time.put_maintenance_start_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn
        input["hour_of_day"] = hour_of_day
        input["minute_of_hour"] = minute_of_hour
        if day_of_week is not None:
            input["day_of_week"] = day_of_week
        if day_of_month is not None:
            input["day_of_month"] = day_of_month

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def test_hypervisor_configuration(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        host: "aws_sdk_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        username: Optional["aws_sdk_backup_gateway.types.username.Username"] = None,
        password: Optional["aws_sdk_backup_gateway.types.password.Password"] = None,
    ) -> "aws_sdk_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput":
        """<p>Tests your hypervisor configuration to validate that backup gateway can connect with the hypervisor and its resources.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to the hypervisor to test.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration.test_hypervisor_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn
        input["host"] = host
        if username is not None:
            input["username"] = username
        if password is not None:
            input["password"] = password

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_gateway_software_now(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput":
        """<p>Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.</p> <note> <p>When you make this request, you get a <code>200 OK</code> success response immediately. However, it might take some time for the update to complete.</p> </note>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to be updated.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now.update_gateway_software_now(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGatewayResource:
    def __init__(self, service: AsyncBackupGatewayClient) -> None:
        self._service = service

    async def create(
        self,
        activation_key: "aws_sdk_backup_gateway.types.activation_key.ActivationKey",
        gateway_display_name: "aws_sdk_backup_gateway.types.name.Name",
        gateway_type: "aws_sdk_backup_gateway.types.gateway_type.GatewayType",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        tags: Optional["aws_sdk_backup_gateway.types.tags.Tags"] = None,
    ) -> "aws_sdk_backup_gateway.types.create_gateway_output.CreateGatewayOutput":
        """<p>Creates a backup gateway. After you create a gateway, you can associate it with a server using the <code>AssociateGatewayToServer</code> operation.</p>

        Args:
            activation_key: <p>The activation key of the created gateway.</p>
            gateway_display_name: <p>The display name of the created gateway.</p>
            gateway_type: <p>The type of created gateway.</p>
            tags: <p>A list of up to 50 tags to assign to the gateway. Each tag is a key-value pair.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.create_gateway_input.CreateGatewayInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.create_gateway_output.CreateGatewayOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.create_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.create_gateway.async_create_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.create_gateway_input.CreateGatewayInput = {}  # type: ignore[typeddict-item]
        input["activation_key"] = activation_key
        input["gateway_display_name"] = gateway_display_name
        input["gateway_type"] = gateway_type
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.get_gateway_output.GetGatewayOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.get_gateway_input.GetGatewayInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.get_gateway_output.GetGatewayOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_gateway.async_get_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.get_gateway_input.GetGatewayInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        gateway_display_name: Optional["aws_sdk_backup_gateway.types.name.Name"] = None,
    ) -> "aws_sdk_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput":
        """<p>Updates a gateway's name. Specify which gateway to update using the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to update.</p>
            gateway_display_name: <p>The updated display name of the gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information.async_update_gateway_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn
        if gateway_display_name is not None:
            input["gateway_display_name"] = gateway_display_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput":
        """<p>Deletes a backup gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.delete_gateway_input.DeleteGatewayInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway.async_delete_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.delete_gateway_input.DeleteGatewayInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        max_results: Optional[
            "aws_sdk_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_backup_gateway.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_backup_gateway.types.list_gateways_output.ListGatewaysOutput":
        """<p>Lists backup gateways owned by an Amazon Web Services account in an Amazon Web Services Region. The returned list is ordered by gateway Amazon Resource Name (ARN).</p>

        Args:
            max_results: <p>The maximum number of gateways to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.list_gateways_input.ListGatewaysInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.list_gateways_output.ListGatewaysOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_gateways

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_gateways.async_list_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.list_gateways_input.ListGatewaysInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_gateway_to_server(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        server_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput":
        """<p>Associates a backup gateway with your server. After you complete the association process, you can back up and restore your VMs through the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            server_arn: <p>The Amazon Resource Name (ARN) of the server that hosts your virtual machines.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server.async_associate_gateway_to_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn
        input["server_arn"] = server_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_gateway_from_server(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput":
        """<p>Disassociates a backup gateway from the specified server. After the disassociation process finishes, the gateway can no longer access the virtual machines on the server.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to disassociate.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server.async_disassociate_gateway_from_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_maintenance_start_time(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        hour_of_day: "aws_sdk_backup_gateway.types.hour_of_day.HourOfDay",
        minute_of_hour: "aws_sdk_backup_gateway.types.minute_of_hour.MinuteOfHour",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        day_of_week: Optional[
            "aws_sdk_backup_gateway.types.day_of_week.DayOfWeek"
        ] = None,
        day_of_month: Optional[
            "aws_sdk_backup_gateway.types.day_of_month.DayOfMonth"
        ] = None,
    ) -> "aws_sdk_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput":
        """<p>Set the maintenance start time for a gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) for the gateway, used to specify its maintenance start time.</p>
            hour_of_day: <p>The hour of the day to start maintenance on a gateway.</p>
            minute_of_hour: <p>The minute of the hour to start maintenance on a gateway.</p>
            day_of_week: <p>The day of the week to start maintenance on a gateway.</p>
            day_of_month: <p>The day of the month start maintenance on a gateway.</p> <p>Valid values range from <code>Sunday</code> to <code>Saturday</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time.async_put_maintenance_start_time(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn
        input["hour_of_day"] = hour_of_day
        input["minute_of_hour"] = minute_of_hour
        if day_of_week is not None:
            input["day_of_week"] = day_of_week
        if day_of_month is not None:
            input["day_of_month"] = day_of_month

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def test_hypervisor_configuration(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        host: "aws_sdk_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        username: Optional["aws_sdk_backup_gateway.types.username.Username"] = None,
        password: Optional["aws_sdk_backup_gateway.types.password.Password"] = None,
    ) -> "aws_sdk_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput":
        """<p>Tests your hypervisor configuration to validate that backup gateway can connect with the hypervisor and its resources.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to the hypervisor to test.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration.async_test_hypervisor_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn
        input["host"] = host
        if username is not None:
            input["username"] = username
        if password is not None:
            input["password"] = password

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_gateway_software_now(
        self,
        gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput":
        """<p>Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.</p> <note> <p>When you make this request, you get a <code>200 OK</code> success response immediately. However, it might take some time for the update to complete.</p> </note>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to be updated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now.async_update_gateway_software_now(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
