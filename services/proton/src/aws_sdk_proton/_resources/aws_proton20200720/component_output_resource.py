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
    import aws_sdk_proton.types.deployment_id
    import aws_sdk_proton.types.empty_next_token
    import aws_sdk_proton.types.list_component_outputs_input
    import aws_sdk_proton.types.list_component_outputs_output
    import aws_sdk_proton.types.output
    import aws_sdk_proton.types.resource_name
    from aws_sdk_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from aws_sdk_proton._services.proton import ProtonClient, ProtonClientConfig


class ComponentOutputResource:
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
        deployment_id: Optional[
            "aws_sdk_proton.types.deployment_id.DeploymentId"
        ] = None,
    ) -> (
        "aws_sdk_proton.types.list_component_outputs_output.ListComponentOutputsOutput"
    ):
        r"""<p>Get a list of component Infrastructure as Code (IaC) outputs.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component whose outputs you want.</p>
            next_token: <p>A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.</p>
            deployment_id: <p>The ID of the deployment whose outputs you want.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_proton.types.list_component_outputs_input.ListComponentOutputsInput]",
        ) -> OperationResponse[
            "aws_sdk_proton.types.list_component_outputs_output.ListComponentOutputsOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_component_outputs

            output, http_response = (
                aws_sdk_proton._operations.aws_proton20200720.list_component_outputs.list_component_outputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_component_outputs_input.ListComponentOutputsInput = {}  # type: ignore[typeddict-item]
        input_["component_name"] = component_name
        if next_token is not None:
            input_["next_token"] = next_token
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncComponentOutputResource:
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
        deployment_id: Optional[
            "aws_sdk_proton.types.deployment_id.DeploymentId"
        ] = None,
    ) -> (
        "aws_sdk_proton.types.list_component_outputs_output.ListComponentOutputsOutput"
    ):
        r"""<p>Get a list of component Infrastructure as Code (IaC) outputs.</p> <p>For more information about components, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component whose outputs you want.</p>
            next_token: <p>A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.</p>
            deployment_id: <p>The ID of the deployment whose outputs you want.</p>

        Raises:
            aws_sdk_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            aws_sdk_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            aws_sdk_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            aws_sdk_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            aws_sdk_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_proton.types.list_component_outputs_input.ListComponentOutputsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_proton.types.list_component_outputs_output.ListComponentOutputsOutput"
        ]:
            import aws_sdk_proton._operations.aws_proton20200720.list_component_outputs

            (
                output,
                http_response,
            ) = await aws_sdk_proton._operations.aws_proton20200720.list_component_outputs.async_list_component_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_proton.types.list_component_outputs_input.ListComponentOutputsInput = {}  # type: ignore[typeddict-item]
        input_["component_name"] = component_name
        if next_token is not None:
            input_["next_token"] = next_token
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
