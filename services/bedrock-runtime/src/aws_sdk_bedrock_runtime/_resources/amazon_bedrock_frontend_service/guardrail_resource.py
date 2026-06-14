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
    import aws_sdk_bedrock_runtime.types.apply_guardrail_request
    import aws_sdk_bedrock_runtime.types.apply_guardrail_response
    import aws_sdk_bedrock_runtime.types.guardrail_content_block_list
    import aws_sdk_bedrock_runtime.types.guardrail_content_source
    import aws_sdk_bedrock_runtime.types.guardrail_identifier
    import aws_sdk_bedrock_runtime.types.guardrail_output_scope
    import aws_sdk_bedrock_runtime.types.guardrail_version
    from aws_sdk_bedrock_runtime._services.async_bedrock_runtime import (
        AsyncBedrockRuntimeClient,
        AsyncBedrockRuntimeClientConfig,
    )
    from aws_sdk_bedrock_runtime._services.bedrock_runtime import (
        BedrockRuntimeClient,
        BedrockRuntimeClientConfig,
    )


class GuardrailResource:
    def __init__(self, service: BedrockRuntimeClient) -> None:
        self._service = service

    def apply_guardrail(
        self,
        guardrail_identifier: "aws_sdk_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier",
        guardrail_version: "aws_sdk_bedrock_runtime.types.guardrail_version.GuardrailVersion",
        source: "aws_sdk_bedrock_runtime.types.guardrail_content_source.GuardrailContentSource",
        content: "aws_sdk_bedrock_runtime.types.guardrail_content_block_list.GuardrailContentBlockList",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        output_scope: Optional[
            "aws_sdk_bedrock_runtime.types.guardrail_output_scope.GuardrailOutputScope"
        ] = None,
    ) -> (
        "aws_sdk_bedrock_runtime.types.apply_guardrail_response.ApplyGuardrailResponse"
    ):
        """<p>The action to apply a guardrail.</p> <p>For troubleshooting some of the common errors you might encounter when using the <code>ApplyGuardrail</code> API, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html\">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            guardrail_identifier: <p>The guardrail identifier used in the request to apply the guardrail.</p>
            guardrail_version: <p>The guardrail version used in the request to apply the guardrail.</p>
            source: <p>The source of data used in the request to apply the guardrail.</p>
            content: <p>The content details used in the request to apply the guardrail.</p>
            output_scope: <p>Specifies the scope of the output that you get in the response. Set to <code>FULL</code> to return the entire output, including any detected and non-detected entries in the response for enhanced debugging.</p> <p>Note that the full output scope doesn't apply to word filters or regex in sensitive information filters. It does apply to all other filtering policies, including sensitive information with filters that can detect personally identifiable information (PII).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_runtime.types.apply_guardrail_request.ApplyGuardrailRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_runtime.types.apply_guardrail_response.ApplyGuardrailResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.apply_guardrail

            output, http_response = (
                aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.apply_guardrail.apply_guardrail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_runtime.types.apply_guardrail_request.ApplyGuardrailRequest = {}  # type: ignore[typeddict-item]
        input_["guardrail_identifier"] = guardrail_identifier
        input_["guardrail_version"] = guardrail_version
        input_["source"] = source
        input_["content"] = content
        if output_scope is not None:
            input_["output_scope"] = output_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGuardrailResource:
    def __init__(self, service: AsyncBedrockRuntimeClient) -> None:
        self._service = service

    async def apply_guardrail(
        self,
        guardrail_identifier: "aws_sdk_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier",
        guardrail_version: "aws_sdk_bedrock_runtime.types.guardrail_version.GuardrailVersion",
        source: "aws_sdk_bedrock_runtime.types.guardrail_content_source.GuardrailContentSource",
        content: "aws_sdk_bedrock_runtime.types.guardrail_content_block_list.GuardrailContentBlockList",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        output_scope: Optional[
            "aws_sdk_bedrock_runtime.types.guardrail_output_scope.GuardrailOutputScope"
        ] = None,
    ) -> (
        "aws_sdk_bedrock_runtime.types.apply_guardrail_response.ApplyGuardrailResponse"
    ):
        """<p>The action to apply a guardrail.</p> <p>For troubleshooting some of the common errors you might encounter when using the <code>ApplyGuardrail</code> API, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html\">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            guardrail_identifier: <p>The guardrail identifier used in the request to apply the guardrail.</p>
            guardrail_version: <p>The guardrail version used in the request to apply the guardrail.</p>
            source: <p>The source of data used in the request to apply the guardrail.</p>
            content: <p>The content details used in the request to apply the guardrail.</p>
            output_scope: <p>Specifies the scope of the output that you get in the response. Set to <code>FULL</code> to return the entire output, including any detected and non-detected entries in the response for enhanced debugging.</p> <p>Note that the full output scope doesn't apply to word filters or regex in sensitive information filters. It does apply to all other filtering policies, including sensitive information with filters that can detect personally identifiable information (PII).</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_runtime.types.apply_guardrail_request.ApplyGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_runtime.types.apply_guardrail_response.ApplyGuardrailResponse"
        ]:
            import aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.apply_guardrail

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_runtime._operations.amazon_bedrock_frontend_service.apply_guardrail.async_apply_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_runtime.types.apply_guardrail_request.ApplyGuardrailRequest = {}  # type: ignore[typeddict-item]
        input_["guardrail_identifier"] = guardrail_identifier
        input_["guardrail_version"] = guardrail_version
        input_["source"] = source
        input_["content"] = content
        if output_scope is not None:
            input_["output_scope"] = output_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
