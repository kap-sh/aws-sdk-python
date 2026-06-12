from typing import TYPE_CHECKING, Optional

import aws_sdk_route53globalresolver._auth._signers
import aws_sdk_route53globalresolver._auth._sigv4
from aws_sdk_route53globalresolver._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.access_sources_item
    import aws_sdk_route53globalresolver.types.cidr
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.create_access_source_input
    import aws_sdk_route53globalresolver.types.create_access_source_output
    import aws_sdk_route53globalresolver.types.delete_access_source_input
    import aws_sdk_route53globalresolver.types.delete_access_source_output
    import aws_sdk_route53globalresolver.types.dns_protocol
    import aws_sdk_route53globalresolver.types.filters
    import aws_sdk_route53globalresolver.types.get_access_source_input
    import aws_sdk_route53globalresolver.types.get_access_source_output
    import aws_sdk_route53globalresolver.types.ip_address_type
    import aws_sdk_route53globalresolver.types.list_access_sources_input
    import aws_sdk_route53globalresolver.types.list_access_sources_output
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name_short
    import aws_sdk_route53globalresolver.types.tags
    import aws_sdk_route53globalresolver.types.update_access_source_input
    import aws_sdk_route53globalresolver.types.update_access_source_output
    from aws_sdk_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from aws_sdk_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class AccessSource:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        cidr: "aws_sdk_route53globalresolver.types.cidr.Cidr",
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        protocol: "aws_sdk_route53globalresolver.types.dns_protocol.DnsProtocol",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "aws_sdk_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        tags: Optional["aws_sdk_route53globalresolver.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput":
        """<p>Creates an access source for a DNS view. Access sources define IP addresses or CIDR ranges that are allowed to send DNS queries to the Route 53 Global Resolver, along with the permitted DNS protocols.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            cidr: <p>The IP address or CIDR range that is allowed to send DNS queries to the Route 53 Global Resolver.</p>
            client_token: <p>A unique string that identifies the request and ensures idempotency.</p>
            ip_address_type: <p>The IP address type for this access source. Valid values are IPv4 and IPv6 (if the Route 53 Global Resolver supports dual-stack).</p>
            name: <p>A descriptive name for the access source.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this access source.</p>
            protocol: <p>The DNS protocol that is permitted for this access source. Valid values are Do53 (DNS over port 53), DoT (DNS over TLS), and DoH (DNS over HTTPS).</p>
            tags: <p>Tags to associate with the access source.</p>

        Examples:
            CreateAccessSource example

            >>> client.create(cidr='85.90.183.3/30', client_token='9fas9-9usdfa-xbi8-kco', dns_view_id='dnsv-123456789', ip_address_type='IPV4', name='My Access Source', protocol='DO53', tags={'Key1': 'Value1'})
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source.create_access_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput = {}  # type: ignore[typeddict-item]
        input["cidr"] = cidr
        if client_token is not None:
            input["client_token"] = client_token
        if ip_address_type is not None:
            input["ip_address_type"] = ip_address_type
        if name is not None:
            input["name"] = name
        input["dns_view_id"] = dns_view_id
        input["protocol"] = protocol
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
        access_source_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput":
        """<p>Retrieves information about an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to retrieve.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.get_access_source_input.GetAccessSourceInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source.get_access_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.get_access_source_input.GetAccessSourceInput = {}  # type: ignore[typeddict-item]
        input["access_source_id"] = access_source_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        access_source_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        cidr: Optional["aws_sdk_route53globalresolver.types.cidr.Cidr"] = None,
        ip_address_type: Optional[
            "aws_sdk_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        protocol: Optional[
            "aws_sdk_route53globalresolver.types.dns_protocol.DnsProtocol"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput":
        """<p>Updates the configuration of an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to update.</p>
            cidr: <p>The CIDR block for the access source.</p>
            ip_address_type: <p>The IP address type for the access source.</p>
            name: <p>The name of the access source.</p>
            protocol: <p>The protocol for the access source.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source.update_access_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput = {}  # type: ignore[typeddict-item]
        input["access_source_id"] = access_source_id
        if cidr is not None:
            input["cidr"] = cidr
        if ip_address_type is not None:
            input["ip_address_type"] = ip_address_type
        if name is not None:
            input["name"] = name
        if protocol is not None:
            input["protocol"] = protocol

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        access_source_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput":
        """<p>Deletes an access source. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source.delete_access_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput = {}  # type: ignore[typeddict-item]
        input["access_source_id"] = access_source_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["aws_sdk_route53globalresolver.types.filters.Filters"] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput":
        """<p>Lists all access sources with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            filters: <p>Values to filter the results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources.list_access_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncAccessSource:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        cidr: "aws_sdk_route53globalresolver.types.cidr.Cidr",
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        protocol: "aws_sdk_route53globalresolver.types.dns_protocol.DnsProtocol",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "aws_sdk_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        tags: Optional["aws_sdk_route53globalresolver.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput":
        """<p>Creates an access source for a DNS view. Access sources define IP addresses or CIDR ranges that are allowed to send DNS queries to the Route 53 Global Resolver, along with the permitted DNS protocols.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            cidr: <p>The IP address or CIDR range that is allowed to send DNS queries to the Route 53 Global Resolver.</p>
            client_token: <p>A unique string that identifies the request and ensures idempotency.</p>
            ip_address_type: <p>The IP address type for this access source. Valid values are IPv4 and IPv6 (if the Route 53 Global Resolver supports dual-stack).</p>
            name: <p>A descriptive name for the access source.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this access source.</p>
            protocol: <p>The DNS protocol that is permitted for this access source. Valid values are Do53 (DNS over port 53), DoT (DNS over TLS), and DoH (DNS over HTTPS).</p>
            tags: <p>Tags to associate with the access source.</p>

        Examples:
            CreateAccessSource example

            >>> await client.create(cidr='85.90.183.3/30', client_token='9fas9-9usdfa-xbi8-kco', dns_view_id='dnsv-123456789', ip_address_type='IPV4', name='My Access Source', protocol='DO53', tags={'Key1': 'Value1'})
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.create_access_source_output.CreateAccessSourceOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_access_source.async_create_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.create_access_source_input.CreateAccessSourceInput = {}  # type: ignore[typeddict-item]
        input["cidr"] = cidr
        if client_token is not None:
            input["client_token"] = client_token
        if ip_address_type is not None:
            input["ip_address_type"] = ip_address_type
        if name is not None:
            input["name"] = name
        input["dns_view_id"] = dns_view_id
        input["protocol"] = protocol
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
        access_source_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput":
        """<p>Retrieves information about an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.get_access_source_input.GetAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.get_access_source_output.GetAccessSourceOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_access_source.async_get_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.get_access_source_input.GetAccessSourceInput = {}  # type: ignore[typeddict-item]
        input["access_source_id"] = access_source_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        access_source_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        cidr: Optional["aws_sdk_route53globalresolver.types.cidr.Cidr"] = None,
        ip_address_type: Optional[
            "aws_sdk_route53globalresolver.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name_short.ResourceNameShort"
        ] = None,
        protocol: Optional[
            "aws_sdk_route53globalresolver.types.dns_protocol.DnsProtocol"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput":
        """<p>Updates the configuration of an access source.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to update.</p>
            cidr: <p>The CIDR block for the access source.</p>
            ip_address_type: <p>The IP address type for the access source.</p>
            name: <p>The name of the access source.</p>
            protocol: <p>The protocol for the access source.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.update_access_source_output.UpdateAccessSourceOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_access_source.async_update_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.update_access_source_input.UpdateAccessSourceInput = {}  # type: ignore[typeddict-item]
        input["access_source_id"] = access_source_id
        if cidr is not None:
            input["cidr"] = cidr
        if ip_address_type is not None:
            input["ip_address_type"] = ip_address_type
        if name is not None:
            input["name"] = name
        if protocol is not None:
            input["protocol"] = protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        access_source_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput":
        """<p>Deletes an access source. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            access_source_id: <p>The unique identifier of the access source to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.delete_access_source_output.DeleteAccessSourceOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_access_source.async_delete_access_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.delete_access_source_input.DeleteAccessSourceInput = {}  # type: ignore[typeddict-item]
        input["access_source_id"] = access_source_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["aws_sdk_route53globalresolver.types.filters.Filters"] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput":
        """<p>Lists all access sources with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            filters: <p>Values to filter the results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.list_access_sources_output.ListAccessSourcesOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_access_sources.async_list_access_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.list_access_sources_input.ListAccessSourcesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if filters is not None:
            input["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
