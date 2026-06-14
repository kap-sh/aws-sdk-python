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
    import aws_sdk_rtbfabric.types.acm_certificate_arn
    import aws_sdk_rtbfabric.types.associate_certificate_request
    import aws_sdk_rtbfabric.types.associate_certificate_response
    import aws_sdk_rtbfabric.types.certificate_association_summary
    import aws_sdk_rtbfabric.types.create_responder_gateway_request
    import aws_sdk_rtbfabric.types.create_responder_gateway_response
    import aws_sdk_rtbfabric.types.delete_responder_gateway_request
    import aws_sdk_rtbfabric.types.delete_responder_gateway_response
    import aws_sdk_rtbfabric.types.disassociate_certificate_request
    import aws_sdk_rtbfabric.types.disassociate_certificate_response
    import aws_sdk_rtbfabric.types.domain_name
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.gateway_type
    import aws_sdk_rtbfabric.types.get_certificate_association_request
    import aws_sdk_rtbfabric.types.get_certificate_association_response
    import aws_sdk_rtbfabric.types.get_responder_gateway_request
    import aws_sdk_rtbfabric.types.get_responder_gateway_response
    import aws_sdk_rtbfabric.types.list_certificate_associations_request
    import aws_sdk_rtbfabric.types.list_certificate_associations_response
    import aws_sdk_rtbfabric.types.listener_config
    import aws_sdk_rtbfabric.types.managed_endpoint_configuration
    import aws_sdk_rtbfabric.types.protocol
    import aws_sdk_rtbfabric.types.security_group_id_list
    import aws_sdk_rtbfabric.types.subnet_id_list
    import aws_sdk_rtbfabric.types.tags_map
    import aws_sdk_rtbfabric.types.trust_store_configuration
    import aws_sdk_rtbfabric.types.update_responder_gateway_request
    import aws_sdk_rtbfabric.types.update_responder_gateway_response
    import aws_sdk_rtbfabric.types.vpc_id
    from aws_sdk_rtbfabric._services.async_rtb_fabric import (
        AsyncRTBFabricClient,
        AsyncRTBFabricClientConfig,
    )
    from aws_sdk_rtbfabric._services.rtb_fabric import (
        RTBFabricClient,
        RTBFabricClientConfig,
    )


