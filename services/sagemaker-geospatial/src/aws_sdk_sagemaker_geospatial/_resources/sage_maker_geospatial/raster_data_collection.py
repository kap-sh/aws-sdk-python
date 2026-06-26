from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_sagemaker_geospatial._auth._signers
import aws_sdk_sagemaker_geospatial._auth._sigv4
from aws_sdk_sagemaker_geospatial._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.data_collection_arn
    import aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_input
    import aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_output
    import aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_input
    import aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_output
    import aws_sdk_sagemaker_geospatial.types.next_token
    import aws_sdk_sagemaker_geospatial.types.raster_data_collection_metadata
    import aws_sdk_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input
    import aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_input
    import aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_output
    from aws_sdk_sagemaker_geospatial._services.async_sage_maker_geospatial import (
        AsyncSageMakerGeospatialClient,
        AsyncSageMakerGeospatialClientConfig,
    )
    from aws_sdk_sagemaker_geospatial._services.sage_maker_geospatial import (
        SageMakerGeospatialClient,
        SageMakerGeospatialClientConfig,
    )


class RasterDataCollection:
    def __init__(self, service: SageMakerGeospatialClient) -> None:
        self._service = service

    def read(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput":
        """<p>Use this operation to get details of a specific raster data collection.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>

        Raises:
            aws_sdk_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection.get_raster_data_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput":
        """<p>Use this operation to get raster data collections.</p>

        Args:
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>

        Raises:
            aws_sdk_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections.list_raster_data_collections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_raster_data_collection(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        raster_data_collection_query: "aws_sdk_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input.RasterDataCollectionQueryWithBandFilterInput",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput":
        r"""<p>Allows you run image query on a specific raster data collection to get a list of the satellite imagery matching the selected filters.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>
            raster_data_collection_query: <p>RasterDataCollectionQuery consisting of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterest.html\">AreaOfInterest(AOI)</a>, <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_PropertyFilter.html\">PropertyFilters</a> and <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TimeRangeFilterInput.html\">TimeRangeFilterInput</a> used in <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html\">SearchRasterDataCollection</a>.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>

        Raises:
            aws_sdk_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput]",
        ) -> OperationResponse[
            "aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection

            output, http_response = (
                aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection.search_raster_data_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["raster_data_collection_query"] = raster_data_collection_query
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRasterDataCollection:
    def __init__(self, service: AsyncSageMakerGeospatialClient) -> None:
        self._service = service

    async def read(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput":
        """<p>Use this operation to get details of a specific raster data collection.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>

        Raises:
            aws_sdk_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection.async_get_raster_data_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput":
        """<p>Use this operation to get raster data collections.</p>

        Args:
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>

        Raises:
            aws_sdk_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections.async_list_raster_data_collections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput = {}  # type: ignore[typeddict-item]
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def search_raster_data_collection(
        self,
        arn: "aws_sdk_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        raster_data_collection_query: "aws_sdk_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input.RasterDataCollectionQueryWithBandFilterInput",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "aws_sdk_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput":
        r"""<p>Allows you run image query on a specific raster data collection to get a list of the satellite imagery matching the selected filters.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>
            raster_data_collection_query: <p>RasterDataCollectionQuery consisting of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterest.html\">AreaOfInterest(AOI)</a>, <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_PropertyFilter.html\">PropertyFilters</a> and <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TimeRangeFilterInput.html\">TimeRangeFilterInput</a> used in <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html\">SearchRasterDataCollection</a>.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>

        Raises:
            aws_sdk_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            aws_sdk_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            aws_sdk_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            aws_sdk_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            aws_sdk_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput"
        ]:
            import aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection

            (
                output,
                http_response,
            ) = await aws_sdk_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection.async_search_raster_data_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["raster_data_collection_query"] = raster_data_collection_query
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
