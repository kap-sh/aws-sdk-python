from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock._services.async_bedrock import ensure_async_iterator
from aws_sdk_bedrock._services.bedrock import ensure_sync_iterator
from aws_sdk_bedrock._services._pipeline import (
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
)
import aws_sdk_bedrock._auth._signers
import aws_sdk_bedrock._auth._sigv4

if TYPE_CHECKING:
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    import aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id
    import aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration
    import aws_sdk_bedrock.types.account_enforced_guardrail_output_configuration
    import aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request
    import aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response
    import aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request
    import aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request
    import aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response


class EnforcedGuardrailConfigurationResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def delete_enforced_guardrail_configuration(
        self,
        config_id: "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse":
        """<p>Deletes the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration.delete_enforced_guardrail_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["config_id"] = config_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_enforced_guardrails_configuration(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse":
        """<p>Lists the account-level enforced guardrail configurations.</p>

        Args:
            next_token: <p>Opaque continuation token of previous paginated response.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration.list_enforced_guardrails_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_enforced_guardrail_configuration(
        self,
        guardrail_inference_config: "aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration.AccountEnforcedGuardrailInferenceInputConfiguration",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        config_id: Optional[
            "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
        ] = None,
    ) -> "aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse":
        """<p>Sets the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>
            guardrail_inference_config: <p>Account-level enforced guardrail input configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration.put_enforced_guardrail_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
        if config_id is not None:
            input["config_id"] = config_id
        input["guardrail_inference_config"] = guardrail_inference_config

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncEnforcedGuardrailConfigurationResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def delete_enforced_guardrail_configuration(
        self,
        config_id: "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse":
        """<p>Deletes the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration.async_delete_enforced_guardrail_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
        input["config_id"] = config_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_enforced_guardrails_configuration(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse":
        """<p>Lists the account-level enforced guardrail configurations.</p>

        Args:
            next_token: <p>Opaque continuation token of previous paginated response.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration.async_list_enforced_guardrails_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_enforced_guardrail_configuration(
        self,
        guardrail_inference_config: "aws_sdk_bedrock.types.account_enforced_guardrail_inference_input_configuration.AccountEnforcedGuardrailInferenceInputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        config_id: Optional[
            "aws_sdk_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
        ] = None,
    ) -> "aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse":
        """<p>Sets the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>
            guardrail_inference_config: <p>Account-level enforced guardrail input configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration.async_put_enforced_guardrail_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest = {}  # type: ignore[typeddict-item]
        if config_id is not None:
            input["config_id"] = config_id
        input["guardrail_inference_config"] = guardrail_inference_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
