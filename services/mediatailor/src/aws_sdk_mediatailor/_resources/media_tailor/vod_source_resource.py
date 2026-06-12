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
    import aws_sdk_mediatailor.types.create_vod_source_request
    import aws_sdk_mediatailor.types.create_vod_source_response
    import aws_sdk_mediatailor.types.delete_vod_source_request
    import aws_sdk_mediatailor.types.delete_vod_source_response
    import aws_sdk_mediatailor.types.describe_vod_source_request
    import aws_sdk_mediatailor.types.describe_vod_source_response
    import aws_sdk_mediatailor.types.http_package_configurations
    import aws_sdk_mediatailor.types.list_vod_sources_request
    import aws_sdk_mediatailor.types.list_vod_sources_response
    import aws_sdk_mediatailor.types.max_results
    import aws_sdk_mediatailor.types.update_vod_source_request
    import aws_sdk_mediatailor.types.update_vod_source_response
    import aws_sdk_mediatailor.types.vod_source
    from aws_sdk_mediatailor._services.async_media_tailor import (
        AsyncMediaTailorClient,
        AsyncMediaTailorClientConfig,
    )
    from aws_sdk_mediatailor._services.media_tailor import (
        MediaTailorClient,
        MediaTailorClientConfig,
    )


class VodSourceResource:
    def __init__(self, service: MediaTailorClient) -> None:
        self._service = service

    def put(
        self,
        http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        vod_source_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        tags: Optional[
            "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "aws_sdk_mediatailor.types.create_vod_source_response.CreateVodSourceResponse":
        """<p>The VOD source configuration parameters.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configuration parameters for this VOD source.</p>
            source_location_name: <p>The name of the source location for this VOD source.</p>
            tags: <p>The tags to assign to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            vod_source_name: <p>The name associated with the VOD source.&gt;</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.create_vod_source_request.CreateVodSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.create_vod_source_response.CreateVodSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.create_vod_source

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.create_vod_source.create_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.create_vod_source_request.CreateVodSourceRequest = {}  # type: ignore[typeddict-item]
        input["http_package_configurations"] = http_package_configurations
        input["source_location_name"] = source_location_name
        if tags is not None:
            input["tags"] = tags
        input["vod_source_name"] = vod_source_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        vod_source_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse":
        """<p>Provides details about a specific video on demand (VOD) source in a specific source location.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD Source.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.describe_vod_source

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.describe_vod_source.describe_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest = {}  # type: ignore[typeddict-item]
        input["source_location_name"] = source_location_name
        input["vod_source_name"] = vod_source_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        vod_source_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse":
        """<p>Updates a VOD source's configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configurations for the VOD source on this account.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.update_vod_source

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.update_vod_source.update_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest = {}  # type: ignore[typeddict-item]
        input["http_package_configurations"] = http_package_configurations
        input["source_location_name"] = source_location_name
        input["vod_source_name"] = vod_source_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        vod_source_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse":
        """<p>The video on demand (VOD) source to delete.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.delete_vod_source

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.delete_vod_source.delete_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest = {}  # type: ignore[typeddict-item]
        input["source_location_name"] = source_location_name
        input["vod_source_name"] = vod_source_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
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
    ) -> "aws_sdk_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse":
        """<p>Lists the VOD sources contained in a source location. A source represents a piece of content.</p>

        Args:
            max_results: <p> The maximum number of VOD sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> VOD sources, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListVodSources</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.list_vod_sources

            output, http_response = (
                aws_sdk_mediatailor._operations.media_tailor.list_vod_sources.list_vod_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["source_location_name"] = source_location_name

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncVodSourceResource:
    def __init__(self, service: AsyncMediaTailorClient) -> None:
        self._service = service

    async def put(
        self,
        http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        vod_source_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        tags: Optional[
            "aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "aws_sdk_mediatailor.types.create_vod_source_response.CreateVodSourceResponse":
        """<p>The VOD source configuration parameters.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configuration parameters for this VOD source.</p>
            source_location_name: <p>The name of the source location for this VOD source.</p>
            tags: <p>The tags to assign to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            vod_source_name: <p>The name associated with the VOD source.&gt;</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.create_vod_source_request.CreateVodSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.create_vod_source_response.CreateVodSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.create_vod_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.create_vod_source.async_create_vod_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.create_vod_source_request.CreateVodSourceRequest = {}  # type: ignore[typeddict-item]
        input["http_package_configurations"] = http_package_configurations
        input["source_location_name"] = source_location_name
        if tags is not None:
            input["tags"] = tags
        input["vod_source_name"] = vod_source_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        vod_source_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse":
        """<p>Provides details about a specific video on demand (VOD) source in a specific source location.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD Source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.describe_vod_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.describe_vod_source.async_describe_vod_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest = {}  # type: ignore[typeddict-item]
        input["source_location_name"] = source_location_name
        input["vod_source_name"] = vod_source_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        http_package_configurations: "aws_sdk_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        vod_source_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse":
        """<p>Updates a VOD source's configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configurations for the VOD source on this account.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.update_vod_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.update_vod_source.async_update_vod_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest = {}  # type: ignore[typeddict-item]
        input["http_package_configurations"] = http_package_configurations
        input["source_location_name"] = source_location_name
        input["vod_source_name"] = vod_source_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        source_location_name: "aws_sdk_mediatailor.types.__string.__string",
        vod_source_name: "aws_sdk_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "aws_sdk_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse":
        """<p>The video on demand (VOD) source to delete.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.delete_vod_source

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.delete_vod_source.async_delete_vod_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest = {}  # type: ignore[typeddict-item]
        input["source_location_name"] = source_location_name
        input["vod_source_name"] = vod_source_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
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
    ) -> "aws_sdk_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse":
        """<p>Lists the VOD sources contained in a source location. A source represents a piece of content.</p>

        Args:
            max_results: <p> The maximum number of VOD sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> VOD sources, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListVodSources</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse"
        ]:
            import aws_sdk_mediatailor._operations.media_tailor.list_vod_sources

            (
                output,
                http_response,
            ) = await aws_sdk_mediatailor._operations.media_tailor.list_vod_sources.async_list_vod_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["source_location_name"] = source_location_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
