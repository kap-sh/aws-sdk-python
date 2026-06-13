from typing import TYPE_CHECKING, Optional

import aws_sdk_neptune_graph._auth._signers
import aws_sdk_neptune_graph._auth._sigv4
from aws_sdk_neptune_graph._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.create_private_graph_endpoint_input
    import aws_sdk_neptune_graph.types.create_private_graph_endpoint_output
    import aws_sdk_neptune_graph.types.delete_private_graph_endpoint_input
    import aws_sdk_neptune_graph.types.delete_private_graph_endpoint_output
    import aws_sdk_neptune_graph.types.get_private_graph_endpoint_input
    import aws_sdk_neptune_graph.types.get_private_graph_endpoint_output
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.list_private_graph_endpoints_input
    import aws_sdk_neptune_graph.types.list_private_graph_endpoints_output
    import aws_sdk_neptune_graph.types.max_results
    import aws_sdk_neptune_graph.types.pagination_token
    import aws_sdk_neptune_graph.types.private_graph_endpoint_summary
    import aws_sdk_neptune_graph.types.security_group_ids
    import aws_sdk_neptune_graph.types.subnet_ids
    import aws_sdk_neptune_graph.types.vpc_id
    from aws_sdk_neptune_graph._services.async_neptune_graph import (
        AsyncNeptuneGraphClient,
        AsyncNeptuneGraphClientConfig,
    )
    from aws_sdk_neptune_graph._services.neptune_graph import (
        NeptuneGraphClient,
        NeptuneGraphClientConfig,
    )


