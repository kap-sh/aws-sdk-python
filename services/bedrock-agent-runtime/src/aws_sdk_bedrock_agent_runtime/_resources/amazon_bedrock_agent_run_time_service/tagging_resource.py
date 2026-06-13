from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agent_runtime._auth._signers
import aws_sdk_bedrock_agent_runtime._auth._sigv4
from aws_sdk_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_request
    import aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_response
    import aws_sdk_bedrock_agent_runtime.types.tag_key_list
    import aws_sdk_bedrock_agent_runtime.types.tag_resource_request
    import aws_sdk_bedrock_agent_runtime.types.tag_resource_response
    import aws_sdk_bedrock_agent_runtime.types.taggable_resources_arn
    import aws_sdk_bedrock_agent_runtime.types.tags_map
    import aws_sdk_bedrock_agent_runtime.types.untag_resource_request
    import aws_sdk_bedrock_agent_runtime.types.untag_resource_response
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class TaggingResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all the tags for the resource you specify.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "aws_sdk_bedrock_agent_runtime.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock_agent_runtime.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Associate tags with a resource. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the Amazon Bedrock User Guide.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>An object containing key-value pairs that define the tags to attach to the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.tag_resource

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "aws_sdk_bedrock_agent_runtime.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of keys of the tags to remove from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.untag_resource

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTaggingResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all the tags for the resource you specify.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "aws_sdk_bedrock_agent_runtime.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> (
        "aws_sdk_bedrock_agent_runtime.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Associate tags with a resource. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Tagging resources</a> in the Amazon Bedrock User Guide.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>An object containing key-value pairs that define the tags to attach to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "aws_sdk_bedrock_agent_runtime.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of keys of the tags to remove from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
