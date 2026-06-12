from typing import TYPE_CHECKING, Optional

import aws_sdk_elementalinference._auth._signers
import aws_sdk_elementalinference._auth._sigv4
from aws_sdk_elementalinference._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.associate_feed_request
    import aws_sdk_elementalinference.types.associate_feed_response
    import aws_sdk_elementalinference.types.associated_resource_name
    import aws_sdk_elementalinference.types.create_feed_request
    import aws_sdk_elementalinference.types.create_feed_response
    import aws_sdk_elementalinference.types.create_output_list
    import aws_sdk_elementalinference.types.delete_feed_request
    import aws_sdk_elementalinference.types.delete_feed_response
    import aws_sdk_elementalinference.types.disassociate_feed_request
    import aws_sdk_elementalinference.types.disassociate_feed_response
    import aws_sdk_elementalinference.types.feed_id
    import aws_sdk_elementalinference.types.feed_summary
    import aws_sdk_elementalinference.types.get_feed_request
    import aws_sdk_elementalinference.types.get_feed_response
    import aws_sdk_elementalinference.types.list_feeds_request
    import aws_sdk_elementalinference.types.list_feeds_response
    import aws_sdk_elementalinference.types.resource_name
    import aws_sdk_elementalinference.types.tag_map
    import aws_sdk_elementalinference.types.update_feed_request
    import aws_sdk_elementalinference.types.update_feed_response
    import aws_sdk_elementalinference.types.update_output_list
    from aws_sdk_elementalinference._services.async_elemental_inference import (
        AsyncElementalInferenceClient,
        AsyncElementalInferenceClientConfig,
    )
    from aws_sdk_elementalinference._services.elemental_inference import (
        ElementalInferenceClient,
        ElementalInferenceClientConfig,
    )


