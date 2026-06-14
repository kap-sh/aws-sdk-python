from typing import TYPE_CHECKING, Optional

import aws_sdk_location._auth._signers
import aws_sdk_location._auth._sigv4
from aws_sdk_location._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_location.types.arn
    import aws_sdk_location.types.list_tags_for_resource_request
    import aws_sdk_location.types.list_tags_for_resource_response
    import aws_sdk_location.types.tag_keys
    import aws_sdk_location.types.tag_map
    import aws_sdk_location.types.tag_resource_request
    import aws_sdk_location.types.tag_resource_response
    import aws_sdk_location.types.untag_resource_request
    import aws_sdk_location.types.untag_resource_response
    from aws_sdk_location._services.async_location import (
        AsyncLocationClient,
        AsyncLocationClientConfig,
    )
    from aws_sdk_location._services.location import LocationClient, LocationClientConfig


class GenericResource:
    def __init__(self, service: LocationClient) -> None:
        self._service = service

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_location.types.arn.Arn",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "aws_sdk_location.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags that are applied to the specified Amazon Location resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_location.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_location.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_location._operations.location_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_location._operations.location_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_location.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_location.types.arn.Arn",
        tags: "aws_sdk_location.types.tag_map.TagMap",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "aws_sdk_location.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified Amazon Location Service resource.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.</p> <p>You can use the <code>TagResource</code> operation with an Amazon Location Service resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the tags already associated with the resource. If you specify a tag key that's already associated with the resource, the new tag value that you specify replaces the previous value for that tag. </p> <p>You can associate up to 50 tags with a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags you want to update.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
            tags: <p>Applies one or more tags to specific resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.</p> <p>Format: <code>\"key\" : \"value\"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource.</p> </li> <li> <p>Each tag key must be unique and must have exactly one associated value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @</p> </li> <li> <p>Cannot use \"aws:\" as a prefix for a key.</p> </li> </ul>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_location.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_location.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_location._operations.location_service.tag_resource

            output, http_response = (
                aws_sdk_location._operations.location_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_location.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_location.types.arn.Arn",
        tag_keys: "aws_sdk_location.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "aws_sdk_location.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified Amazon Location resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
            tag_keys: <p>The list of tag keys to remove from the specified resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_location.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_location.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_location._operations.location_service.untag_resource

            output, http_response = (
                aws_sdk_location._operations.location_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_location.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGenericResource:
    def __init__(self, service: AsyncLocationClient) -> None:
        self._service = service

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_location.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "aws_sdk_location.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags that are applied to the specified Amazon Location resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_location.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_location.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_location._operations.location_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_location._operations.location_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_location.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_location.types.arn.Arn",
        tags: "aws_sdk_location.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "aws_sdk_location.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified Amazon Location Service resource.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.</p> <p>You can use the <code>TagResource</code> operation with an Amazon Location Service resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the tags already associated with the resource. If you specify a tag key that's already associated with the resource, the new tag value that you specify replaces the previous value for that tag. </p> <p>You can associate up to 50 tags with a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags you want to update.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
            tags: <p>Applies one or more tags to specific resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.</p> <p>Format: <code>\"key\" : \"value\"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource.</p> </li> <li> <p>Each tag key must be unique and must have exactly one associated value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @</p> </li> <li> <p>Cannot use \"aws:\" as a prefix for a key.</p> </li> </ul>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_location.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_location.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_location._operations.location_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_location._operations.location_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_location.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_location.types.arn.Arn",
        tag_keys: "aws_sdk_location.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "aws_sdk_location.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified Amazon Location resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
            tag_keys: <p>The list of tag keys to remove from the specified resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_location.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_location.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_location._operations.location_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_location._operations.location_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_location.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
