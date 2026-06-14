from typing import TYPE_CHECKING, Optional

import aws_sdk_omics._auth._signers
import aws_sdk_omics._auth._sigv4
from aws_sdk_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_omics.types.list_tags_for_resource_request
    import aws_sdk_omics.types.list_tags_for_resource_response
    import aws_sdk_omics.types.tag_arn
    import aws_sdk_omics.types.tag_key_list
    import aws_sdk_omics.types.tag_map
    import aws_sdk_omics.types.tag_resource_request
    import aws_sdk_omics.types.tag_resource_response
    import aws_sdk_omics.types.untag_resource_request
    import aws_sdk_omics.types.untag_resource_response
    from aws_sdk_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from aws_sdk_omics._services.omics import OmicsClient, OmicsClientConfig


class TaggingResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def list(
        self,
        resource_arn: "aws_sdk_omics.types.tag_arn.TagArn",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_tags_for_resource

            output, http_response = (
                aws_sdk_omics._operations.omics.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_omics.types.tag_arn.TagArn",
        tags: "aws_sdk_omics.types.tag_map.TagMap",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tags: <p>Tags for the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_omics._operations.omics.tag_resource

            output, http_response = (
                aws_sdk_omics._operations.omics.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_omics.types.tag_arn.TagArn",
        tag_keys: "aws_sdk_omics.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tag_keys: <p>Keys of tags to remove.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_omics.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_omics.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_omics._operations.omics.untag_resource

            output, http_response = (
                aws_sdk_omics._operations.omics.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTaggingResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def list(
        self,
        resource_arn: "aws_sdk_omics.types.tag_arn.TagArn",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_omics._operations.omics.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_omics.types.tag_arn.TagArn",
        tags: "aws_sdk_omics.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tags: <p>Tags for the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_omics._operations.omics.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_omics.types.tag_arn.TagArn",
        tag_keys: "aws_sdk_omics.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "aws_sdk_omics.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tag_keys: <p>Keys of tags to remove.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_omics.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_omics.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_omics._operations.omics.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_omics._operations.omics.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_omics.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
