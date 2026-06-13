from typing import TYPE_CHECKING, Optional

import aws_sdk_mediaconnect._auth._signers
import aws_sdk_mediaconnect._auth._sigv4
from aws_sdk_mediaconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.describe_offering_request
    import aws_sdk_mediaconnect.types.describe_offering_response
    import aws_sdk_mediaconnect.types.list_offerings_request
    import aws_sdk_mediaconnect.types.list_offerings_response
    import aws_sdk_mediaconnect.types.max_results
    import aws_sdk_mediaconnect.types.offering
    import aws_sdk_mediaconnect.types.offering_arn
    from aws_sdk_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from aws_sdk_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class OfferingResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def read(
        self,
        offering_arn: "aws_sdk_mediaconnect.types.offering_arn.OfferingArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> (
        "aws_sdk_mediaconnect.types.describe_offering_response.DescribeOfferingResponse"
    ):
        """<p> Displays the details of an offering. The response includes the offering description, duration, outbound bandwidth, price, and Amazon Resource Name (ARN).</p>

        Args:
            offering_arn: <p> The ARN of the offering.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.describe_offering_request.DescribeOfferingRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.describe_offering_response.DescribeOfferingResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_offering

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.describe_offering.describe_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_offering_request.DescribeOfferingRequest = {}  # type: ignore[typeddict-item]
        input["offering_arn"] = offering_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.list_offerings_response.ListOfferingsResponse":
        """<p> Displays a list of all offerings that are available to this account in the current Amazon Web Services Region. If you have an active reservation (which means you've purchased an offering that has already started and hasn't expired yet), your account isn't eligible for other offerings.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListOfferings</code> request a second time and specify the <code>NextToken</code> value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.list_offerings_request.ListOfferingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.list_offerings_response.ListOfferingsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_offerings

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.list_offerings.list_offerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.list_offerings_request.ListOfferingsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncOfferingResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def read(
        self,
        offering_arn: "aws_sdk_mediaconnect.types.offering_arn.OfferingArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> (
        "aws_sdk_mediaconnect.types.describe_offering_response.DescribeOfferingResponse"
    ):
        """<p> Displays the details of an offering. The response includes the offering description, duration, outbound bandwidth, price, and Amazon Resource Name (ARN).</p>

        Args:
            offering_arn: <p> The ARN of the offering.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.describe_offering_request.DescribeOfferingRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.describe_offering_response.DescribeOfferingResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_offering

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.describe_offering.async_describe_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_offering_request.DescribeOfferingRequest = {}  # type: ignore[typeddict-item]
        input["offering_arn"] = offering_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        max_results: Optional[
            "aws_sdk_mediaconnect.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_mediaconnect.types.list_offerings_response.ListOfferingsResponse":
        """<p> Displays a list of all offerings that are available to this account in the current Amazon Web Services Region. If you have an active reservation (which means you've purchased an offering that has already started and hasn't expired yet), your account isn't eligible for other offerings.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListOfferings</code> request a second time and specify the <code>NextToken</code> value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_offerings_request.ListOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_offerings_response.ListOfferingsResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_offerings

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_offerings.async_list_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.list_offerings_request.ListOfferingsRequest = {}  # type: ignore[typeddict-item]
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
