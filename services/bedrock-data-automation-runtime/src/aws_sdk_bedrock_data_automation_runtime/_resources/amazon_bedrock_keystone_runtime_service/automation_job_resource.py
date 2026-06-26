from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from aws_sdk_bedrock_data_automation_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.blueprint_list
    import aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.data_automation_profile_arn
    import aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_request
    import aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_response
    import aws_sdk_bedrock_data_automation_runtime.types.idempotency_token
    import aws_sdk_bedrock_data_automation_runtime.types.input_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.invocation_arn
    import aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_request
    import aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_response
    import aws_sdk_bedrock_data_automation_runtime.types.notification_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.output_configuration
    import aws_sdk_bedrock_data_automation_runtime.types.tag_list
    from aws_sdk_bedrock_data_automation_runtime._services.async_bedrock_data_automation_runtime import (
        AsyncBedrockDataAutomationRuntimeClient,
        AsyncBedrockDataAutomationRuntimeClientConfig,
    )
    from aws_sdk_bedrock_data_automation_runtime._services.bedrock_data_automation_runtime import (
        BedrockDataAutomationRuntimeClient,
        BedrockDataAutomationRuntimeClientConfig,
    )


class AutomationJobResource:
    def __init__(self, service: BedrockDataAutomationRuntimeClient) -> None:
        self._service = service

    def create(
        self,
        input_configuration: "aws_sdk_bedrock_data_automation_runtime.types.input_configuration.InputConfiguration",
        output_configuration: "aws_sdk_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration",
        data_automation_profile_arn: "aws_sdk_bedrock_data_automation_runtime.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[BedrockDataAutomationRuntimeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.idempotency_token.IdempotencyToken"
        ] = None,
        data_automation_configuration: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration.DataAutomationConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        notification_configuration: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.notification_configuration.NotificationConfiguration"
        ] = None,
        blueprints: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.blueprint_list.BlueprintList"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.tag_list.TagList"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_response.InvokeDataAutomationAsyncResponse":
        """Async API: Invoke data automation.

        Args:
            client_token: Idempotency token.
            input_configuration: Input configuration.
            output_configuration: Output configuration.
            data_automation_configuration: Data automation configuration.
            encryption_configuration: Encryption configuration.
            notification_configuration: Notification configuration.
            blueprints: Blueprint list.
            data_automation_profile_arn: Data automation profile ARN
            tags: List of tags.

        Raises:
            aws_sdk_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            aws_sdk_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            aws_sdk_bedrock_data_automation_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception will be thrown when service quota is exceeded.
            aws_sdk_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            aws_sdk_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            aws_sdk_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_request.InvokeDataAutomationAsyncRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_response.InvokeDataAutomationAsyncResponse"
        ]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation_async

            output, http_response = (
                aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation_async.invoke_data_automation_async(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_request.InvokeDataAutomationAsyncRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["input_configuration"] = input_configuration
        input_["output_configuration"] = output_configuration
        if data_automation_configuration is not None:
            input_["data_automation_configuration"] = data_automation_configuration
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if notification_configuration is not None:
            input_["notification_configuration"] = notification_configuration
        if blueprints is not None:
            input_["blueprints"] = blueprints
        input_["data_automation_profile_arn"] = data_automation_profile_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        invocation_arn: "aws_sdk_bedrock_data_automation_runtime.types.invocation_arn.InvocationArn",
        *,
        config_overrides: Optional[BedrockDataAutomationRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_response.GetDataAutomationStatusResponse":
        """API used to get data automation status.

        Args:
            invocation_arn: Invocation arn.

        Raises:
            aws_sdk_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            aws_sdk_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            aws_sdk_bedrock_data_automation_runtime.errors.resource_not_found_exception.ResourceNotFoundException: This exception will be thrown when resource provided from customer not found.
            aws_sdk_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            aws_sdk_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            aws_sdk_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_request.GetDataAutomationStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_response.GetDataAutomationStatusResponse"
        ]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.get_data_automation_status

            output, http_response = (
                aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.get_data_automation_status.get_data_automation_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_request.GetDataAutomationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["invocation_arn"] = invocation_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAutomationJobResource:
    def __init__(self, service: AsyncBedrockDataAutomationRuntimeClient) -> None:
        self._service = service

    async def create(
        self,
        input_configuration: "aws_sdk_bedrock_data_automation_runtime.types.input_configuration.InputConfiguration",
        output_configuration: "aws_sdk_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration",
        data_automation_profile_arn: "aws_sdk_bedrock_data_automation_runtime.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[
            AsyncBedrockDataAutomationRuntimeClientConfig
        ] = None,
        client_token: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.idempotency_token.IdempotencyToken"
        ] = None,
        data_automation_configuration: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.data_automation_configuration.DataAutomationConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        notification_configuration: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.notification_configuration.NotificationConfiguration"
        ] = None,
        blueprints: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.blueprint_list.BlueprintList"
        ] = None,
        tags: Optional[
            "aws_sdk_bedrock_data_automation_runtime.types.tag_list.TagList"
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_response.InvokeDataAutomationAsyncResponse":
        """Async API: Invoke data automation.

        Args:
            client_token: Idempotency token.
            input_configuration: Input configuration.
            output_configuration: Output configuration.
            data_automation_configuration: Data automation configuration.
            encryption_configuration: Encryption configuration.
            notification_configuration: Notification configuration.
            blueprints: Blueprint list.
            data_automation_profile_arn: Data automation profile ARN
            tags: List of tags.

        Raises:
            aws_sdk_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            aws_sdk_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            aws_sdk_bedrock_data_automation_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception will be thrown when service quota is exceeded.
            aws_sdk_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            aws_sdk_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            aws_sdk_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_request.InvokeDataAutomationAsyncRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_response.InvokeDataAutomationAsyncResponse"
        ]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation_async

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation_async.async_invoke_data_automation_async(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation_runtime.types.invoke_data_automation_async_request.InvokeDataAutomationAsyncRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input_["client_token"] = client_token
        input_["input_configuration"] = input_configuration
        input_["output_configuration"] = output_configuration
        if data_automation_configuration is not None:
            input_["data_automation_configuration"] = data_automation_configuration
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if notification_configuration is not None:
            input_["notification_configuration"] = notification_configuration
        if blueprints is not None:
            input_["blueprints"] = blueprints
        input_["data_automation_profile_arn"] = data_automation_profile_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        invocation_arn: "aws_sdk_bedrock_data_automation_runtime.types.invocation_arn.InvocationArn",
        *,
        config_overrides: Optional[
            AsyncBedrockDataAutomationRuntimeClientConfig
        ] = None,
    ) -> "aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_response.GetDataAutomationStatusResponse":
        """API used to get data automation status.

        Args:
            invocation_arn: Invocation arn.

        Raises:
            aws_sdk_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            aws_sdk_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            aws_sdk_bedrock_data_automation_runtime.errors.resource_not_found_exception.ResourceNotFoundException: This exception will be thrown when resource provided from customer not found.
            aws_sdk_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            aws_sdk_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            aws_sdk_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_request.GetDataAutomationStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_response.GetDataAutomationStatusResponse"
        ]:
            import aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.get_data_automation_status

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.get_data_automation_status.async_get_data_automation_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation_runtime.types.get_data_automation_status_request.GetDataAutomationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["invocation_arn"] = invocation_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
