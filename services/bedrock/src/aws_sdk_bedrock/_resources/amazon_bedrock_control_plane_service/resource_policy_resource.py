from __future__ import annotations

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
    import aws_sdk_bedrock.types.delete_resource_policy_request
    import aws_sdk_bedrock.types.delete_resource_policy_response
    import aws_sdk_bedrock.types.get_resource_policy_request
    import aws_sdk_bedrock.types.get_resource_policy_response
    import aws_sdk_bedrock.types.put_resource_policy_request
    import aws_sdk_bedrock.types.put_resource_policy_response
    import aws_sdk_bedrock.types.resource_policy_document
    import aws_sdk_bedrock.types.resource_policy_resource_arn
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class ResourcePolicyResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a previously created Bedrock resource policy.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Gets the resource policy document for a Bedrock resource</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        resource_policy: "aws_sdk_bedrock.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Adds a resource policy for a Bedrock resource.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>
            resource_policy: <p>The JSON string representing the Bedrock resource policy.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_policy"] = resource_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncResourcePolicyResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def delete_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a previously created Bedrock resource policy.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Gets the resource policy document for a Bedrock resource</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "aws_sdk_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        resource_policy: "aws_sdk_bedrock.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Adds a resource policy for a Bedrock resource.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>
            resource_policy: <p>The JSON string representing the Bedrock resource policy.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["resource_policy"] = resource_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
