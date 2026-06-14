from typing import TYPE_CHECKING, Optional

from aws_sdk_opensearchserverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.create_vpc_endpoint_request
    import aws_sdk_opensearchserverless.types.create_vpc_endpoint_response
    import aws_sdk_opensearchserverless.types.delete_vpc_endpoint_request
    import aws_sdk_opensearchserverless.types.delete_vpc_endpoint_response
    import aws_sdk_opensearchserverless.types.list_vpc_endpoints_request
    import aws_sdk_opensearchserverless.types.list_vpc_endpoints_response
    import aws_sdk_opensearchserverless.types.security_group_ids
    import aws_sdk_opensearchserverless.types.subnet_ids
    import aws_sdk_opensearchserverless.types.vpc_endpoint_filters
    import aws_sdk_opensearchserverless.types.vpc_endpoint_id
    import aws_sdk_opensearchserverless.types.vpc_endpoint_name
    import aws_sdk_opensearchserverless.types.vpc_id
    from aws_sdk_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from aws_sdk_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class VpcEndpoint:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_opensearchserverless.types.vpc_endpoint_name.VpcEndpointName",
        vpc_id: "aws_sdk_opensearchserverless.types.vpc_id.VpcId",
        subnet_ids: "aws_sdk_opensearchserverless.types.subnet_ids.SubnetIds",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        security_group_ids: Optional[
            "aws_sdk_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse":
        """<p>Creates an OpenSearch Serverless-managed interface VPC endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            name: <p>The name of the interface endpoint.</p>
            vpc_id: <p>The ID of the VPC from which you'll access OpenSearch Serverless.</p>
            subnet_ids: <p>The ID of one or more subnets from which you'll access OpenSearch Serverless.</p>
            security_group_ids: <p>The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint.create_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["vpc_id"] = vpc_id
        input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id: "aws_sdk_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse":
        """<p>Deletes an OpenSearch Serverless-managed interface endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            id: <p>The VPC endpoint identifier.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint.delete_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        vpc_endpoint_filters: Optional[
            "aws_sdk_opensearchserverless.types.vpc_endpoint_filters.VpcEndpointFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse":
        """<p>Returns the OpenSearch Serverless-managed interface VPC endpoints associated with the current account. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            vpc_endpoint_filters: <p>Filter the results according to the current status of the VPC endpoint. Possible statuses are <code>CREATING</code>, <code>DELETING</code>, <code>UPDATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>
            next_token: <p>If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page. </p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints.list_vpc_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
        if vpc_endpoint_filters is not None:
            input_["vpc_endpoint_filters"] = vpc_endpoint_filters
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


class AsyncVpcEndpoint:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_opensearchserverless.types.vpc_endpoint_name.VpcEndpointName",
        vpc_id: "aws_sdk_opensearchserverless.types.vpc_id.VpcId",
        subnet_ids: "aws_sdk_opensearchserverless.types.subnet_ids.SubnetIds",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        security_group_ids: Optional[
            "aws_sdk_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse":
        """<p>Creates an OpenSearch Serverless-managed interface VPC endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            name: <p>The name of the interface endpoint.</p>
            vpc_id: <p>The ID of the VPC from which you'll access OpenSearch Serverless.</p>
            subnet_ids: <p>The ID of one or more subnets from which you'll access OpenSearch Serverless.</p>
            security_group_ids: <p>The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint.async_create_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["vpc_id"] = vpc_id
        input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id: "aws_sdk_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse":
        """<p>Deletes an OpenSearch Serverless-managed interface endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            id: <p>The VPC endpoint identifier.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint.async_delete_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["id"] = id
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        vpc_endpoint_filters: Optional[
            "aws_sdk_opensearchserverless.types.vpc_endpoint_filters.VpcEndpointFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse":
        """<p>Returns the OpenSearch Serverless-managed interface VPC endpoints associated with the current account. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html\">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            vpc_endpoint_filters: <p>Filter the results according to the current status of the VPC endpoint. Possible statuses are <code>CREATING</code>, <code>DELETING</code>, <code>UPDATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>
            next_token: <p>If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page. </p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints.async_list_vpc_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest = {}  # type: ignore[typeddict-item]
        if vpc_endpoint_filters is not None:
            input_["vpc_endpoint_filters"] = vpc_endpoint_filters
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
