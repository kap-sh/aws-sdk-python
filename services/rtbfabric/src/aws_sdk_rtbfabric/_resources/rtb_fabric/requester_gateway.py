from typing import TYPE_CHECKING, Optional

import aws_sdk_rtbfabric._auth._signers
import aws_sdk_rtbfabric._auth._sigv4
from aws_sdk_rtbfabric._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.create_requester_gateway_request
    import aws_sdk_rtbfabric.types.create_requester_gateway_response
    import aws_sdk_rtbfabric.types.delete_requester_gateway_request
    import aws_sdk_rtbfabric.types.delete_requester_gateway_response
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.get_requester_gateway_request
    import aws_sdk_rtbfabric.types.get_requester_gateway_response
    import aws_sdk_rtbfabric.types.security_group_id_list
    import aws_sdk_rtbfabric.types.subnet_id_list
    import aws_sdk_rtbfabric.types.tags_map
    import aws_sdk_rtbfabric.types.update_requester_gateway_request
    import aws_sdk_rtbfabric.types.update_requester_gateway_response
    import aws_sdk_rtbfabric.types.vpc_id
    from aws_sdk_rtbfabric._services.async_rtb_fabric import (
        AsyncRTBFabricClient,
        AsyncRTBFabricClientConfig,
    )
    from aws_sdk_rtbfabric._services.rtb_fabric import (
        RTBFabricClient,
        RTBFabricClientConfig,
    )


class RequesterGateway:
    def __init__(self, service: RTBFabricClient) -> None:
        self._service = service

    def create(
        self,
        vpc_id: "aws_sdk_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "aws_sdk_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "aws_sdk_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        client_token: str,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["aws_sdk_rtbfabric.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse":
        """<p>Creates a requester gateway.</p>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>The unique identifiers of the subnets.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            client_token: <p>The unique client token.</p>
            description: <p>An optional description for the requester gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Examples:
            Create a requester gateway
            Create requester gateway

            >>> client.create(description='My requester gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], client_token='12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.create_requester_gateway

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.create_requester_gateway.create_requester_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
        input["vpc_id"] = vpc_id
        input["subnet_ids"] = subnet_ids
        input["security_group_ids"] = security_group_ids
        input["client_token"] = client_token
        if description is not None:
            input["description"] = description
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
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse":
        """<p>Retrieves information about a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Examples:
            Get requester gateway details
            Get requester gateway

            >>> client.read(gateway_id='rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.get_requester_gateway

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.get_requester_gateway.get_requester_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
        input["gateway_id"] = gateway_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse":
        """<p>Deletes a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Examples:
            Delete a requester gateway
            Delete requester gateway

            >>> client.delete(gateway_id='rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.delete_requester_gateway

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.delete_requester_gateway.delete_requester_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
        input["gateway_id"] = gateway_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_requester_gateway(
        self,
        client_token: str,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        description: Optional[str] = None,
    ) -> "aws_sdk_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse":
        """<p>Updates a requester gateway.</p>

        Args:
            client_token: <p>The unique client token.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the requester gateway.</p>

        Examples:
            Update requester gateway
            Update requester gateway

            >>> client.update_requester_gateway(gateway_id='rtb-gw-12345678', description='Updated requester gateway description', client_token='12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.update_requester_gateway

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.update_requester_gateway.update_requester_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
        input["client_token"] = client_token
        input["gateway_id"] = gateway_id
        if description is not None:
            input["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRequesterGateway:
    def __init__(self, service: AsyncRTBFabricClient) -> None:
        self._service = service

    async def create(
        self,
        vpc_id: "aws_sdk_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "aws_sdk_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "aws_sdk_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        client_token: str,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["aws_sdk_rtbfabric.types.tags_map.TagsMap"] = None,
    ) -> "aws_sdk_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse":
        """<p>Creates a requester gateway.</p>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>The unique identifiers of the subnets.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            client_token: <p>The unique client token.</p>
            description: <p>An optional description for the requester gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>

        Examples:
            Create a requester gateway
            Create requester gateway

            >>> await client.create(description='My requester gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.create_requester_gateway_response.CreateRequesterGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.create_requester_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.create_requester_gateway.async_create_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.create_requester_gateway_request.CreateRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
        input["vpc_id"] = vpc_id
        input["subnet_ids"] = subnet_ids
        input["security_group_ids"] = security_group_ids
        input["client_token"] = client_token
        if description is not None:
            input["description"] = description
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
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse":
        """<p>Retrieves information about a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Examples:
            Get requester gateway details
            Get requester gateway

            >>> await client.read(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.get_requester_gateway_response.GetRequesterGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.get_requester_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.get_requester_gateway.async_get_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.get_requester_gateway_request.GetRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
        input["gateway_id"] = gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse":
        """<p>Deletes a requester gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Examples:
            Delete a requester gateway
            Delete requester gateway

            >>> await client.delete(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.delete_requester_gateway_response.DeleteRequesterGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.delete_requester_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.delete_requester_gateway.async_delete_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.delete_requester_gateway_request.DeleteRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
        input["gateway_id"] = gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_requester_gateway(
        self,
        client_token: str,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        description: Optional[str] = None,
    ) -> "aws_sdk_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse":
        """<p>Updates a requester gateway.</p>

        Args:
            client_token: <p>The unique client token.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the requester gateway.</p>

        Examples:
            Update requester gateway
            Update requester gateway

            >>> await client.update_requester_gateway(gateway_id='rtb-gw-12345678', description='Updated requester gateway description', client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.update_requester_gateway_response.UpdateRequesterGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.update_requester_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.update_requester_gateway.async_update_requester_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_rtbfabric.types.update_requester_gateway_request.UpdateRequesterGatewayRequest = {}  # type: ignore[typeddict-item]
        input["client_token"] = client_token
        input["gateway_id"] = gateway_id
        if description is not None:
            input["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
