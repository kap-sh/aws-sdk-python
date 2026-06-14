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
    import aws_sdk_proton.types.list_environment_provisioned_resources_input
    import aws_sdk_proton.types.list_environment_provisioned_resources_output
    import aws_sdk_proton.types.provisioned_resource
    import aws_sdk_proton.types.resource_name
    from aws_sdk_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig


class EnvironmentProvisionedResourceResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def list(
        self,
        environment_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[
            "aws_sdk_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "aws_sdk_proton.types.list_environment_provisioned_resources_output.ListEnvironmentProvisionedResourcesOutput":
        """<p>List the provisioned resources for your environment.</p>

        Args:
            environment_name: <p>The environment name.</p>
            next_token: <p>A token that indicates the location of the next environment provisioned resource in the array of environment provisioned resources, after the list of environment provisioned resources that was previously requested.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.list_environment_provisioned_resources_input.ListEnvironmentProvisionedResourcesInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.list_environment_provisioned_resources_output.ListEnvironmentProvisionedResourcesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_environment_provisioned_resources

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.list_environment_provisioned_resources.list_environment_provisioned_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_environment_provisioned_resources_input.ListEnvironmentProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["environment_name"] = environment_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEnvironmentProvisionedResourceResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def list(
        self,
        environment_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "aws_sdk_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "aws_sdk_proton.types.list_environment_provisioned_resources_output.ListEnvironmentProvisionedResourcesOutput":
        """<p>List the provisioned resources for your environment.</p>

        Args:
            environment_name: <p>The environment name.</p>
            next_token: <p>A token that indicates the location of the next environment provisioned resource in the array of environment provisioned resources, after the list of environment provisioned resources that was previously requested.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.list_environment_provisioned_resources_input.ListEnvironmentProvisionedResourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.list_environment_provisioned_resources_output.ListEnvironmentProvisionedResourcesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_environment_provisioned_resources

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.list_environment_provisioned_resources.async_list_environment_provisioned_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_environment_provisioned_resources_input.ListEnvironmentProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["environment_name"] = environment_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
