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
    import aws_sdk_backup_gateway.types.get_virtual_machine_input
    import aws_sdk_backup_gateway.types.get_virtual_machine_output
    import aws_sdk_backup_gateway.types.list_virtual_machines_input
    import aws_sdk_backup_gateway.types.list_virtual_machines_output
    import aws_sdk_backup_gateway.types.max_results
    import aws_sdk_backup_gateway.types.next_token
    import aws_sdk_backup_gateway.types.resource_arn
    import aws_sdk_backup_gateway.types.server_arn
    from aws_sdk_backup_gateway._services.async_backup_gateway import (
        AsyncBackupGatewayClient,
        AsyncBackupGatewayClientConfig,
    )
    from aws_sdk_backup_gateway._services.backup_gateway import (
        BackupGatewayClient,
        BackupGatewayClientConfig,
    )


class VirtualMachineResource:
    def __init__(self, service: BackupGatewayClient) -> None:
        self._service = service

    def read(
        self,
        resource_arn: "aws_sdk_backup_gateway.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the virtual machine.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the virtual machine.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine.get_virtual_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

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
        hypervisor_arn: Optional[
            "aws_sdk_backup_gateway.types.server_arn.ServerArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_backup_gateway.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput":
        """<p>Lists your virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor connected to your virtual machine.</p>
            max_results: <p>The maximum number of virtual machines to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput]",
        ) -> OperationResponse[
            "aws_sdk_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines

            output, http_response = (
                aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines.list_virtual_machines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput = {}  # type: ignore[typeddict-item]
        if hypervisor_arn is not None:
            input_["hypervisor_arn"] = hypervisor_arn
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


class AsyncVirtualMachineResource:
    def __init__(self, service: AsyncBackupGatewayClient) -> None:
        self._service = service

    async def read(
        self,
        resource_arn: "aws_sdk_backup_gateway.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "aws_sdk_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the virtual machine.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the virtual machine.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine.async_get_virtual_machine(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

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
        hypervisor_arn: Optional[
            "aws_sdk_backup_gateway.types.server_arn.ServerArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_backup_gateway.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput":
        """<p>Lists your virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor connected to your virtual machine.</p>
            max_results: <p>The maximum number of virtual machines to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput"
        ]:
            import aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines

            (
                output,
                http_response,
            ) = await aws_sdk_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines.async_list_virtual_machines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput = {}  # type: ignore[typeddict-item]
        if hypervisor_arn is not None:
            input_["hypervisor_arn"] = hypervisor_arn
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
