from __future__ import annotations

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
    import aws_sdk_vpc_lattice.types.boolean
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.create_resource_configuration_request
    import aws_sdk_vpc_lattice.types.create_resource_configuration_response
    import aws_sdk_vpc_lattice.types.delete_resource_configuration_request
    import aws_sdk_vpc_lattice.types.delete_resource_configuration_response
    import aws_sdk_vpc_lattice.types.domain_name
    import aws_sdk_vpc_lattice.types.domain_verification_identifier
    import aws_sdk_vpc_lattice.types.get_resource_configuration_request
    import aws_sdk_vpc_lattice.types.get_resource_configuration_response
    import aws_sdk_vpc_lattice.types.list_resource_configurations_request
    import aws_sdk_vpc_lattice.types.list_resource_configurations_response
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.port_range_list
    import aws_sdk_vpc_lattice.types.protocol_type
    import aws_sdk_vpc_lattice.types.resource_configuration_definition
    import aws_sdk_vpc_lattice.types.resource_configuration_identifier
    import aws_sdk_vpc_lattice.types.resource_configuration_name
    import aws_sdk_vpc_lattice.types.resource_configuration_summary
    import aws_sdk_vpc_lattice.types.resource_configuration_type
    import aws_sdk_vpc_lattice.types.resource_gateway_identifier
    import aws_sdk_vpc_lattice.types.tag_map
    import aws_sdk_vpc_lattice.types.update_resource_configuration_request
    import aws_sdk_vpc_lattice.types.update_resource_configuration_response
    from aws_sdk_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from aws_sdk_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class ResourceConfiguration:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName",
        type: "aws_sdk_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        port_ranges: Optional[
            "aws_sdk_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
        protocol: Optional[
            "aws_sdk_vpc_lattice.types.protocol_type.ProtocolType"
        ] = None,
        resource_gateway_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        resource_configuration_definition: Optional[
            "aws_sdk_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "aws_sdk_vpc_lattice.types.boolean.Boolean"
        ] = None,
        custom_domain_name: Optional[
            "aws_sdk_vpc_lattice.types.domain_name.DomainName"
        ] = None,
        group_domain: Optional[
            "aws_sdk_vpc_lattice.types.domain_name.DomainName"
        ] = None,
        domain_verification_identifier: Optional[
            "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse":
        """<p>Creates a resource configuration. A resource configuration defines a specific resource. You can associate a resource configuration with a service network or a VPC endpoint.</p>

        Args:
            name: <p>The name of the resource configuration. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            type: <p>The type of resource configuration. A resource configuration can be one of the following types:</p> <ul> <li> <p> <b>SINGLE</b> - A single resource.</p> </li> <li> <p> <b>GROUP</b> - A group of resources. You must create a group resource configuration before you create a child resource configuration.</p> </li> <li> <p> <b>CHILD</b> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <b>ARN</b> - An Amazon Web Services resource.</p> </li> </ul>
            port_ranges: <p>(SINGLE, GROUP, CHILD) The TCP port ranges that a consumer can use to access a resource configuration (for example: 1-65535). You can separate port ranges using commas (for example: 1,2,22-30).</p>
            protocol: <p>(SINGLE, GROUP) The protocol accepted by the resource configuration.</p>
            resource_gateway_identifier: <p>(SINGLE, GROUP, ARN) The ID or ARN of the resource gateway used to connect to the resource configuration. For a child resource configuration, this value is inherited from the parent resource configuration.</p>
            resource_configuration_group_identifier: <p>(CHILD) The ID or ARN of the parent resource configuration of type <code>GROUP</code>. This is used to associate a child resource configuration with a group resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>(SINGLE, GROUP, ARN) Specifies whether the resource configuration can be associated with a sharable service network. The default is false.</p>
            custom_domain_name: <p> A custom domain name for your resource configuration. Additionally, provide a DomainVerificationID to prove your ownership of a domain. </p>
            group_domain: <p> (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain. </p>
            domain_verification_identifier: <p> The domain verification ID of your verified custom domain name. If you don't provide an ID, you must configure the DNS settings yourself. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the resource configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_resource_configuration

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.create_resource_configuration.create_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["type"] = type
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges
        if protocol is not None:
            input_["protocol"] = protocol
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if group_domain is not None:
            input_["group_domain"] = group_domain
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
        if client_token is not None:
            input_["client_token"] = client_token
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
        resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse":
        """<p>Retrieves information about the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_configuration

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_configuration.get_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_configuration_identifier"] = resource_configuration_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_configuration_definition: Optional[
            "aws_sdk_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "aws_sdk_vpc_lattice.types.boolean.Boolean"
        ] = None,
        port_ranges: Optional[
            "aws_sdk_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse":
        """<p>Updates the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>Indicates whether to add the resource configuration to service networks that are shared with other accounts.</p>
            port_ranges: <p>The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_resource_configuration

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.update_resource_configuration.update_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_configuration_identifier"] = resource_configuration_identifier
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse":
        """<p>Deletes the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID or ARN of the resource configuration.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration.delete_resource_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_configuration_identifier"] = resource_configuration_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        resource_gateway_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        domain_verification_identifier: Optional[
            "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse":
        """<p>Lists the resource configurations owned by or shared with this account.</p>

        Args:
            resource_gateway_identifier: <p>The ID of the resource gateway for the resource configuration.</p>
            resource_configuration_group_identifier: <p>The ID of the resource configuration of type <code>Group</code>.</p>
            domain_verification_identifier: <p> The domain verification ID. </p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_configurations

            output, http_response = (
                aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_configurations.list_resource_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncResourceConfiguration:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_vpc_lattice.types.resource_configuration_name.ResourceConfigurationName",
        type: "aws_sdk_vpc_lattice.types.resource_configuration_type.ResourceConfigurationType",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        port_ranges: Optional[
            "aws_sdk_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
        protocol: Optional[
            "aws_sdk_vpc_lattice.types.protocol_type.ProtocolType"
        ] = None,
        resource_gateway_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        resource_configuration_definition: Optional[
            "aws_sdk_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "aws_sdk_vpc_lattice.types.boolean.Boolean"
        ] = None,
        custom_domain_name: Optional[
            "aws_sdk_vpc_lattice.types.domain_name.DomainName"
        ] = None,
        group_domain: Optional[
            "aws_sdk_vpc_lattice.types.domain_name.DomainName"
        ] = None,
        domain_verification_identifier: Optional[
            "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        client_token: Optional[
            "aws_sdk_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        tags: Optional["aws_sdk_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "aws_sdk_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse":
        """<p>Creates a resource configuration. A resource configuration defines a specific resource. You can associate a resource configuration with a service network or a VPC endpoint.</p>

        Args:
            name: <p>The name of the resource configuration. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>
            type: <p>The type of resource configuration. A resource configuration can be one of the following types:</p> <ul> <li> <p> <b>SINGLE</b> - A single resource.</p> </li> <li> <p> <b>GROUP</b> - A group of resources. You must create a group resource configuration before you create a child resource configuration.</p> </li> <li> <p> <b>CHILD</b> - A single resource that is part of a group resource configuration.</p> </li> <li> <p> <b>ARN</b> - An Amazon Web Services resource.</p> </li> </ul>
            port_ranges: <p>(SINGLE, GROUP, CHILD) The TCP port ranges that a consumer can use to access a resource configuration (for example: 1-65535). You can separate port ranges using commas (for example: 1,2,22-30).</p>
            protocol: <p>(SINGLE, GROUP) The protocol accepted by the resource configuration.</p>
            resource_gateway_identifier: <p>(SINGLE, GROUP, ARN) The ID or ARN of the resource gateway used to connect to the resource configuration. For a child resource configuration, this value is inherited from the parent resource configuration.</p>
            resource_configuration_group_identifier: <p>(CHILD) The ID or ARN of the parent resource configuration of type <code>GROUP</code>. This is used to associate a child resource configuration with a group resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>(SINGLE, GROUP, ARN) Specifies whether the resource configuration can be associated with a sharable service network. The default is false.</p>
            custom_domain_name: <p> A custom domain name for your resource configuration. Additionally, provide a DomainVerificationID to prove your ownership of a domain. </p>
            group_domain: <p> (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain. </p>
            domain_verification_identifier: <p> The domain verification ID of your verified custom domain name. If you don't provide an ID, you must configure the DNS settings yourself. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            tags: <p>The tags for the resource configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.create_resource_configuration_response.CreateResourceConfigurationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.create_resource_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.create_resource_configuration.async_create_resource_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.create_resource_configuration_request.CreateResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        input_["type"] = type
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges
        if protocol is not None:
            input_["protocol"] = protocol
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if group_domain is not None:
            input_["group_domain"] = group_domain
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
        if client_token is not None:
            input_["client_token"] = client_token
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
        resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse":
        """<p>Retrieves information about the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.get_resource_configuration_response.GetResourceConfigurationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.get_resource_configuration.async_get_resource_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.get_resource_configuration_request.GetResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_configuration_identifier"] = resource_configuration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        resource_configuration_definition: Optional[
            "aws_sdk_vpc_lattice.types.resource_configuration_definition.ResourceConfigurationDefinition"
        ] = None,
        allow_association_to_shareable_service_network: Optional[
            "aws_sdk_vpc_lattice.types.boolean.Boolean"
        ] = None,
        port_ranges: Optional[
            "aws_sdk_vpc_lattice.types.port_range_list.PortRangeList"
        ] = None,
    ) -> "aws_sdk_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse":
        """<p>Updates the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID of the resource configuration.</p>
            resource_configuration_definition: <p>Identifies the resource configuration in one of the following ways:</p> <ul> <li> <p> <b>Amazon Resource Name (ARN)</b> - Supported resource-types that are provisioned by Amazon Web Services services, such as RDS databases, can be identified by their ARN.</p> </li> <li> <p> <b>Domain name</b> - Any domain name that is publicly resolvable.</p> </li> <li> <p> <b>IP address</b> - For IPv4 and IPv6, only IP addresses in the VPC are supported.</p> </li> </ul>
            allow_association_to_shareable_service_network: <p>Indicates whether to add the resource configuration to service networks that are shared with other accounts.</p>
            port_ranges: <p>The TCP port ranges that a consumer can use to access a resource configuration. You can separate port ranges with a comma. Example: 1-65535 or 1,2,22-30</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.update_resource_configuration_response.UpdateResourceConfigurationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.update_resource_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.update_resource_configuration.async_update_resource_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.update_resource_configuration_request.UpdateResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_configuration_identifier"] = resource_configuration_identifier
        if resource_configuration_definition is not None:
            input_["resource_configuration_definition"] = (
                resource_configuration_definition
            )
        if allow_association_to_shareable_service_network is not None:
            input_["allow_association_to_shareable_service_network"] = (
                allow_association_to_shareable_service_network
            )
        if port_ranges is not None:
            input_["port_ranges"] = port_ranges

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "aws_sdk_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse":
        """<p>Deletes the specified resource configuration.</p>

        Args:
            resource_configuration_identifier: <p>The ID or ARN of the resource configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.delete_resource_configuration_response.DeleteResourceConfigurationResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.delete_resource_configuration.async_delete_resource_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.delete_resource_configuration_request.DeleteResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource_configuration_identifier"] = resource_configuration_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        resource_gateway_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
        ] = None,
        resource_configuration_group_identifier: Optional[
            "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
        ] = None,
        domain_verification_identifier: Optional[
            "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
        ] = None,
        max_results: Optional[
            "aws_sdk_vpc_lattice.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse":
        """<p>Lists the resource configurations owned by or shared with this account.</p>

        Args:
            resource_gateway_identifier: <p>The ID of the resource gateway for the resource configuration.</p>
            resource_configuration_group_identifier: <p>The ID of the resource configuration of type <code>Group</code>.</p>
            domain_verification_identifier: <p> The domain verification ID. </p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>A pagination token for the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_vpc_lattice.types.list_resource_configurations_response.ListResourceConfigurationsResponse"
        ]:
            import aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_vpc_lattice._operations.mercury_control_plane.list_resource_configurations.async_list_resource_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_vpc_lattice.types.list_resource_configurations_request.ListResourceConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if resource_gateway_identifier is not None:
            input_["resource_gateway_identifier"] = resource_gateway_identifier
        if resource_configuration_group_identifier is not None:
            input_["resource_configuration_group_identifier"] = (
                resource_configuration_group_identifier
            )
        if domain_verification_identifier is not None:
            input_["domain_verification_identifier"] = domain_verification_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
