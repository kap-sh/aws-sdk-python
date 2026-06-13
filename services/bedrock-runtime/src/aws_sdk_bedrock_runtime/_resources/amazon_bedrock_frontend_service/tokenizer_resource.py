from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_runtime._auth._signers
import aws_sdk_bedrock_runtime._auth._sigv4
from aws_sdk_bedrock_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.count_tokens_input
    import aws_sdk_bedrock_runtime.types.count_tokens_request
    import aws_sdk_bedrock_runtime.types.count_tokens_response
    import aws_sdk_bedrock_runtime.types.foundation_model_version_identifier
    from aws_sdk_bedrock_runtime._services.async_bedrock_runtime import (
        AsyncBedrockRuntimeClient,
        AsyncBedrockRuntimeClientConfig,
    )
    from aws_sdk_bedrock_runtime._services.bedrock_runtime import (
        BedrockRuntimeClient,
        BedrockRuntimeClientConfig,
    )


class TokenizerResource:
    def __init__(self, service: BedrockRuntimeClient) -> None:
        self._service = service

    def count_tokens(
        self,
        model_id: "aws_sdk_bedrock_runtime.types.foundation_model_version_identifier.FoundationModelVersionIdentifier",
        input: "aws_sdk_bedrock_runtime.types.count_tokens_input.CountTokensInput",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_runtime.types.count_tokens_response.CountTokensResponse":
        """<p>Returns the token count for a given inference request. This operation helps you estimate token usage before sending requests to foundation models by returning the token count that would be used if the same input were sent to the model in an inference request.</p> <p>Token counting is model-specific because different models use different tokenization strategies. The token count returned by this operation will match the token count that would be charged if the same input were sent to the model in an <code>InvokeModel</code> or <code>Converse</code> request.</p> <p>You can use this operation to:</p> <ul> <li> <p>Estimate costs before sending inference requests.</p> </li> <li> <p>Optimize prompts to fit within token limits.</p> </li> <li> <p>Plan for token usage in your applications.</p> </li> </ul> <p>This operation accepts the same input formats as <code>InvokeModel</code> and <code>Converse</code>, allowing you to count tokens for both raw text inputs and structured conversation formats.</p> <p>The following operations are related to <code>CountTokens</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock/latest/API/API_runtime_InvokeModel.html\">InvokeModel</a> - Sends inference requests to foundation models</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock/latest/API/API_runtime_Converse.html\">Converse</a> - Sends conversation-based inference requests to foundation models</p> </li> </ul>

        Args:
            model_id: <p>The unique identifier or ARN of the foundation model to use for token counting. Each model processes tokens differently, so the token count is specific to the model you specify.</p>
            input: <p>The input for which to count tokens. The structure of this parameter depends on whether you're counting tokens for an <code>InvokeModel</code> or <code>Converse</code> request:</p> <ul> <li> <p>For <code>InvokeModel</code> requests, provide the request body in the <code>invokeModel</code> field</p> </li> <li> <p>For <code>Converse</code> requests, provide the messages and system content in the <code>converse</code> field</p> </li> </ul> <p>The input format must be compatible with the model specified in the <code>modelId</code> parameter.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_runtime.types.count_tokens_request.CountTokensRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_runtime.types.count_tokens_response.CountTokensResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.count_tokens

            output, http_response = (
                aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.count_tokens.count_tokens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_runtime.types.count_tokens_request.CountTokensRequest = {}  # type: ignore[typeddict-item]
        input["model_id"] = model_id
        input["input"] = input

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTokenizerResource:
    def __init__(self, service: AsyncBedrockRuntimeClient) -> None:
        self._service = service

    async def count_tokens(
        self,
        model_id: "aws_sdk_bedrock_runtime.types.foundation_model_version_identifier.FoundationModelVersionIdentifier",
        input: "aws_sdk_bedrock_runtime.types.count_tokens_input.CountTokensInput",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_runtime.types.count_tokens_response.CountTokensResponse":
        """<p>Returns the token count for a given inference request. This operation helps you estimate token usage before sending requests to foundation models by returning the token count that would be used if the same input were sent to the model in an inference request.</p> <p>Token counting is model-specific because different models use different tokenization strategies. The token count returned by this operation will match the token count that would be charged if the same input were sent to the model in an <code>InvokeModel</code> or <code>Converse</code> request.</p> <p>You can use this operation to:</p> <ul> <li> <p>Estimate costs before sending inference requests.</p> </li> <li> <p>Optimize prompts to fit within token limits.</p> </li> <li> <p>Plan for token usage in your applications.</p> </li> </ul> <p>This operation accepts the same input formats as <code>InvokeModel</code> and <code>Converse</code>, allowing you to count tokens for both raw text inputs and structured conversation formats.</p> <p>The following operations are related to <code>CountTokens</code>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock/latest/API/API_runtime_InvokeModel.html\">InvokeModel</a> - Sends inference requests to foundation models</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/bedrock/latest/API/API_runtime_Converse.html\">Converse</a> - Sends conversation-based inference requests to foundation models</p> </li> </ul>

        Args:
            model_id: <p>The unique identifier or ARN of the foundation model to use for token counting. Each model processes tokens differently, so the token count is specific to the model you specify.</p>
            input: <p>The input for which to count tokens. The structure of this parameter depends on whether you're counting tokens for an <code>InvokeModel</code> or <code>Converse</code> request:</p> <ul> <li> <p>For <code>InvokeModel</code> requests, provide the request body in the <code>invokeModel</code> field</p> </li> <li> <p>For <code>Converse</code> requests, provide the messages and system content in the <code>converse</code> field</p> </li> </ul> <p>The input format must be compatible with the model specified in the <code>modelId</code> parameter.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_runtime.types.count_tokens_request.CountTokensRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_runtime.types.count_tokens_response.CountTokensResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.count_tokens

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.count_tokens.async_count_tokens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_runtime.types.count_tokens_request.CountTokensRequest = {}  # type: ignore[typeddict-item]
        input["model_id"] = model_id
        input["input"] = input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