class PrivateGraphEndpointResource:
    def __init__(self, service: NeptuneGraphClient) -> None:
        self._service = service

    def create_private_graph_endpoint(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        vpc_id: Optional["aws_sdk_neptune_graph.types.vpc_id.VpcId"] = None,
        subnet_ids: Optional["aws_sdk_neptune_graph.types.subnet_ids.SubnetIds"] = None,
        vpc_security_group_ids: Optional[
            "aws_sdk_neptune_graph.types.security_group_ids.SecurityGroupIds"
        ] = None,
    ) -> "aws_sdk_neptune_graph.types.create_private_graph_endpoint_output.CreatePrivateGraphEndpointOutput":
        """<p>Create a private graph endpoint to allow private access to the graph from within a VPC. You can attach security groups to the private graph endpoint.</p> <note> <p>VPC endpoint charges apply.</p> </note>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            vpc_id: <p> The VPC in which the private graph endpoint needs to be created.</p>
            subnet_ids: <p>Subnets in which private graph endpoint ENIs are created.</p>
            vpc_security_group_ids: <p>Security groups to be attached to the private graph endpoint.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.create_private_graph_endpoint_input.CreatePrivateGraphEndpointInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.create_private_graph_endpoint_output.CreatePrivateGraphEndpointOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.create_private_graph_endpoint

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.create_private_graph_endpoint.create_private_graph_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.create_private_graph_endpoint_input.CreatePrivateGraphEndpointInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        if vpc_id is not None:
            input["vpc_id"] = vpc_id
        if subnet_ids is not None:
            input["subnet_ids"] = subnet_ids
        if vpc_security_group_ids is not None:
            input["vpc_security_group_ids"] = vpc_security_group_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_private_graph_endpoint(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        vpc_id: "aws_sdk_neptune_graph.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.delete_private_graph_endpoint_output.DeletePrivateGraphEndpointOutput":
        """<p>Deletes a private graph endpoint.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            vpc_id: <p>The ID of the VPC where the private endpoint is located.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.delete_private_graph_endpoint_input.DeletePrivateGraphEndpointInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.delete_private_graph_endpoint_output.DeletePrivateGraphEndpointOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.delete_private_graph_endpoint

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.delete_private_graph_endpoint.delete_private_graph_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.delete_private_graph_endpoint_input.DeletePrivateGraphEndpointInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        input["vpc_id"] = vpc_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_private_graph_endpoint(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        vpc_id: "aws_sdk_neptune_graph.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.get_private_graph_endpoint_output.GetPrivateGraphEndpointOutput":
        """<p>Retrieves information about a specified private endpoint.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            vpc_id: <p>The ID of the VPC where the private endpoint is located.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.get_private_graph_endpoint_input.GetPrivateGraphEndpointInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.get_private_graph_endpoint_output.GetPrivateGraphEndpointOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_private_graph_endpoint

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_private_graph_endpoint.get_private_graph_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.get_private_graph_endpoint_input.GetPrivateGraphEndpointInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        input["vpc_id"] = vpc_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_private_graph_endpoints(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_neptune_graph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_neptune_graph.types.list_private_graph_endpoints_output.ListPrivateGraphEndpointsOutput":
        """<p>Lists private endpoints for a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_neptune_graph.types.list_private_graph_endpoints_input.ListPrivateGraphEndpointsInput]",
        ) -> OperationResponse[
            "aws_sdk_neptune_graph.types.list_private_graph_endpoints_output.ListPrivateGraphEndpointsOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_private_graph_endpoints

            output, http_response = (
                aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_private_graph_endpoints.list_private_graph_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.list_private_graph_endpoints_input.ListPrivateGraphEndpointsInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncPrivateGraphEndpointResource:
    def __init__(self, service: AsyncNeptuneGraphClient) -> None:
        self._service = service

    async def create_private_graph_endpoint(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        vpc_id: Optional["aws_sdk_neptune_graph.types.vpc_id.VpcId"] = None,
        subnet_ids: Optional["aws_sdk_neptune_graph.types.subnet_ids.SubnetIds"] = None,
        vpc_security_group_ids: Optional[
            "aws_sdk_neptune_graph.types.security_group_ids.SecurityGroupIds"
        ] = None,
    ) -> "aws_sdk_neptune_graph.types.create_private_graph_endpoint_output.CreatePrivateGraphEndpointOutput":
        """<p>Create a private graph endpoint to allow private access to the graph from within a VPC. You can attach security groups to the private graph endpoint.</p> <note> <p>VPC endpoint charges apply.</p> </note>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            vpc_id: <p> The VPC in which the private graph endpoint needs to be created.</p>
            subnet_ids: <p>Subnets in which private graph endpoint ENIs are created.</p>
            vpc_security_group_ids: <p>Security groups to be attached to the private graph endpoint.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.create_private_graph_endpoint_input.CreatePrivateGraphEndpointInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.create_private_graph_endpoint_output.CreatePrivateGraphEndpointOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.create_private_graph_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.create_private_graph_endpoint.async_create_private_graph_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.create_private_graph_endpoint_input.CreatePrivateGraphEndpointInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        if vpc_id is not None:
            input["vpc_id"] = vpc_id
        if subnet_ids is not None:
            input["subnet_ids"] = subnet_ids
        if vpc_security_group_ids is not None:
            input["vpc_security_group_ids"] = vpc_security_group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_private_graph_endpoint(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        vpc_id: "aws_sdk_neptune_graph.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.delete_private_graph_endpoint_output.DeletePrivateGraphEndpointOutput":
        """<p>Deletes a private graph endpoint.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            vpc_id: <p>The ID of the VPC where the private endpoint is located.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.delete_private_graph_endpoint_input.DeletePrivateGraphEndpointInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.delete_private_graph_endpoint_output.DeletePrivateGraphEndpointOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.delete_private_graph_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.delete_private_graph_endpoint.async_delete_private_graph_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.delete_private_graph_endpoint_input.DeletePrivateGraphEndpointInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        input["vpc_id"] = vpc_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_private_graph_endpoint(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        vpc_id: "aws_sdk_neptune_graph.types.vpc_id.VpcId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "aws_sdk_neptune_graph.types.get_private_graph_endpoint_output.GetPrivateGraphEndpointOutput":
        """<p>Retrieves information about a specified private endpoint.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            vpc_id: <p>The ID of the VPC where the private endpoint is located.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.get_private_graph_endpoint_input.GetPrivateGraphEndpointInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.get_private_graph_endpoint_output.GetPrivateGraphEndpointOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_private_graph_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.get_private_graph_endpoint.async_get_private_graph_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.get_private_graph_endpoint_input.GetPrivateGraphEndpointInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        input["vpc_id"] = vpc_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_private_graph_endpoints(
        self,
        graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        next_token: Optional[
            "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "aws_sdk_neptune_graph.types.max_results.MaxResults"
        ] = None,
    ) -> "aws_sdk_neptune_graph.types.list_private_graph_endpoints_output.ListPrivateGraphEndpointsOutput":
        """<p>Lists private endpoints for a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_neptune_graph.types.list_private_graph_endpoints_input.ListPrivateGraphEndpointsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_neptune_graph.types.list_private_graph_endpoints_output.ListPrivateGraphEndpointsOutput"
        ]:
            import aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_private_graph_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_neptune_graph._operations.amazon_neptune_graph.list_private_graph_endpoints.async_list_private_graph_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_neptune_graph.types.list_private_graph_endpoints_input.ListPrivateGraphEndpointsInput = {}  # type: ignore[typeddict-item]
        input["graph_identifier"] = graph_identifier
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
