from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_data_automation._auth._signers
import aws_sdk_bedrock_data_automation._auth._sigv4
from aws_sdk_bedrock_data_automation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_invocation_arn
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_object
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_output_configuration
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_samples
    import aws_sdk_bedrock_data_automation.types.data_automation_profile_arn
    import aws_sdk_bedrock_data_automation.types.encryption_configuration
    import aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_request
    import aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_response
    import aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_request
    import aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_response
    import aws_sdk_bedrock_data_automation.types.tag_list
    from aws_sdk_bedrock_data_automation._services.async_bedrock_data_automation import (
        AsyncBedrockDataAutomationClient,
        AsyncBedrockDataAutomationClientConfig,
    )
    from aws_sdk_bedrock_data_automation._services.bedrock_data_automation import (
        BedrockDataAutomationClient,
        BedrockDataAutomationClientConfig,
    )


class BlueprintOptimizationJobResource:
    def __init__(self, service: BedrockDataAutomationClient) -> None:
        self._service = service

    def create(
        self,
        blueprint: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_object.BlueprintOptimizationObject",
        samples: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_samples.BlueprintOptimizationSamples",
        output_configuration: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_output_configuration.BlueprintOptimizationOutputConfiguration",
        data_automation_profile_arn: "aws_sdk_bedrock_data_automation.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse":
        """Invoke an async job to perform Blueprint Optimization

        Args:
            blueprint: Blueprint to be optimized
            samples: List of Blueprint Optimization Samples
            output_configuration: Output configuration where the results should be placed
            data_automation_profile_arn: Data automation profile ARN
            encryption_configuration: Encryption configuration.
            tags: List of tags.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async.invoke_blueprint_optimization_async(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint"] = blueprint
        input_["samples"] = samples
        input_["output_configuration"] = output_configuration
        input_["data_automation_profile_arn"] = data_automation_profile_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
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
        invocation_arn: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_invocation_arn.BlueprintOptimizationInvocationArn",
        *,
        config_overrides: Optional[BedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse":
        """API used to get blueprint optimization status.

        Args:
            invocation_arn: Invocation arn.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status

            output, http_response = (
                aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status.get_blueprint_optimization_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["invocation_arn"] = invocation_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncBlueprintOptimizationJobResource:
    def __init__(self, service: AsyncBedrockDataAutomationClient) -> None:
        self._service = service

    async def create(
        self,
        blueprint: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_object.BlueprintOptimizationObject",
        samples: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_samples.BlueprintOptimizationSamples",
        output_configuration: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_output_configuration.BlueprintOptimizationOutputConfiguration",
        data_automation_profile_arn: "aws_sdk_bedrock_data_automation.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
        encryption_configuration: Optional[
            "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["aws_sdk_bedrock_data_automation.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse":
        """Invoke an async job to perform Blueprint Optimization

        Args:
            blueprint: Blueprint to be optimized
            samples: List of Blueprint Optimization Samples
            output_configuration: Output configuration where the results should be placed
            data_automation_profile_arn: Data automation profile ARN
            encryption_configuration: Encryption configuration.
            tags: List of tags.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_response.InvokeBlueprintOptimizationAsyncResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.invoke_blueprint_optimization_async.async_invoke_blueprint_optimization_async(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.invoke_blueprint_optimization_async_request.InvokeBlueprintOptimizationAsyncRequest = {}  # type: ignore[typeddict-item]
        input_["blueprint"] = blueprint
        input_["samples"] = samples
        input_["output_configuration"] = output_configuration
        input_["data_automation_profile_arn"] = data_automation_profile_arn
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
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
        invocation_arn: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_invocation_arn.BlueprintOptimizationInvocationArn",
        *,
        config_overrides: Optional[AsyncBedrockDataAutomationClientConfig] = None,
    ) -> "aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse":
        """API used to get blueprint optimization status.

        Args:
            invocation_arn: Invocation arn.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_response.GetBlueprintOptimizationStatusResponse"
        ]:
            import aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_data_automation._operations.amazon_bedrock_keystone_build_time_service.get_blueprint_optimization_status.async_get_blueprint_optimization_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_data_automation.types.get_blueprint_optimization_status_request.GetBlueprintOptimizationStatusRequest = {}  # type: ignore[typeddict-item]
        input_["invocation_arn"] = invocation_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