class ResponderGateway:
    def __init__(self, service: RTBFabricClient) -> None:
        self._service = service

    def create(
        self,
        vpc_id: "aws_sdk_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "aws_sdk_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "aws_sdk_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        port: int,
        protocol: "aws_sdk_rtbfabric.types.protocol.Protocol",
        client_token: str,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        domain_name: Optional["aws_sdk_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "aws_sdk_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "aws_sdk_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "aws_sdk_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["aws_sdk_rtbfabric.types.tags_map.TagsMap"] = None,
        gateway_type: Optional[
            "aws_sdk_rtbfabric.types.gateway_type.GatewayType"
        ] = None,
    ) -> "aws_sdk_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse":
        """<p>Creates a responder gateway.</p> <important> <p>A domain name or managed endpoint is required.</p> </important>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>The unique identifiers of the subnets.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            domain_name: <p>The domain name for the responder gateway.</p>
            port: <p>The networking port to use.</p>
            protocol: <p>The networking protocol to use.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>The unique client token.</p>
            description: <p>An optional description for the responder gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
            gateway_type: <p>The type of gateway. Valid values are <code>EXTERNAL</code> or <code>INTERNAL</code>.</p>

        Examples:
            Create a responder gateway
            Create responder gateway

            >>> client.create(description='My responder gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], port=443, protocol='HTTPS', client_token='12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.create_responder_gateway

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.create_responder_gateway.create_responder_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_id"] = vpc_id
        input_["subnet_ids"] = subnet_ids
        input_["security_group_ids"] = security_group_ids
        if domain_name is not None:
            input_["domain_name"] = domain_name
        input_["port"] = port
        input_["protocol"] = protocol
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if gateway_type is not None:
            input_["gateway_type"] = gateway_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse":
        """<p>Retrieves information about a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Examples:
            Get responder gateway details
            Get responder gateway

            >>> client.read(gateway_id='rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.get_responder_gateway

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.get_responder_gateway.get_responder_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse":
        """<p>Deletes a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Examples:
            Delete a responder gateway
            Delete responder gateway

            >>> client.delete(gateway_id='rtb-gw-12345678')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.delete_responder_gateway

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.delete_responder_gateway.delete_responder_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def associate_certificate(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        client_token: str,
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse":
        """<p>Associates an ACM certificate with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to associate.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Examples:
            Associate a certificate with a responder gateway
            Associate an ACM certificate with a responder gateway

            >>> client.associate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.associate_certificate

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.associate_certificate.associate_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
        input_["acm_certificate_arn"] = acm_certificate_arn
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_certificate(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse":
        """<p>Removes a certificate association from a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to disassociate.</p>

        Examples:
            Disassociate a certificate from a responder gateway
            Remove an ACM certificate association from a responder gateway

            >>> client.disassociate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.disassociate_certificate

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.disassociate_certificate.disassociate_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
        input_["acm_certificate_arn"] = acm_certificate_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_certificate_association(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse":
        """<p>Retrieves the details of a certificate association with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate.</p>

        Examples:
            Get certificate association details from a responder gateway
            Retrieve details of an ACM certificate association with a responder gateway

            >>> client.get_certificate_association(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.get_certificate_association

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.get_certificate_association.get_certificate_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
        input_["acm_certificate_arn"] = acm_certificate_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_certificate_associations(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse":
        """<p>Lists the certificate associations for a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Examples:
            List certificate associations for a responder gateway
            Retrieve all certificate associations for a responder gateway

            >>> client.list_certificate_associations(gateway_id='rtb-gw-12345678', max_results=5)
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.list_certificate_associations

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.list_certificate_associations.list_certificate_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
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

    def update_responder_gateway(
        self,
        port: int,
        protocol: "aws_sdk_rtbfabric.types.protocol.Protocol",
        client_token: str,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[RTBFabricClientConfig] = None,
        domain_name: Optional["aws_sdk_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "aws_sdk_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "aws_sdk_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "aws_sdk_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
    ) -> "aws_sdk_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse":
        """<p>Updates a responder gateway.</p>

        Args:
            domain_name: <p>The domain name for the responder gateway.</p>
            port: <p>The networking port to use.</p>
            protocol: <p>The networking protocol to use.</p>
            listener_config: <p>The listener configuration for the responder gateway.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>The unique client token.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the responder gateway.</p>

        Examples:
            Update responder gateway
            Update responder gateway

            >>> client.update_responder_gateway(gateway_id='rtb-gw-12345678', description='Updated responder gateway description', port=8080, protocol='HTTP', client_token='12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[aws_sdk_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest]",
        ) -> OperationResponse[
            "aws_sdk_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.update_responder_gateway

            output, http_response = (
                aws_sdk_rtbfabric._operations.rtb_fabric.update_responder_gateway.update_responder_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest = {}  # type: ignore[typeddict-item]
        if domain_name is not None:
            input_["domain_name"] = domain_name
        input_["port"] = port
        input_["protocol"] = protocol
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        input_["client_token"] = client_token
        input_["gateway_id"] = gateway_id
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncResponderGateway:
    def __init__(self, service: AsyncRTBFabricClient) -> None:
        self._service = service

    async def create(
        self,
        vpc_id: "aws_sdk_rtbfabric.types.vpc_id.VpcId",
        subnet_ids: "aws_sdk_rtbfabric.types.subnet_id_list.SubnetIdList",
        security_group_ids: "aws_sdk_rtbfabric.types.security_group_id_list.SecurityGroupIdList",
        port: int,
        protocol: "aws_sdk_rtbfabric.types.protocol.Protocol",
        client_token: str,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        domain_name: Optional["aws_sdk_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "aws_sdk_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "aws_sdk_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "aws_sdk_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["aws_sdk_rtbfabric.types.tags_map.TagsMap"] = None,
        gateway_type: Optional[
            "aws_sdk_rtbfabric.types.gateway_type.GatewayType"
        ] = None,
    ) -> "aws_sdk_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse":
        """<p>Creates a responder gateway.</p> <important> <p>A domain name or managed endpoint is required.</p> </important>

        Args:
            vpc_id: <p>The unique identifier of the Virtual Private Cloud (VPC).</p>
            subnet_ids: <p>The unique identifiers of the subnets.</p>
            security_group_ids: <p>The unique identifiers of the security groups.</p>
            domain_name: <p>The domain name for the responder gateway.</p>
            port: <p>The networking port to use.</p>
            protocol: <p>The networking protocol to use.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>The unique client token.</p>
            description: <p>An optional description for the responder gateway.</p>
            tags: <p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>
            gateway_type: <p>The type of gateway. Valid values are <code>EXTERNAL</code> or <code>INTERNAL</code>.</p>

        Examples:
            Create a responder gateway
            Create responder gateway

            >>> await client.create(description='My responder gateway', vpc_id='vpc-12345678', subnet_ids=['subnet-12345678', 'subnet-87654321'], security_group_ids=['sg-12345678'], port=443, protocol='HTTPS', client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.create_responder_gateway_response.CreateResponderGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.create_responder_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.create_responder_gateway.async_create_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.create_responder_gateway_request.CreateResponderGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["vpc_id"] = vpc_id
        input_["subnet_ids"] = subnet_ids
        input_["security_group_ids"] = security_group_ids
        if domain_name is not None:
            input_["domain_name"] = domain_name
        input_["port"] = port
        input_["protocol"] = protocol
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if gateway_type is not None:
            input_["gateway_type"] = gateway_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse":
        """<p>Retrieves information about a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Examples:
            Get responder gateway details
            Get responder gateway

            >>> await client.read(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.get_responder_gateway_response.GetResponderGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.get_responder_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.get_responder_gateway.async_get_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.get_responder_gateway_request.GetResponderGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse":
        """<p>Deletes a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>

        Examples:
            Delete a responder gateway
            Delete responder gateway

            >>> await client.delete(gateway_id='rtb-gw-12345678')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.delete_responder_gateway_response.DeleteResponderGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.delete_responder_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.delete_responder_gateway.async_delete_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.delete_responder_gateway_request.DeleteResponderGatewayRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def associate_certificate(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        client_token: str,
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse":
        """<p>Associates an ACM certificate with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to associate.</p>
            client_token: <p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>

        Examples:
            Associate a certificate with a responder gateway
            Associate an ACM certificate with a responder gateway

            >>> await client.associate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012', client_token='550e8400-e29b-41d4-a716-446655440000')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.associate_certificate_response.AssociateCertificateResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.associate_certificate

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.associate_certificate.async_associate_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.associate_certificate_request.AssociateCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
        input_["acm_certificate_arn"] = acm_certificate_arn
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disassociate_certificate(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse":
        """<p>Removes a certificate association from a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate to disassociate.</p>

        Examples:
            Disassociate a certificate from a responder gateway
            Remove an ACM certificate association from a responder gateway

            >>> await client.disassociate_certificate(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.disassociate_certificate_response.DisassociateCertificateResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.disassociate_certificate

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.disassociate_certificate.async_disassociate_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.disassociate_certificate_request.DisassociateCertificateRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
        input_["acm_certificate_arn"] = acm_certificate_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_certificate_association(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        acm_certificate_arn: "aws_sdk_rtbfabric.types.acm_certificate_arn.AcmCertificateArn",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
    ) -> "aws_sdk_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse":
        """<p>Retrieves the details of a certificate association with a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            acm_certificate_arn: <p>The Amazon Resource Name (ARN) of the ACM certificate.</p>

        Examples:
            Get certificate association details from a responder gateway
            Retrieve details of an ACM certificate association with a responder gateway

            >>> await client.get_certificate_association(gateway_id='rtb-gw-12345678', acm_certificate_arn='arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.get_certificate_association_response.GetCertificateAssociationResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.get_certificate_association

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.get_certificate_association.async_get_certificate_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.get_certificate_association_request.GetCertificateAssociationRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
        input_["acm_certificate_arn"] = acm_certificate_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_certificate_associations(
        self,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse":
        """<p>Lists the certificate associations for a responder gateway.</p>

        Args:
            gateway_id: <p>The unique identifier of the gateway.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>
            max_results: <p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>

        Examples:
            List certificate associations for a responder gateway
            Retrieve all certificate associations for a responder gateway

            >>> await client.list_certificate_associations(gateway_id='rtb-gw-12345678', max_results=5)
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.list_certificate_associations_response.ListCertificateAssociationsResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.list_certificate_associations

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.list_certificate_associations.async_list_certificate_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.list_certificate_associations_request.ListCertificateAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["gateway_id"] = gateway_id
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

    async def update_responder_gateway(
        self,
        port: int,
        protocol: "aws_sdk_rtbfabric.types.protocol.Protocol",
        client_token: str,
        gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId",
        *,
        config_overrides: Optional[AsyncRTBFabricClientConfig] = None,
        domain_name: Optional["aws_sdk_rtbfabric.types.domain_name.DomainName"] = None,
        listener_config: Optional[
            "aws_sdk_rtbfabric.types.listener_config.ListenerConfig"
        ] = None,
        trust_store_configuration: Optional[
            "aws_sdk_rtbfabric.types.trust_store_configuration.TrustStoreConfiguration"
        ] = None,
        managed_endpoint_configuration: Optional[
            "aws_sdk_rtbfabric.types.managed_endpoint_configuration.ManagedEndpointConfiguration"
        ] = None,
        description: Optional[str] = None,
    ) -> "aws_sdk_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse":
        """<p>Updates a responder gateway.</p>

        Args:
            domain_name: <p>The domain name for the responder gateway.</p>
            port: <p>The networking port to use.</p>
            protocol: <p>The networking protocol to use.</p>
            listener_config: <p>The listener configuration for the responder gateway.</p>
            trust_store_configuration: <p>The configuration of the trust store.</p>
            managed_endpoint_configuration: <p>The configuration for the managed endpoint.</p>
            client_token: <p>The unique client token.</p>
            gateway_id: <p>The unique identifier of the gateway.</p>
            description: <p>An optional description for the responder gateway.</p>

        Examples:
            Update responder gateway
            Update responder gateway

            >>> await client.update_responder_gateway(gateway_id='rtb-gw-12345678', description='Updated responder gateway description', port=8080, protocol='HTTP', client_token='12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rtbfabric.types.update_responder_gateway_response.UpdateResponderGatewayResponse"
        ]:
            import aws_sdk_rtbfabric._operations.rtb_fabric.update_responder_gateway

            (
                output,
                http_response,
            ) = await aws_sdk_rtbfabric._operations.rtb_fabric.update_responder_gateway.async_update_responder_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_rtbfabric.types.update_responder_gateway_request.UpdateResponderGatewayRequest = {}  # type: ignore[typeddict-item]
        if domain_name is not None:
            input_["domain_name"] = domain_name
        input_["port"] = port
        input_["protocol"] = protocol
        if listener_config is not None:
            input_["listener_config"] = listener_config
        if trust_store_configuration is not None:
            input_["trust_store_configuration"] = trust_store_configuration
        if managed_endpoint_configuration is not None:
            input_["managed_endpoint_configuration"] = managed_endpoint_configuration
        input_["client_token"] = client_token
        input_["gateway_id"] = gateway_id
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
