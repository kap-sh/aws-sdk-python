from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_mediatailor._auth._signers
import aws_sdk_mediatailor._auth._sigv4
from aws_sdk_mediatailor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.__string
    import aws_sdk_mediatailor.types.create_live_source_request
    import aws_sdk_mediatailor.types.create_live_source_response
    import aws_sdk_mediatailor.types.delete_live_source_request
    import aws_sdk_mediatailor.types.delete_live_source_response
    import aws_sdk_mediatailor.types.describe_live_source_request
    import aws_sdk_mediatailor.types.describe_live_source_response
    import aws_sdk_mediatailor.types.http_package_configurations
    import aws_sdk_mediatailor.types.list_live_sources_request
    import aws_sdk_mediatailor.types.list_live_sources_response
    import aws_sdk_mediatailor.types.live_source
    import aws_sdk_mediatailor.types.max_results
    import aws_sdk_mediatailor.types.update_live_source_request
    import aws_sdk_mediatailor.types.update_live_source_response
    from aws_sdk_mediatailor._services.async_media_tailor import (
        AsyncMediaTailorClient,
        AsyncMediaTailorClientConfig,
    )
    from aws_sdk_mediatailor._services.media_tailor import (
        MediaTailorClient,
        MediaTailorClientConfig,
    )


