from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4
from aws_sdk_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.get_foundation_model_identifier
    import aws_sdk_bedrock.types.get_foundation_model_request
    import aws_sdk_bedrock.types.get_foundation_model_response
    import aws_sdk_bedrock.types.inference_type
    import aws_sdk_bedrock.types.list_foundation_models_request
    import aws_sdk_bedrock.types.list_foundation_models_response
    import aws_sdk_bedrock.types.model_customization
    import aws_sdk_bedrock.types.model_modality
    import aws_sdk_bedrock.types.provider
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class ModelResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def get_foundation_model(
        self,
        model_identifier: "aws_sdk_bedrock.types.get_foundation_model_identifier.GetFoundationModelIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock.types.get_foundation_model_response.GetFoundationModelResponse"
    ):
        """<p>Get details about a Amazon Bedrock foundation model.</p>

        Args:
            model_identifier: <p>The model identifier. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_foundation_model_request.GetFoundationModelRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_foundation_model_response.GetFoundationModelResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model.get_foundation_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_foundation_model_request.GetFoundationModelRequest = {}  # type: ignore[typeddict-item]
        input["model_identifier"] = model_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_foundation_models(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        by_provider: Optional["aws_sdk_bedrock.types.provider.Provider"] = None,
        by_customization_type: Optional[
            "aws_sdk_bedrock.types.model_customization.ModelCustomization"
        ] = None,
        by_output_modality: Optional[
            "aws_sdk_bedrock.types.model_modality.ModelModality"
        ] = None,
        by_inference_type: Optional[
            "aws_sdk_bedrock.types.inference_type.InferenceType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse":
        """<p>Lists Amazon Bedrock foundation models that you can use. You can filter the results with the request parameters. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models.html\">Foundation models</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            by_provider: <p>Return models belonging to the model provider that you specify.</p>
            by_customization_type: <p>Return models that support the customization type that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html\">Custom models</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>
            by_output_modality: <p>Return models that support the output modality that you specify.</p>
            by_inference_type: <p>Return models that support the inference type that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models.list_foundation_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest = {}  # type: ignore[typeddict-item]
        if by_provider is not None:
            input["by_provider"] = by_provider
        if by_customization_type is not None:
            input["by_customization_type"] = by_customization_type
        if by_output_modality is not None:
            input["by_output_modality"] = by_output_modality
        if by_inference_type is not None:
            input["by_inference_type"] = by_inference_type

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncModelResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def get_foundation_model(
        self,
        model_identifier: "aws_sdk_bedrock.types.get_foundation_model_identifier.GetFoundationModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock.types.get_foundation_model_response.GetFoundationModelResponse"
    ):
        """<p>Get details about a Amazon Bedrock foundation model.</p>

        Args:
            model_identifier: <p>The model identifier. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_foundation_model_request.GetFoundationModelRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_foundation_model_response.GetFoundationModelResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model.async_get_foundation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.get_foundation_model_request.GetFoundationModelRequest = {}  # type: ignore[typeddict-item]
        input["model_identifier"] = model_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_foundation_models(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        by_provider: Optional["aws_sdk_bedrock.types.provider.Provider"] = None,
        by_customization_type: Optional[
            "aws_sdk_bedrock.types.model_customization.ModelCustomization"
        ] = None,
        by_output_modality: Optional[
            "aws_sdk_bedrock.types.model_modality.ModelModality"
        ] = None,
        by_inference_type: Optional[
            "aws_sdk_bedrock.types.inference_type.InferenceType"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse":
        """<p>Lists Amazon Bedrock foundation models that you can use. You can filter the results with the request parameters. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models.html\">Foundation models</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            by_provider: <p>Return models belonging to the model provider that you specify.</p>
            by_customization_type: <p>Return models that support the customization type that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html\">Custom models</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>
            by_output_modality: <p>Return models that support the output modality that you specify.</p>
            by_inference_type: <p>Return models that support the inference type that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html\">Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models.async_list_foundation_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest = {}  # type: ignore[typeddict-item]
        if by_provider is not None:
            input["by_provider"] = by_provider
        if by_customization_type is not None:
            input["by_customization_type"] = by_customization_type
        if by_output_modality is not None:
            input["by_output_modality"] = by_output_modality
        if by_inference_type is not None:
            input["by_inference_type"] = by_inference_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
