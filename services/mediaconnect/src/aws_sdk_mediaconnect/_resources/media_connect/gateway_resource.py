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
    import aws_sdk_mediaconnect.types.__list_of_gateway_network
    import aws_sdk_mediaconnect.types.__list_of_string
    import aws_sdk_mediaconnect.types.create_gateway_request
    import aws_sdk_mediaconnect.types.create_gateway_response
    import aws_sdk_mediaconnect.types.delete_gateway_request
    import aws_sdk_mediaconnect.types.delete_gateway_response
    import aws_sdk_mediaconnect.types.describe_gateway_request
    import aws_sdk_mediaconnect.types.describe_gateway_response
    import aws_sdk_mediaconnect.types.gateway_arn
    import aws_sdk_mediaconnect.types.list_gateways_request
    import aws_sdk_mediaconnect.types.list_gateways_response
    import aws_sdk_mediaconnect.types.listed_gateway
    import aws_sdk_mediaconnect.types.max_results
    from aws_sdk_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from aws_sdk_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class GatewayResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        egress_cidr_blocks: "aws_sdk_mediaconnect.types.__list_of_string.__listOfString",
        name: str,
        networks: "aws_sdk_mediaconnect.types.__list_of_gateway_network.__listOfGatewayNetwork",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.create_gateway_response.CreateGatewayResponse":
        """<p> Creates a new gateway. The request must include at least one network (up to four).</p>

        Args:
            egress_cidr_blocks: <p> The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>
            name: <p> The name of the gateway. This name can not be modified after the gateway is created.</p>
            networks: <p> The list of networks that you want to add to the gateway.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.create_gateway_request.CreateGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_gateway

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.create_gateway.create_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.create_gateway_request.CreateGatewayRequest = {}  # type: ignore[typeddict-item]
        input["egress_cidr_blocks"] = egress_cidr_blocks
        input["name"] = name
        input["networks"] = networks

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        gateway_arn: "aws_sdk_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse":
        """<p> Displays the details of a gateway. The response includes the gateway Amazon Resource Name (ARN), name, and CIDR blocks, as well as details about the networks.</p>

        Args:
            gateway_arn: <p> The ARN of the gateway that you want to describe.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_gateway

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.describe_gateway.describe_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        gateway_arn: "aws_sdk_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse":
        """<p> Deletes a gateway. Before you can delete a gateway, you must deregister its instances and delete its bridges.</p>

        Args:
            gateway_arn: <p> The Amazon Resource Name (ARN) of the gateway that you want to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_gateway

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

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
    ) -> "aws_sdk_mediaconnect.types.list_gateways_response.ListGatewaysResponse":
        """<p> Displays a list of gateways that are associated with this account. This request returns a paginated result.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListGateways</code> request a second time and specify the <code>NextToken</code> value.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_mediaconnect.types.list_gateways_request.ListGatewaysRequest]",
        ) -> OperationResponse[
            "aws_sdk_mediaconnect.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_gateways

            output, http_response = (
                aws_sdk_mediaconnect._operations.media_connect.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.list_gateways_request.ListGatewaysRequest = {}  # type: ignore[typeddict-item]
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


class AsyncGatewayResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        egress_cidr_blocks: "aws_sdk_mediaconnect.types.__list_of_string.__listOfString",
        name: str,
        networks: "aws_sdk_mediaconnect.types.__list_of_gateway_network.__listOfGatewayNetwork",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.create_gateway_response.CreateGatewayResponse":
        """<p> Creates a new gateway. The request must include at least one network (up to four).</p>

        Args:
            egress_cidr_blocks: <p> The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>
            name: <p> The name of the gateway. This name can not be modified after the gateway is created.</p>
            networks: <p> The list of networks that you want to add to the gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.create_gateway_request.CreateGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.create_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.create_gateway.async_create_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.create_gateway_request.CreateGatewayRequest = {}  # type: ignore[typeddict-item]
        input["egress_cidr_blocks"] = egress_cidr_blocks
        input["name"] = name
        input["networks"] = networks

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        gateway_arn: "aws_sdk_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse":
        """<p> Displays the details of a gateway. The response includes the gateway Amazon Resource Name (ARN), name, and CIDR blocks, as well as details about the networks.</p>

        Args:
            gateway_arn: <p> The ARN of the gateway that you want to describe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.describe_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.describe_gateway.async_describe_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        gateway_arn: "aws_sdk_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "aws_sdk_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse":
        """<p> Deletes a gateway. Before you can delete a gateway, you must deregister its instances and delete its bridges.</p>

        Args:
            gateway_arn: <p> The Amazon Resource Name (ARN) of the gateway that you want to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.delete_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.delete_gateway.async_delete_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest = {}  # type: ignore[typeddict-item]
        input["gateway_arn"] = gateway_arn

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
    ) -> "aws_sdk_mediaconnect.types.list_gateways_response.ListGatewaysResponse":
        """<p> Displays a list of gateways that are associated with this account. This request returns a paginated result.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListGateways</code> request a second time and specify the <code>NextToken</code> value.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_mediaconnect.types.list_gateways_request.ListGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_mediaconnect.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import aws_sdk_mediaconnect._operations.media_connect.list_gateways

            (
                output,
                http_response,
            ) = await aws_sdk_mediaconnect._operations.media_connect.list_gateways.async_list_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_mediaconnect.types.list_gateways_request.ListGatewaysRequest = {}  # type: ignore[typeddict-item]
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