class LiveSourceResource:
    def __init__(self, service: MediaTailorClient) -> None:
        self._service = service

    def put(
        self,
        http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        live_source_name: "aws_sdk_mediatailor.types.__string.__string",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        tags: Optional[
            "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> (
        "aws_sdk_mediatailor.types.create_live_source_response.CreateLiveSourceResponse"
    ):
        r"""<p>The live source configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configuration parameters for this live source.</p>
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location.</p>
            tags: <p>The tags to assign to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.create_live_source_request.CreateLiveSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.create_live_source_response.CreateLiveSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.create_live_source

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.create_live_source.create_live_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.create_live_source_request.CreateLiveSourceRequest = {}  # type: ignore[typeddict-item]
        input_["http_package_configurations"] = http_package_configurations
        input_["live_source_name"] = live_source_name
        input_["source_location_name"] = source_location_name
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
        live_source_name: "aws_sdk_mediatailor.types.__string.__string",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.describe_live_source_response.DescribeLiveSourceResponse":
        """<p>The live source to describe.</p>

        Args:
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location associated with this Live Source.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.describe_live_source_request.DescribeLiveSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.describe_live_source_response.DescribeLiveSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.describe_live_source

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.describe_live_source.describe_live_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.describe_live_source_request.DescribeLiveSourceRequest = {}  # type: ignore[typeddict-item]
        input_["live_source_name"] = live_source_name
        input_["source_location_name"] = source_location_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        live_source_name: "aws_sdk_mediatailor.types.__string.__string",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> (
        "aws_sdk_mediatailor.types.update_live_source_response.UpdateLiveSourceResponse"
    ):
        """<p>Updates a live source's configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configurations for the live source on this account.</p>
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location associated with this Live Source.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.update_live_source_request.UpdateLiveSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.update_live_source_response.UpdateLiveSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.update_live_source

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.update_live_source.update_live_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.update_live_source_request.UpdateLiveSourceRequest = {}  # type: ignore[typeddict-item]
        input_["http_package_configurations"] = http_package_configurations
        input_["live_source_name"] = live_source_name
        input_["source_location_name"] = source_location_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        live_source_name: "aws_sdk_mediatailor.types.__string.__string",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> (
        "aws_sdk_mediatailor.types.delete_live_source_response.DeleteLiveSourceResponse"
    ):
        """<p>The live source to delete.</p>

        Args:
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location associated with this Live Source.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.delete_live_source_request.DeleteLiveSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.delete_live_source_response.DeleteLiveSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.delete_live_source

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.delete_live_source.delete_live_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.delete_live_source_request.DeleteLiveSourceRequest = {}  # type: ignore[typeddict-item]
        input_["live_source_name"] = live_source_name
        input_["source_location_name"] = source_location_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediatailor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediatailor.types.__string.__string"] = None,
    ) -> "aws_sdk_mediatailor.types.list_live_sources_response.ListLiveSourcesResponse":
        """<p>Lists the live sources contained in a source location. A source represents a piece of content.</p>

        Args:
            max_results: <p>The maximum number of live sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> live sources, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListLiveSources</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            source_location_name: <p>The name of the source location associated with this Live Sources list.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.list_live_sources_request.ListLiveSourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.list_live_sources_response.ListLiveSourcesResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.list_live_sources

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.list_live_sources.list_live_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.list_live_sources_request.ListLiveSourcesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["source_location_name"] = source_location_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncLiveSourceResource:
    def __init__(self, service: AsyncMediaTailorClient) -> None:
        self._service = service

    async def put(
        self,
        http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        live_source_name: "aws_sdk_mediatailor.types.__string.__string",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        tags: Optional[
            "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> (
        "aws_sdk_mediatailor.types.create_live_source_response.CreateLiveSourceResponse"
    ):
        r"""<p>The live source configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configuration parameters for this live source.</p>
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location.</p>
            tags: <p>The tags to assign to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.create_live_source_request.CreateLiveSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.create_live_source_response.CreateLiveSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.create_live_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.create_live_source.async_create_live_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.create_live_source_request.CreateLiveSourceRequest = {}  # type: ignore[typeddict-item]
        input_["http_package_configurations"] = http_package_configurations
        input_["live_source_name"] = live_source_name
        input_["source_location_name"] = source_location_name
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
        live_source_name: "aws_sdk_mediatailor.types.__string.__string",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.describe_live_source_response.DescribeLiveSourceResponse":
        """<p>The live source to describe.</p>

        Args:
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location associated with this Live Source.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.describe_live_source_request.DescribeLiveSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.describe_live_source_response.DescribeLiveSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.describe_live_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.describe_live_source.async_describe_live_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.describe_live_source_request.DescribeLiveSourceRequest = {}  # type: ignore[typeddict-item]
        input_["live_source_name"] = live_source_name
        input_["source_location_name"] = source_location_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        live_source_name: "aws_sdk_mediatailor.types.__string.__string",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> (
        "aws_sdk_mediatailor.types.update_live_source_response.UpdateLiveSourceResponse"
    ):
        """<p>Updates a live source's configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configurations for the live source on this account.</p>
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location associated with this Live Source.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.update_live_source_request.UpdateLiveSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.update_live_source_response.UpdateLiveSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.update_live_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.update_live_source.async_update_live_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.update_live_source_request.UpdateLiveSourceRequest = {}  # type: ignore[typeddict-item]
        input_["http_package_configurations"] = http_package_configurations
        input_["live_source_name"] = live_source_name
        input_["source_location_name"] = source_location_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        live_source_name: "aws_sdk_mediatailor.types.__string.__string",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> (
        "aws_sdk_mediatailor.types.delete_live_source_response.DeleteLiveSourceResponse"
    ):
        """<p>The live source to delete.</p>

        Args:
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location associated with this Live Source.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.delete_live_source_request.DeleteLiveSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.delete_live_source_response.DeleteLiveSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.delete_live_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.delete_live_source.async_delete_live_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.delete_live_source_request.DeleteLiveSourceRequest = {}  # type: ignore[typeddict-item]
        input_["live_source_name"] = live_source_name
        input_["source_location_name"] = source_location_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediatailor.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_mediatailor.types.__string.__string"] = None,
    ) -> "aws_sdk_mediatailor.types.list_live_sources_response.ListLiveSourcesResponse":
        """<p>Lists the live sources contained in a source location. A source represents a piece of content.</p>

        Args:
            max_results: <p>The maximum number of live sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> live sources, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListLiveSources</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            source_location_name: <p>The name of the source location associated with this Live Sources list.</p>

        Raises:
            aws_sdk_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.list_live_sources_request.ListLiveSourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.list_live_sources_response.ListLiveSourcesResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.list_live_sources

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.list_live_sources.async_list_live_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_mediatailor.types.list_live_sources_request.ListLiveSourcesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["source_location_name"] = source_location_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
