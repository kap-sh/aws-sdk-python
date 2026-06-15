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
    import aws_sdk_bedrock.types.list_tags_for_resource_request
    import aws_sdk_bedrock.types.list_tags_for_resource_response
    import aws_sdk_bedrock.types.tag_key_list
    import aws_sdk_bedrock.types.tag_list
    import aws_sdk_bedrock.types.tag_resource_request
    import aws_sdk_bedrock.types.tag_resource_response
    import aws_sdk_bedrock.types.taggable_resources_arn
    import aws_sdk_bedrock.types.untag_resource_request
    import aws_sdk_bedrock.types.untag_resource_response
    from aws_sdk_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from aws_sdk_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class TaggingResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_bedrock.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>List the tags associated with the specified resource.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_bedrock.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "aws_sdk_bedrock.types.tag_list.TagList",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.tag_resource_response.TagResourceResponse":
        r"""<p>Associate tags with a resource. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>Tags to associate with the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.tag_resource

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_bedrock.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "aws_sdk_bedrock.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Remove one or more tags from a resource. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to untag.</p>
            tag_keys: <p>Tag keys of the tags to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.untag_resource

            output, http_response = (
                aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTaggingResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_bedrock.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>List the tags associated with the specified resource.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_bedrock.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "aws_sdk_bedrock.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.tag_resource_response.TagResourceResponse":
        r"""<p>Associate tags with a resource. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>Tags to associate with the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_bedrock.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "aws_sdk_bedrock.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "aws_sdk_bedrock.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Remove one or more tags from a resource. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to untag.</p>
            tag_keys: <p>Tag keys of the tags to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock._operations.amazon_bedrock_control_plane_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
