from typing import TYPE_CHECKING, Optional

from aws_sdk_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_proton.types.empty_next_token
    import aws_sdk_proton.types.list_service_instance_provisioned_resources_input
    import aws_sdk_proton.types.list_service_instance_provisioned_resources_output
    import aws_sdk_proton.types.provisioned_resource
    import aws_sdk_proton.types.resource_name
    from aws_sdk_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig


class ServiceInstanceProvisionedResourceResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def list(
        self,
        service_name: "aws_sdk_proton.types.resource_name.ResourceName",
        service_instance_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[
            "aws_sdk_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "aws_sdk_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput":
        """<p>List provisioned resources for a service instance with details.</p>

        Args:
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated to.</p>
            service_instance_name: <p>The name of the service instance whose provisioned resources you want.</p>
            next_token: <p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources.list_service_instance_provisioned_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["service_name"] = service_name
        input_["service_instance_name"] = service_instance_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncServiceInstanceProvisionedResourceResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def list(
        self,
        service_name: "aws_sdk_proton.types.resource_name.ResourceName",
        service_instance_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "aws_sdk_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "aws_sdk_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput":
        """<p>List provisioned resources for a service instance with details.</p>

        Args:
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated to.</p>
            service_instance_name: <p>The name of the service instance whose provisioned resources you want.</p>
            next_token: <p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources.async_list_service_instance_provisioned_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["service_name"] = service_name
        input_["service_instance_name"] = service_instance_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
