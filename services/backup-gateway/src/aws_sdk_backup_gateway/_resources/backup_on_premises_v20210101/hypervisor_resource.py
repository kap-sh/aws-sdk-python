from __future__ import annotations

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
    import aws_sdk_backup_gateway.types.delete_hypervisor_input
    import aws_sdk_backup_gateway.types.delete_hypervisor_output
    import aws_sdk_backup_gateway.types.get_hypervisor_input
    import aws_sdk_backup_gateway.types.get_hypervisor_output
    import aws_sdk_backup_gateway.types.host
    import aws_sdk_backup_gateway.types.import_hypervisor_configuration_input
    import aws_sdk_backup_gateway.types.import_hypervisor_configuration_output
    import aws_sdk_backup_gateway.types.kms_key_arn
    import aws_sdk_backup_gateway.types.list_hypervisors_input
    import aws_sdk_backup_gateway.types.list_hypervisors_output
    import aws_sdk_backup_gateway.types.log_group_arn
    import aws_sdk_backup_gateway.types.max_results
    import aws_sdk_backup_gateway.types.name
    import aws_sdk_backup_gateway.types.next_token
    import aws_sdk_backup_gateway.types.password
    import aws_sdk_backup_gateway.types.server_arn
    import aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_input
    import aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_output
    import aws_sdk_backup_gateway.types.tags
    import aws_sdk_backup_gateway.types.update_hypervisor_input
    import aws_sdk_backup_gateway.types.update_hypervisor_output
    import aws_sdk_backup_gateway.types.username
    from aws_sdk_backup_gateway._services.async_backup_gateway import (
        AsyncBackupGatewayClient,
        AsyncBackupGatewayClientConfig,
    )
    from aws_sdk_backup_gateway._services.backup_gateway import (
        BackupGatewayClient,
        BackupGatewayClientConfig,
    )