class FeedResource:
    def __init__(self, service: ElementalInferenceClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_elementalinference.types.resource_name.ResourceName",
        outputs: "aws_sdk_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        tags: Optional["aws_sdk_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_elementalinference.types.create_feed_response.CreateFeedResponse":
        """<p>Creates a feed. The feed is the target for the live media stream that is being sent by the calling application. An example of a calling application is AWS Elemental MediaLive. </p> <p>The key contents of the feed is an array of outputs. Each output represents an Elemental Inference feature. After you create the feed, you must associate a resource with the feed. At that point, you will have a useable feed: resource - feed - output or outputs. </p>

        Args:
            name: <p>A user-friendly name for this feed.</p>
            outputs: <p>An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed. </p>
            tags: <p>Optional tags. You can also add tags later, using TagResource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.create_feed_request.CreateFeedRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.create_feed_response.CreateFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.create_feed

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.create_feed.create_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.create_feed_request.CreateFeedRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["outputs"] = outputs
        if tags is not None:
            input["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.get_feed_response.GetFeedResponse":
        """<p>Retrieves information about the specified feed.</p>

        Args:
            id: <p>The ID of the feed to query.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.get_feed_request.GetFeedRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.get_feed_response.GetFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.get_feed

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.get_feed.get_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.get_feed_request.GetFeedRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        name: "aws_sdk_elementalinference.types.resource_name.ResourceName",
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        outputs: "aws_sdk_elementalinference.types.update_output_list.UpdateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.update_feed_response.UpdateFeedResponse":
        """<p>Updates the name and/or outputs in a feed. </p> <p>UpdateFeed is a PUT operation, which means that the payload that you specify completely overwrites the existing payload. </p> <p>This means that if you want to touch the array of outputs, you must pass in the full new list. So you must omit outputs you want to delete, and include outputs you want to add or modify. </p> <p>If you want to patch the array of outputs to make selective additions, use AssociateFeed. </p>

        Args:
            name: <p>Required. You can specify the existing name (to leave it unchanged) or a new name. </p>
            id: <p>The ID of the feed to update.</p>
            outputs: <p>Required. You can specify the existing array of outputs (to leave outputs unchanged) or you can specify a new array. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.update_feed_request.UpdateFeedRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.update_feed_response.UpdateFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.update_feed

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.update_feed.update_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.update_feed_request.UpdateFeedRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["id"] = id
        input["outputs"] = outputs

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.delete_feed_response.DeleteFeedResponse":
        """<p>Deletes the specified feed. You can delete the feed at any time. Elemental Inference doesn't block you from deleting a feed when the calling application is calling PutMedia or GetMetadata on that feed, although both these calls will start to fail. For more information about managing inactive feeds, see the Elemental Inference User Guide. </p>

        Args:
            id: <p>The ID of the feed.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.delete_feed_request.DeleteFeedRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.delete_feed_response.DeleteFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.delete_feed

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.delete_feed.delete_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.delete_feed_request.DeleteFeedRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_elementalinference.types.list_feeds_response.ListFeedsResponse":
        """<p>Displays a list of feeds that belong to this AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return per API request.</p> <p>For example, you submit a list request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page. </p> <p>Valid Range: Minimum value of 1. Maximum value of 1000.</p>
            next_token: <p>The token that identifies the batch of results that you want to see.</p> <p>For example, you submit a ListFeeds request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFeeds request a second time and specify the NextToken value. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.list_feeds_request.ListFeedsRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.list_feeds_response.ListFeedsResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.list_feeds

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.list_feeds.list_feeds(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.list_feeds_request.ListFeedsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_feed(
        self,
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "aws_sdk_elementalinference.types.associated_resource_name.AssociatedResourceName",
        outputs: "aws_sdk_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> (
        "aws_sdk_elementalinference.types.associate_feed_response.AssociateFeedResponse"
    ):
        """<p>Associates a resource with the feed. The resource provides the input that Elemental Inference needs in order to perform an Elemental Inference feature, such as cropping video. You always provide the resource by associating it with a feed. You can associate only one resource with each feed. With an association, a specific source media is claiming ownership of the feed. </p> <p>AssociateFeed is a PATCH operation, which means that you can include only parameters that you want to change. Parameters that you don't include will not be affected by the operation. </p> <p>Specifically:</p> <ul> <li> <p>You can add more outputs to the existing outputs. New outputs will be appended.</p> </li> <li> <p>You can't modify an existing output (for example to change its name). Instead, use UpdateFeed. </p> </li> <li> <p>You can't delete an existing output. Instead, use UpdateFeed.</p> </li> </ul> <p>Also note that you can't change the feed name with AssociateFeed. Instead, use UpdateFeed. </p>

        Args:
            id: <p>The ID of the feed.</p>
            associated_resource_name: <p>An identifier for the resource. This name must not resemble an ARN.</p> <p>The resource is the source media that the feed will process. The name you assign should help you to later identify the source media that belongs to the feed. In this way, you will know which source media to push to the feed (using PutMedia). </p>
            outputs: <p>An array of one or more outputs that you want to add to this feed now, to supplement any outputs that you specified when you created or updated the feed. </p>
            dry_run: <p>Set to true if you want to do a dry run of the associate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions, quota limits exceeded, conflicting outputs, and so on. If the dry run fails, the action returns a 4xx error code. After you've fixed the errors, resubmit the request. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.associate_feed_request.AssociateFeedRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.associate_feed_response.AssociateFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.associate_feed

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.associate_feed.associate_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.associate_feed_request.AssociateFeedRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["associated_resource_name"] = associated_resource_name
        input["outputs"] = outputs
        if dry_run is not None:
            input["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_feed(
        self,
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "aws_sdk_elementalinference.types.associated_resource_name.AssociatedResourceName",
        *,
        config_overrides: Optional[ElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "aws_sdk_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse":
        """<p>Releases the resource (the source media) that is associated with this feed. The outputs in the feed become DISABLED. </p>

        Args:
            id: <p>The ID of the feed where you want to release the resource.</p>
            associated_resource_name: <p>The name of the resource currently associated with the feed.</p>
            dry_run: <p>Set to true if you want to do a dry run of the disassociate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions. If the dry run fails, the action returns a 4xx error code. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest]",
        ) -> OperationResponse[
            "aws_sdk_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.disassociate_feed

            output, http_response = (
                aws_sdk_elementalinference._operations.elemental_inference.disassociate_feed.disassociate_feed(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["associated_resource_name"] = associated_resource_name
        if dry_run is not None:
            input["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncFeedResource:
    def __init__(self, service: AsyncElementalInferenceClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_elementalinference.types.resource_name.ResourceName",
        outputs: "aws_sdk_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        tags: Optional["aws_sdk_elementalinference.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_elementalinference.types.create_feed_response.CreateFeedResponse":
        """<p>Creates a feed. The feed is the target for the live media stream that is being sent by the calling application. An example of a calling application is AWS Elemental MediaLive. </p> <p>The key contents of the feed is an array of outputs. Each output represents an Elemental Inference feature. After you create the feed, you must associate a resource with the feed. At that point, you will have a useable feed: resource - feed - output or outputs. </p>

        Args:
            name: <p>A user-friendly name for this feed.</p>
            outputs: <p>An array of outputs for this feed. Each output represents a specific Elemental Inference feature. For example, there is one output type for the smart crop feature. You must specify at least one output, but you can later add outputs using AssociateFeed, or add, modify, and delete outputs using UpdateFeed. </p>
            tags: <p>Optional tags. You can also add tags later, using TagResource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.create_feed_request.CreateFeedRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.create_feed_response.CreateFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.create_feed

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.create_feed.async_create_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.create_feed_request.CreateFeedRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["outputs"] = outputs
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.get_feed_response.GetFeedResponse":
        """<p>Retrieves information about the specified feed.</p>

        Args:
            id: <p>The ID of the feed to query.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.get_feed_request.GetFeedRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.get_feed_response.GetFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.get_feed

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.get_feed.async_get_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.get_feed_request.GetFeedRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        name: "aws_sdk_elementalinference.types.resource_name.ResourceName",
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        outputs: "aws_sdk_elementalinference.types.update_output_list.UpdateOutputList",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.update_feed_response.UpdateFeedResponse":
        """<p>Updates the name and/or outputs in a feed. </p> <p>UpdateFeed is a PUT operation, which means that the payload that you specify completely overwrites the existing payload. </p> <p>This means that if you want to touch the array of outputs, you must pass in the full new list. So you must omit outputs you want to delete, and include outputs you want to add or modify. </p> <p>If you want to patch the array of outputs to make selective additions, use AssociateFeed. </p>

        Args:
            name: <p>Required. You can specify the existing name (to leave it unchanged) or a new name. </p>
            id: <p>The ID of the feed to update.</p>
            outputs: <p>Required. You can specify the existing array of outputs (to leave outputs unchanged) or you can specify a new array. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.update_feed_request.UpdateFeedRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.update_feed_response.UpdateFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.update_feed

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.update_feed.async_update_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.update_feed_request.UpdateFeedRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["id"] = id
        input["outputs"] = outputs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
    ) -> "aws_sdk_elementalinference.types.delete_feed_response.DeleteFeedResponse":
        """<p>Deletes the specified feed. You can delete the feed at any time. Elemental Inference doesn't block you from deleting a feed when the calling application is calling PutMedia or GetMetadata on that feed, although both these calls will start to fail. For more information about managing inactive feeds, see the Elemental Inference User Guide. </p>

        Args:
            id: <p>The ID of the feed.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.delete_feed_request.DeleteFeedRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.delete_feed_response.DeleteFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.delete_feed

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.delete_feed.async_delete_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.delete_feed_request.DeleteFeedRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_elementalinference.types.list_feeds_response.ListFeedsResponse":
        """<p>Displays a list of feeds that belong to this AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return per API request.</p> <p>For example, you submit a list request with MaxResults set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the MaxResults value. If MaxResults is not included in the request, the service defaults to pagination with a maximum of 10 results per page. </p> <p>Valid Range: Minimum value of 1. Maximum value of 1000.</p>
            next_token: <p>The token that identifies the batch of results that you want to see.</p> <p>For example, you submit a ListFeeds request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a NextToken value. To see the next batch of results, you can submit the ListFeeds request a second time and specify the NextToken value. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.list_feeds_request.ListFeedsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.list_feeds_response.ListFeedsResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.list_feeds

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.list_feeds.async_list_feeds(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.list_feeds_request.ListFeedsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_feed(
        self,
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "aws_sdk_elementalinference.types.associated_resource_name.AssociatedResourceName",
        outputs: "aws_sdk_elementalinference.types.create_output_list.CreateOutputList",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> (
        "aws_sdk_elementalinference.types.associate_feed_response.AssociateFeedResponse"
    ):
        """<p>Associates a resource with the feed. The resource provides the input that Elemental Inference needs in order to perform an Elemental Inference feature, such as cropping video. You always provide the resource by associating it with a feed. You can associate only one resource with each feed. With an association, a specific source media is claiming ownership of the feed. </p> <p>AssociateFeed is a PATCH operation, which means that you can include only parameters that you want to change. Parameters that you don't include will not be affected by the operation. </p> <p>Specifically:</p> <ul> <li> <p>You can add more outputs to the existing outputs. New outputs will be appended.</p> </li> <li> <p>You can't modify an existing output (for example to change its name). Instead, use UpdateFeed. </p> </li> <li> <p>You can't delete an existing output. Instead, use UpdateFeed.</p> </li> </ul> <p>Also note that you can't change the feed name with AssociateFeed. Instead, use UpdateFeed. </p>

        Args:
            id: <p>The ID of the feed.</p>
            associated_resource_name: <p>An identifier for the resource. This name must not resemble an ARN.</p> <p>The resource is the source media that the feed will process. The name you assign should help you to later identify the source media that belongs to the feed. In this way, you will know which source media to push to the feed (using PutMedia). </p>
            outputs: <p>An array of one or more outputs that you want to add to this feed now, to supplement any outputs that you specified when you created or updated the feed. </p>
            dry_run: <p>Set to true if you want to do a dry run of the associate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions, quota limits exceeded, conflicting outputs, and so on. If the dry run fails, the action returns a 4xx error code. After you've fixed the errors, resubmit the request. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.associate_feed_request.AssociateFeedRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.associate_feed_response.AssociateFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.associate_feed

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.associate_feed.async_associate_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.associate_feed_request.AssociateFeedRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["associated_resource_name"] = associated_resource_name
        input["outputs"] = outputs
        if dry_run is not None:
            input["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_feed(
        self,
        id: "aws_sdk_elementalinference.types.feed_id.FeedId",
        associated_resource_name: "aws_sdk_elementalinference.types.associated_resource_name.AssociatedResourceName",
        *,
        config_overrides: Optional[AsyncElementalInferenceClientConfig] = None,
        dry_run: Optional[bool] = None,
    ) -> "aws_sdk_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse":
        """<p>Releases the resource (the source media) that is associated with this feed. The outputs in the feed become DISABLED. </p>

        Args:
            id: <p>The ID of the feed where you want to release the resource.</p>
            associated_resource_name: <p>The name of the resource currently associated with the feed.</p>
            dry_run: <p>Set to true if you want to do a dry run of the disassociate action.</p> <p>Elemental Inference will validate that the real request would succeed without actually making any changes. A dry run catches errors such as missing IAM permissions. If the dry run fails, the action returns a 4xx error code. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_elementalinference.types.disassociate_feed_response.DisassociateFeedResponse"
        ]:
            import aws_sdk_elementalinference._operations.elemental_inference.disassociate_feed

            (
                output,
                http_response,
            ) = await aws_sdk_elementalinference._operations.elemental_inference.disassociate_feed.async_disassociate_feed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_elementalinference.types.disassociate_feed_request.DisassociateFeedRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        input["associated_resource_name"] = associated_resource_name
        if dry_run is not None:
            input["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
