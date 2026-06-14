from typing import TYPE_CHECKING, Optional

import aws_sdk_controltower._auth._signers
import aws_sdk_controltower._auth._sigv4
from aws_sdk_controltower._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_controltower.types.arn
    import aws_sdk_controltower.types.list_tags_for_resource_input
    import aws_sdk_controltower.types.list_tags_for_resource_output
    import aws_sdk_controltower.types.tag_keys
    import aws_sdk_controltower.types.tag_map
    import aws_sdk_controltower.types.tag_resource_input
    import aws_sdk_controltower.types.tag_resource_output
    import aws_sdk_controltower.types.untag_resource_input
    import aws_sdk_controltower.types.untag_resource_output
    from aws_sdk_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from aws_sdk_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class TaggingResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def list(
        self,
        resource_arn: "aws_sdk_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns a list of tags associated with the resource. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p> The ARN of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_tags_for_resource

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_controltower.types.arn.Arn",
        tags: "aws_sdk_controltower.types.tag_map.TagMap",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.tag_resource_output.TagResourceOutput":
        """<p>Applies tags to a resource. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be tagged.</p>
            tags: <p>Tags to be applied to the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.tag_resource

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_controltower.types.arn.Arn",
        tag_keys: "aws_sdk_controltower.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from a resource. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>Tag keys to be removed from the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_controltower.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "aws_sdk_controltower.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.untag_resource

            output, http_response = (
                aws_sdk_controltower._operations.aws_control_tower_apis.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncTaggingResource:
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def list(
        self,
        resource_arn: "aws_sdk_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns a list of tags associated with the resource. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p> The ARN of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_controltower.types.arn.Arn",
        tags: "aws_sdk_controltower.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.tag_resource_output.TagResourceOutput":
        """<p>Applies tags to a resource. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be tagged.</p>
            tags: <p>Tags to be applied to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.tag_resource_output.TagResourceOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.tag_resource_input.TagResourceInput = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_controltower.types.arn.Arn",
        tag_keys: "aws_sdk_controltower.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "aws_sdk_controltower.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from a resource. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>Tag keys to be removed from the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_controltower.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_controltower.types.untag_resource_output.UntagResourceOutput"
        ]:
            import aws_sdk_controltower._operations.aws_control_tower_apis.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_controltower._operations.aws_control_tower_apis.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_controltower.types.untag_resource_input.UntagResourceInput = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
