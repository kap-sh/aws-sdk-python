from __future__ import annotations

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
    import aws_sdk_proton.types.list_component_provisioned_resources_input
    import aws_sdk_proton.types.list_component_provisioned_resources_output
    import aws_sdk_proton.types.provisioned_resource
    import aws_sdk_proton.types.resource_name
    from aws_sdk_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig


class ComponentProvisionedResourceResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def list(
        self,
        component_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[
            "aws_sdk_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "aws_sdk_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput":
        r"""<p>List provisioned resources for a component with details.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component whose provisioned resources you want.</p>
            next_token: <p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_component_provisioned_resources

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.list_component_provisioned_resources.list_component_provisioned_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["component_name"] = component_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncComponentProvisionedResourceResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def list(
        self,
        component_name: "aws_sdk_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "aws_sdk_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "aws_sdk_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput":
        r"""<p>List provisioned resources for a component with details.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component whose provisioned resources you want.</p>
            next_token: <p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_component_provisioned_resources

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.list_component_provisioned_resources.async_list_component_provisioned_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput = {}  # type: ignore[typeddict-item]
        input_["component_name"] = component_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