class HypervisorResource:
    def __init__(self, service: BackupGatewayClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_backup_gateway.types.name.Name",
        host: "aws_sdk_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        username: Optional["aws_sdk_backup_gateway.types.username.Username"] = None,
        password: Optional["aws_sdk_backup_gateway.types.password.Password"] = None,
        kms_key_arn: Optional[
            "aws_sdk_backup_gateway.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_backup_gateway.types.tags.Tags"] = None,
    ) -> "aws_sdk_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput":
        """<p>Connect to a hypervisor by importing its configuration.</p>

        Args:
            name: <p>The name of the hypervisor.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>
            kms_key_arn: <p>The Key Management Service for the hypervisor.</p>
            tags: <p>The tags of the hypervisor configuration to import.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration.import_hypervisor_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["host"] = host
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput":
        """<p>This action requests information about the specified hypervisor to which the gateway will connect. A hypervisor is hardware, software, or firmware that creates and manages virtual machines, and allocates resources to them.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.get_hypervisor_input.GetHypervisorInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor.get_hypervisor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.get_hypervisor_input.GetHypervisorInput = {}  # type: ignore[typeddict-item]
        input_["hypervisor_arn"] = hypervisor_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        host: Optional["aws_sdk_backup_gateway.types.host.Host"] = None,
        username: Optional["aws_sdk_backup_gateway.types.username.Username"] = None,
        password: Optional["aws_sdk_backup_gateway.types.password.Password"] = None,
        name: Optional["aws_sdk_backup_gateway.types.name.Name"] = None,
        log_group_arn: Optional[
            "aws_sdk_backup_gateway.types.log_group_arn.LogGroupArn"
        ] = None,
    ) -> "aws_sdk_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput":
        """<p>Updates a hypervisor metadata, including its host, username, and password. Specify which hypervisor to update using the Amazon Resource Name (ARN) of the hypervisor in your request.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to update.</p>
            host: <p>The updated host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The updated username for the hypervisor.</p>
            password: <p>The updated password for the hypervisor.</p>
            name: <p>The updated name for the hypervisor</p>
            log_group_arn: <p>The Amazon Resource Name (ARN) of the group of gateways within the requested log.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor.update_hypervisor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput = {}  # type: ignore[typeddict-item]
        input_["hypervisor_arn"] = hypervisor_arn
        if host is not None:
            input_["host"] = host
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if name is not None:
            input_["name"] = name
        if log_group_arn is not None:
            input_["log_group_arn"] = log_group_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput":
        """<p>Deletes a hypervisor.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor.delete_hypervisor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput = {}  # type: ignore[typeddict-item]
        input_["hypervisor_arn"] = hypervisor_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
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
    ) -> "aws_sdk_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput":
        """<p>Lists your hypervisors.</p>

        Args:
            max_results: <p>The maximum number of hypervisors to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors.list_hypervisors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput = {}  # type: ignore[typeddict-item]
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

    def start_virtual_machines_metadata_sync(
        self,
        hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput":
        """<p>This action sends a request to sync metadata across the specified virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync.start_virtual_machines_metadata_sync(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput = {}  # type: ignore[typeddict-item]
        input_["hypervisor_arn"] = hypervisor_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncHypervisorResource:
    def __init__(self, service: AsyncBackupGatewayClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_backup_gateway.types.name.Name",
        host: "aws_sdk_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        username: Optional["aws_sdk_backup_gateway.types.username.Username"] = None,
        password: Optional["aws_sdk_backup_gateway.types.password.Password"] = None,
        kms_key_arn: Optional[
            "aws_sdk_backup_gateway.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["aws_sdk_backup_gateway.types.tags.Tags"] = None,
    ) -> "aws_sdk_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput":
        """<p>Connect to a hypervisor by importing its configuration.</p>

        Args:
            name: <p>The name of the hypervisor.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>
            kms_key_arn: <p>The Key Management Service for the hypervisor.</p>
            tags: <p>The tags of the hypervisor configuration to import.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration.async_import_hypervisor_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["host"] = host
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput":
        """<p>This action requests information about the specified hypervisor to which the gateway will connect. A hypervisor is hardware, software, or firmware that creates and manages virtual machines, and allocates resources to them.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.get_hypervisor_input.GetHypervisorInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor.async_get_hypervisor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.get_hypervisor_input.GetHypervisorInput = {}  # type: ignore[typeddict-item]
        input_["hypervisor_arn"] = hypervisor_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        host: Optional["aws_sdk_backup_gateway.types.host.Host"] = None,
        username: Optional["aws_sdk_backup_gateway.types.username.Username"] = None,
        password: Optional["aws_sdk_backup_gateway.types.password.Password"] = None,
        name: Optional["aws_sdk_backup_gateway.types.name.Name"] = None,
        log_group_arn: Optional[
            "aws_sdk_backup_gateway.types.log_group_arn.LogGroupArn"
        ] = None,
    ) -> "aws_sdk_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput":
        """<p>Updates a hypervisor metadata, including its host, username, and password. Specify which hypervisor to update using the Amazon Resource Name (ARN) of the hypervisor in your request.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to update.</p>
            host: <p>The updated host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The updated username for the hypervisor.</p>
            password: <p>The updated password for the hypervisor.</p>
            name: <p>The updated name for the hypervisor</p>
            log_group_arn: <p>The Amazon Resource Name (ARN) of the group of gateways within the requested log.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor.async_update_hypervisor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput = {}  # type: ignore[typeddict-item]
        input_["hypervisor_arn"] = hypervisor_arn
        if host is not None:
            input_["host"] = host
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if name is not None:
            input_["name"] = name
        if log_group_arn is not None:
            input_["log_group_arn"] = log_group_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput":
        """<p>Deletes a hypervisor.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor.async_delete_hypervisor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput = {}  # type: ignore[typeddict-item]
        input_["hypervisor_arn"] = hypervisor_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
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
    ) -> "aws_sdk_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput":
        """<p>Lists your hypervisors.</p>

        Args:
            max_results: <p>The maximum number of hypervisors to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors.async_list_hypervisors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput = {}  # type: ignore[typeddict-item]
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

    async def start_virtual_machines_metadata_sync(
        self,
        hypervisor_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput":
        """<p>This action sends a request to sync metadata across the specified virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync.async_start_virtual_machines_metadata_sync(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput = {}  # type: ignore[typeddict-item]
        input_["hypervisor_arn"] = hypervisor_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
