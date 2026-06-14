from typing import TYPE_CHECKING, Optional

import aws_sdk_nova_act._auth._signers
import aws_sdk_nova_act._auth._sigv4
from aws_sdk_nova_act._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.list_models_request
    import aws_sdk_nova_act.types.list_models_response
    from aws_sdk_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
        AsyncNovaActClientConfig,
    )
    from aws_sdk_nova_act._services.nova_act import NovaActClient, NovaActClientConfig


class ModelResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service

    def list(
        self,
        client_compatibility_version: int,
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "aws_sdk_nova_act.types.list_models_response.ListModelsResponse":
        """<p>Lists all available AI models that can be used for workflow execution, including their status and compatibility information.</p>

        Args:
            client_compatibility_version: <p>The client compatibility version to filter models by compatibility.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_nova_act.types.list_models_request.ListModelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_nova_act.types.list_models_response.ListModelsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_models

            output, http_response = (
                aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_models.list_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.list_models_request.ListModelsRequest = {}  # type: ignore[typeddict-item]
        input_["client_compatibility_version"] = client_compatibility_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncModelResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service

    async def list(
        self,
        client_compatibility_version: int,
        *,
        config_overrides: Optional[AsyncNovaActClientConfig] = None,
    ) -> "aws_sdk_nova_act.types.list_models_response.ListModelsResponse":
        """<p>Lists all available AI models that can be used for workflow execution, including their status and compatibility information.</p>

        Args:
            client_compatibility_version: <p>The client compatibility version to filter models by compatibility.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_nova_act.types.list_models_request.ListModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_nova_act.types.list_models_response.ListModelsResponse"
        ]:
            import aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_models

            (
                output,
                http_response,
            ) = await aws_sdk_nova_act._operations.amazon_nova_agents_data_plane.list_models.async_list_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_nova_act.types.list_models_request.ListModelsRequest = {}  # type: ignore[typeddict-item]
        input_["client_compatibility_version"] = client_compatibility_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
