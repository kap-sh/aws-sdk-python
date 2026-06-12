from typing import TYPE_CHECKING, Optional

import aws_sdk_vpc_lattice._auth._signers
import aws_sdk_vpc_lattice._auth._sigv4
from aws_sdk_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_resource_gateway_request
    import aws_sdk_vpc_lattice.types.create_resource_gateway_response
    import aws_sdk_vpc_lattice.types.delete_resource_gateway_request
    import aws_sdk_vpc_lattice.types.delete_resource_gateway_response
    import aws_sdk_vpc_lattice.types.get_resource_gateway_request
    import aws_sdk_vpc_lattice.types.get_resource_gateway_response
    import aws_sdk_vpc_lattice.types.ipv4_addresses_per_eni
    import aws_sdk_vpc_lattice.types.list_resource_gateways_request
    import aws_sdk_vpc_lattice.types.list_resource_gateways_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.resource_config_dns_resolution
    import aws_sdk_vpc_lattice.types.resource_gateway_identifier
    import aws_sdk_vpc_lattice.types.resource_gateway_ip_address_type
    import aws_sdk_vpc_lattice.types.resource_gateway_name
    import aws_sdk_vpc_lattice.types.resource_gateway_summary
    import aws_sdk_vpc_lattice.types.security_group_list
    import aws_sdk_vpc_lattice.types.subnet_list
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.update_resource_gateway_request
    import aws_sdk_vpc_lattice.types.update_resource_gateway_response
    import aws_sdk_vpc_lattice.types.vpc_id
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ResourceGateway:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_vpc_lattice.types.resource_gateway_name.ResourceGatewayName",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        vpc_identifier: Optional["aws_sdk_vpc_lattice.types.vpc_id.VpcId"] = None,
        subnet_ids: Optional["aws_sdk_vpc_lattice.types.subnet_list.SubnetList"] = None,
        security_group_ids: Optional[
            "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_vpc_lattice.types.resource_gateway_ip_address_type.ResourceGatewayIpAddressType"
        ] = None,
        ipv4_addresses_per_eni: Optional[
            "aws_sdk_vpc_lattice.types.ipv4_addresses_per_eni.Ipv4AddressesPerEni"
        ] = None,
        resource_config_dns_resolution: Optional[
            "aws_sdk_vpc_lattice.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_resource_gateway_response.CreateResourceGatewayResponse":
        """<p>A resource gateway is a point of ingress into the VPC where a resource resides. It spans multiple Availability Zones. For your resource to be accessible from all Availability Zones, you should create your resource gateways to span as many Availability Zones as possible. A VPC can have multiple resource gateways.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the resource gateway.</p>
            vpc_identifier: <p>The ID of the VPC for the resource gateway.</p>
            subnet_ids: <p>The IDs of the VPC subnets in which to create the resource gateway.</p>
            security_group_ids: <p>The IDs of the security groups to apply to the resource gateway. The security groups must be in the same VPC.</p>
            ip_address_type: <p>A resource gateway can have IPv4, IPv6 or dualstack addresses. The IP address type of a resource gateway must be compatible with the subnets of the resource gateway and the IP address type of the resource, as described here: </p> <ul> <li> <p> <b>IPv4</b>Assign IPv4 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have IPv4 address ranges, and the resource also has an IPv4 address.</p> </li> <li> <p> <b>IPv6</b>Assign IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets are IPv6 only subnets, and the resource also has an IPv6 address.</p> </li> <li> <p> <b>Dualstack</b>Assign both IPv4 and IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges, and the resource either has an IPv4 or IPv6 address.</p> </li> </ul> <p>The IP address type of the resource gateway is independent of the IP address type of the client or the VPC endpoint through which the resource is accessed.</p>
            ipv4_addresses_per_eni: <p>The number of IPv4 addresses in each ENI for the resource gateway.</p>
            resource_config_dns_resolution: <p>Indicates how DNS is resolved for resource configurations associated to this resource gateway. ResourceConfigDnsResolution is set at creation time and cannot be changed.</p> <ul> <li> <p> <code>IN_VPC</code> - DNS resolution occurs privately within the resource gateway's VPC. DNS queries for resources behind this resource gateway resolve using the DNS resolvers defined in the VPC's DHCP option sets. Use this when your resource domain names are hosted in private Route 53 hosted zones or on-premises DNS servers reachable from the VPC.</p> </li> <li> <p> <code>PUBLIC</code> - DNS resolution occurs against public DNS resolvers. DNS queries for resources behind this resource gateway resolve using standard public DNS. Use this when your resource domain names are publicly resolvable.</p> </li> </ul>
            tags: <p>The tags for the resource gateway.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_resource_gateway_request.CreateResourceGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_resource_gateway_response.CreateResourceGatewayResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_resource_gateway

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_resource_gateway.create_resource_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.create_resource_gateway_request.CreateResourceGatewayRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["name"] = name
        if vpc_identifier is not None:
            input["vpc_identifier"] = vpc_identifier
        if subnet_ids is not None:
            input["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input["security_group_ids"] = security_group_ids
        if ip_address_type is not None:
            input["ip_address_type"] = ip_address_type
        if ipv4_addresses_per_eni is not None:
            input["ipv4_addresses_per_eni"] = ipv4_addresses_per_eni
        if resource_config_dns_resolution is not None:
            input["resource_config_dns_resolution"] = resource_config_dns_resolution
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
        resource_gateway_identifier: "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_resource_gateway_response.GetResourceGatewayResponse":
        """<p>Retrieves information about the specified resource gateway.</p>

        Args:
            resource_gateway_identifier: <p>The ID of the resource gateway.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_resource_gateway_request.GetResourceGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_resource_gateway_response.GetResourceGatewayResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_gateway

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_gateway.get_resource_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.get_resource_gateway_request.GetResourceGatewayRequest = {}  # type: ignore[typeddict-item]
        input["resource_gateway_identifier"] = resource_gateway_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        resource_gateway_identifier: "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        security_group_ids: Optional[
            "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_resource_gateway_response.UpdateResourceGatewayResponse":
        """<p>Updates the specified resource gateway.</p>

        Args:
            resource_gateway_identifier: <p>The ID or ARN of the resource gateway.</p>
            security_group_ids: <p>The IDs of the security groups associated with the resource gateway.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.update_resource_gateway_request.UpdateResourceGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.update_resource_gateway_response.UpdateResourceGatewayResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_resource_gateway

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.update_resource_gateway.update_resource_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.update_resource_gateway_request.UpdateResourceGatewayRequest = {}  # type: ignore[typeddict-item]
        input["resource_gateway_identifier"] = resource_gateway_identifier
        if security_group_ids is not None:
            input["security_group_ids"] = security_group_ids

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        resource_gateway_identifier: "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_resource_gateway_response.DeleteResourceGatewayResponse":
        """<p>Deletes the specified resource gateway.</p>

        Args:
            resource_gateway_identifier: <p>The ID or ARN of the resource gateway.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_resource_gateway_request.DeleteResourceGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_resource_gateway_response.DeleteResourceGatewayResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_gateway

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_gateway.delete_resource_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.delete_resource_gateway_request.DeleteResourceGatewayRequest = {}  # type: ignore[typeddict-item]
        input["resource_gateway_identifier"] = resource_gateway_identifier

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_resource_gateways_response.ListResourceGatewaysResponse":
        """<p>Lists the resource gateways that you own or that were shared with you.</p>

        Args:
            max_results: <p>The maximum page size.</p>
            next_token: <p>If there are additional results, a pagination token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_resource_gateways_request.ListResourceGatewaysRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_resource_gateways_response.ListResourceGatewaysResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_gateways

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_gateways.list_resource_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.list_resource_gateways_request.ListResourceGatewaysRequest = {}  # type: ignore[typeddict-item]
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


class AsyncResourceGateway:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_vpc_lattice.types.resource_gateway_name.ResourceGatewayName",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        vpc_identifier: Optional["aws_sdk_vpc_lattice.types.vpc_id.VpcId"] = None,
        subnet_ids: Optional["aws_sdk_vpc_lattice.types.subnet_list.SubnetList"] = None,
        security_group_ids: Optional[
            "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_vpc_lattice.types.resource_gateway_ip_address_type.ResourceGatewayIpAddressType"
        ] = None,
        ipv4_addresses_per_eni: Optional[
            "aws_sdk_vpc_lattice.types.ipv4_addresses_per_eni.Ipv4AddressesPerEni"
        ] = None,
        resource_config_dns_resolution: Optional[
            "aws_sdk_vpc_lattice.types.resource_config_dns_resolution.ResourceConfigDnsResolution"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_resource_gateway_response.CreateResourceGatewayResponse":
        """<p>A resource gateway is a point of ingress into the VPC where a resource resides. It spans multiple Availability Zones. For your resource to be accessible from all Availability Zones, you should create your resource gateways to span as many Availability Zones as possible. A VPC can have multiple resource gateways.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            name: <p>The name of the resource gateway.</p>
            vpc_identifier: <p>The ID of the VPC for the resource gateway.</p>
            subnet_ids: <p>The IDs of the VPC subnets in which to create the resource gateway.</p>
            security_group_ids: <p>The IDs of the security groups to apply to the resource gateway. The security groups must be in the same VPC.</p>
            ip_address_type: <p>A resource gateway can have IPv4, IPv6 or dualstack addresses. The IP address type of a resource gateway must be compatible with the subnets of the resource gateway and the IP address type of the resource, as described here: </p> <ul> <li> <p> <b>IPv4</b>Assign IPv4 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have IPv4 address ranges, and the resource also has an IPv4 address.</p> </li> <li> <p> <b>IPv6</b>Assign IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets are IPv6 only subnets, and the resource also has an IPv6 address.</p> </li> <li> <p> <b>Dualstack</b>Assign both IPv4 and IPv6 addresses to your resource gateway network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges, and the resource either has an IPv4 or IPv6 address.</p> </li> </ul> <p>The IP address type of the resource gateway is independent of the IP address type of the client or the VPC endpoint through which the resource is accessed.</p>
            ipv4_addresses_per_eni: <p>The number of IPv4 addresses in each ENI for the resource gateway.</p>
            resource_config_dns_resolution: <p>Indicates how DNS is resolved for resource configurations associated to this resource gateway. ResourceConfigDnsResolution is set at creation time and cannot be changed.</p> <ul> <li> <p> <code>IN_VPC</code> - DNS resolution occurs privately within the resource gateway's VPC. DNS queries for resources behind this resource gateway resolve using the DNS resolvers defined in the VPC's DHCP option sets. Use this when your resource domain names are hosted in private Route 53 hosted zones or on-premises DNS servers reachable from the VPC.</p> </li> <li> <p> <code>PUBLIC</code> - DNS resolution occurs against public DNS resolvers. DNS queries for resources behind this resource gateway resolve using standard public DNS. Use this when your resource domain names are publicly resolvable.</p> </li> </ul>
            tags: <p>The tags for the resource gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_resource_gateway_request.CreateResourceGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_resource_gateway_response.CreateResourceGatewayResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_resource_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_resource_gateway.async_create_resource_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.create_resource_gateway_request.CreateResourceGatewayRequest = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["name"] = name
        if vpc_identifier is not None:
            input["vpc_identifier"] = vpc_identifier
        if subnet_ids is not None:
            input["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input["security_group_ids"] = security_group_ids
        if ip_address_type is not None:
            input["ip_address_type"] = ip_address_type
        if ipv4_addresses_per_eni is not None:
            input["ipv4_addresses_per_eni"] = ipv4_addresses_per_eni
        if resource_config_dns_resolution is not None:
            input["resource_config_dns_resolution"] = resource_config_dns_resolution
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
        resource_gateway_identifier: "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_resource_gateway_response.GetResourceGatewayResponse":
        """<p>Retrieves information about the specified resource gateway.</p>

        Args:
            resource_gateway_identifier: <p>The ID of the resource gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_resource_gateway_request.GetResourceGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_resource_gateway_response.GetResourceGatewayResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_gateway.async_get_resource_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.get_resource_gateway_request.GetResourceGatewayRequest = {}  # type: ignore[typeddict-item]
        input["resource_gateway_identifier"] = resource_gateway_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        resource_gateway_identifier: "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        security_group_ids: Optional[
            "aws_sdk_vpc_lattice.types.security_group_list.SecurityGroupList"
        ] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_resource_gateway_response.UpdateResourceGatewayResponse":
        """<p>Updates the specified resource gateway.</p>

        Args:
            resource_gateway_identifier: <p>The ID or ARN of the resource gateway.</p>
            security_group_ids: <p>The IDs of the security groups associated with the resource gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.update_resource_gateway_request.UpdateResourceGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.update_resource_gateway_response.UpdateResourceGatewayResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_resource_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.update_resource_gateway.async_update_resource_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.update_resource_gateway_request.UpdateResourceGatewayRequest = {}  # type: ignore[typeddict-item]
        input["resource_gateway_identifier"] = resource_gateway_identifier
        if security_group_ids is not None:
            input["security_group_ids"] = security_group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        resource_gateway_identifier: "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_resource_gateway_response.DeleteResourceGatewayResponse":
        """<p>Deletes the specified resource gateway.</p>

        Args:
            resource_gateway_identifier: <p>The ID or ARN of the resource gateway.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_resource_gateway_request.DeleteResourceGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_resource_gateway_response.DeleteResourceGatewayResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_gateway.async_delete_resource_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.delete_resource_gateway_request.DeleteResourceGatewayRequest = {}  # type: ignore[typeddict-item]
        input["resource_gateway_identifier"] = resource_gateway_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_resource_gateways_response.ListResourceGatewaysResponse":
        """<p>Lists the resource gateways that you own or that were shared with you.</p>

        Args:
            max_results: <p>The maximum page size.</p>
            next_token: <p>If there are additional results, a pagination token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_resource_gateways_request.ListResourceGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_resource_gateways_response.ListResourceGatewaysResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_gateways

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_gateways.async_list_resource_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_vpc_lattice.types.list_resource_gateways_request.ListResourceGatewaysRequest = {}  # type: ignore[typeddict-item]
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
