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
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.create_dns_view_input
    import aws_sdk_route53globalresolver.types.create_dns_view_output
    import aws_sdk_route53globalresolver.types.delete_dns_view_input
    import aws_sdk_route53globalresolver.types.delete_dns_view_output
    import aws_sdk_route53globalresolver.types.disable_dns_view_input
    import aws_sdk_route53globalresolver.types.disable_dns_view_output
    import aws_sdk_route53globalresolver.types.dns_sec_validation_type
    import aws_sdk_route53globalresolver.types.dns_view_summary
    import aws_sdk_route53globalresolver.types.edns_client_subnet_type
    import aws_sdk_route53globalresolver.types.enable_dns_view_input
    import aws_sdk_route53globalresolver.types.enable_dns_view_output
    import aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type
    import aws_sdk_route53globalresolver.types.get_dns_view_input
    import aws_sdk_route53globalresolver.types.get_dns_view_output
    import aws_sdk_route53globalresolver.types.list_dns_views_input
    import aws_sdk_route53globalresolver.types.list_dns_views_output
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name
    import aws_sdk_route53globalresolver.types.tags
    import aws_sdk_route53globalresolver.types.update_dns_view_input
    import aws_sdk_route53globalresolver.types.update_dns_view_output
    from aws_sdk_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from aws_sdk_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class DNSView:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "aws_sdk_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        dnssec_validation: Optional[
            "aws_sdk_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
        ] = None,
        edns_client_subnet: Optional[
            "aws_sdk_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
        ] = None,
        firewall_rules_fail_open: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["aws_sdk_route53globalresolver.types.tags.Tags"] = None,
    ) -> (
        "aws_sdk_route53globalresolver.types.create_dns_view_output.CreateDNSViewOutput"
    ):
        """<p>Creates a DNS view within a Route 53 Global Resolver. A DNS view models end users, user groups, networks, and devices, and serves as a parent resource that holds configurations controlling access, authorization, DNS firewall rules, and forwarding rules.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The ID of the Route 53 Global Resolver to associate with this DNS view.</p>
            client_token: <p>A unique string that identifies the request and ensures idempotency.</p>
            name: <p>A descriptive name for the DNS view.</p>
            dnssec_validation: <p>Whether to enable DNSSEC validation for DNS queries in this DNS view. When enabled, the resolver verifies the authenticity and integrity of DNS responses from public name servers for DNSSEC-signed domains.</p>
            edns_client_subnet: <p>Whether to enable EDNS Client Subnet injection for DNS queries in this DNS view. When enabled, client subnet information is forwarded to provide more accurate geographic-based DNS responses.</p>
            firewall_rules_fail_open: <p>Determines the behavior when Route 53 Global Resolver cannot apply DNS firewall rules due to service impairment. When enabled, DNS queries are allowed through; when disabled, queries are blocked.</p>
            description: <p>An optional description for the DNS view.</p>
            tags: <p>Tags to associate with the DNS view.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.create_dns_view_input.CreateDNSViewInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.create_dns_view_output.CreateDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_dns_view

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_dns_view.create_dns_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.create_dns_view_input.CreateDNSViewInput = {}  # type: ignore[typeddict-item]
        input["global_resolver_id"] = global_resolver_id
        if client_token is not None:
            input["client_token"] = client_token
        input["name"] = name
        if dnssec_validation is not None:
            input["dnssec_validation"] = dnssec_validation
        if edns_client_subnet is not None:
            input["edns_client_subnet"] = edns_client_subnet
        if firewall_rules_fail_open is not None:
            input["firewall_rules_fail_open"] = firewall_rules_fail_open
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
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_dns_view_output.GetDNSViewOutput":
        """<p>Retrieves information about a DNS view.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The ID of the DNS view to retrieve information about.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.get_dns_view_input.GetDNSViewInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.get_dns_view_output.GetDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_dns_view

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_dns_view.get_dns_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.get_dns_view_input.GetDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dnssec_validation: Optional[
            "aws_sdk_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
        ] = None,
        edns_client_subnet: Optional[
            "aws_sdk_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
        ] = None,
        firewall_rules_fail_open: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
        ] = None,
    ) -> (
        "aws_sdk_route53globalresolver.types.update_dns_view_output.UpdateDNSViewOutput"
    ):
        """<p>Updates the configuration of a DNS view.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to update.</p>
            name: <p>The name of the DNS view.</p>
            description: <p>A description of the DNS view.</p>
            dnssec_validation: <p>Whether to enable DNSSEC validation for the DNS view.</p>
            edns_client_subnet: <p>Whether to enable EDNS Client Subnet injection for the DNS view.</p>
            firewall_rules_fail_open: <p>Whether firewall rules should fail open when they cannot be evaluated.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.update_dns_view_input.UpdateDNSViewInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.update_dns_view_output.UpdateDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_dns_view

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_dns_view.update_dns_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.update_dns_view_input.UpdateDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if dnssec_validation is not None:
            input["dnssec_validation"] = dnssec_validation
        if edns_client_subnet is not None:
            input["edns_client_subnet"] = edns_client_subnet
        if firewall_rules_fail_open is not None:
            input["firewall_rules_fail_open"] = firewall_rules_fail_open

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> (
        "aws_sdk_route53globalresolver.types.delete_dns_view_output.DeleteDNSViewOutput"
    ):
        """<p>Deletes a DNS view. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.delete_dns_view_input.DeleteDNSViewInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.delete_dns_view_output.DeleteDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_dns_view

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_dns_view.delete_dns_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.delete_dns_view_input.DeleteDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_dns_views_output.ListDNSViewsOutput":
        """<p>Lists all DNS views for a Route 53 Global Resolver with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            global_resolver_id: <p>The Global Resolver ID.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.list_dns_views_input.ListDNSViewsInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.list_dns_views_output.ListDNSViewsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_dns_views

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_dns_views.list_dns_views(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.list_dns_views_input.ListDNSViewsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["global_resolver_id"] = global_resolver_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disable_dns_view(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.disable_dns_view_output.DisableDNSViewOutput":
        """<p>Disables a DNS view, preventing it from serving DNS queries.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to disable.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.disable_dns_view_input.DisableDNSViewInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.disable_dns_view_output.DisableDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disable_dns_view

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disable_dns_view.disable_dns_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.disable_dns_view_input.DisableDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def enable_dns_view(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> (
        "aws_sdk_route53globalresolver.types.enable_dns_view_output.EnableDNSViewOutput"
    ):
        """<p>Enables a disabled DNS view, allowing it to serve DNS queries again.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to enable.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.enable_dns_view_input.EnableDNSViewInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.enable_dns_view_output.EnableDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.enable_dns_view

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.enable_dns_view.enable_dns_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.enable_dns_view_input.EnableDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncDNSView:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        client_token: Optional[
            "aws_sdk_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        dnssec_validation: Optional[
            "aws_sdk_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
        ] = None,
        edns_client_subnet: Optional[
            "aws_sdk_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
        ] = None,
        firewall_rules_fail_open: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["aws_sdk_route53globalresolver.types.tags.Tags"] = None,
    ) -> (
        "aws_sdk_route53globalresolver.types.create_dns_view_output.CreateDNSViewOutput"
    ):
        """<p>Creates a DNS view within a Route 53 Global Resolver. A DNS view models end users, user groups, networks, and devices, and serves as a parent resource that holds configurations controlling access, authorization, DNS firewall rules, and forwarding rules.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            global_resolver_id: <p>The ID of the Route 53 Global Resolver to associate with this DNS view.</p>
            client_token: <p>A unique string that identifies the request and ensures idempotency.</p>
            name: <p>A descriptive name for the DNS view.</p>
            dnssec_validation: <p>Whether to enable DNSSEC validation for DNS queries in this DNS view. When enabled, the resolver verifies the authenticity and integrity of DNS responses from public name servers for DNSSEC-signed domains.</p>
            edns_client_subnet: <p>Whether to enable EDNS Client Subnet injection for DNS queries in this DNS view. When enabled, client subnet information is forwarded to provide more accurate geographic-based DNS responses.</p>
            firewall_rules_fail_open: <p>Determines the behavior when Route 53 Global Resolver cannot apply DNS firewall rules due to service impairment. When enabled, DNS queries are allowed through; when disabled, queries are blocked.</p>
            description: <p>An optional description for the DNS view.</p>
            tags: <p>Tags to associate with the DNS view.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.create_dns_view_input.CreateDNSViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.create_dns_view_output.CreateDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_dns_view

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_dns_view.async_create_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.create_dns_view_input.CreateDNSViewInput = {}  # type: ignore[typeddict-item]
        input["global_resolver_id"] = global_resolver_id
        if client_token is not None:
            input["client_token"] = client_token
        input["name"] = name
        if dnssec_validation is not None:
            input["dnssec_validation"] = dnssec_validation
        if edns_client_subnet is not None:
            input["edns_client_subnet"] = edns_client_subnet
        if firewall_rules_fail_open is not None:
            input["firewall_rules_fail_open"] = firewall_rules_fail_open
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
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_dns_view_output.GetDNSViewOutput":
        """<p>Retrieves information about a DNS view.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The ID of the DNS view to retrieve information about.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.get_dns_view_input.GetDNSViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.get_dns_view_output.GetDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_dns_view

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_dns_view.async_get_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.get_dns_view_input.GetDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dnssec_validation: Optional[
            "aws_sdk_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
        ] = None,
        edns_client_subnet: Optional[
            "aws_sdk_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
        ] = None,
        firewall_rules_fail_open: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
        ] = None,
    ) -> (
        "aws_sdk_route53globalresolver.types.update_dns_view_output.UpdateDNSViewOutput"
    ):
        """<p>Updates the configuration of a DNS view.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to update.</p>
            name: <p>The name of the DNS view.</p>
            description: <p>A description of the DNS view.</p>
            dnssec_validation: <p>Whether to enable DNSSEC validation for the DNS view.</p>
            edns_client_subnet: <p>Whether to enable EDNS Client Subnet injection for the DNS view.</p>
            firewall_rules_fail_open: <p>Whether firewall rules should fail open when they cannot be evaluated.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.update_dns_view_input.UpdateDNSViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.update_dns_view_output.UpdateDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_dns_view

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_dns_view.async_update_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.update_dns_view_input.UpdateDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id
        if name is not None:
            input["name"] = name
        if description is not None:
            input["description"] = description
        if dnssec_validation is not None:
            input["dnssec_validation"] = dnssec_validation
        if edns_client_subnet is not None:
            input["edns_client_subnet"] = edns_client_subnet
        if firewall_rules_fail_open is not None:
            input["firewall_rules_fail_open"] = firewall_rules_fail_open

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> (
        "aws_sdk_route53globalresolver.types.delete_dns_view_output.DeleteDNSViewOutput"
    ):
        """<p>Deletes a DNS view. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.delete_dns_view_input.DeleteDNSViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.delete_dns_view_output.DeleteDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_dns_view

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_dns_view.async_delete_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.delete_dns_view_input.DeleteDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_dns_views_output.ListDNSViewsOutput":
        """<p>Lists all DNS views for a Route 53 Global Resolver with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            global_resolver_id: <p>The Global Resolver ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.list_dns_views_input.ListDNSViewsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.list_dns_views_output.ListDNSViewsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_dns_views

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_dns_views.async_list_dns_views(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.list_dns_views_input.ListDNSViewsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["global_resolver_id"] = global_resolver_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def disable_dns_view(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.disable_dns_view_output.DisableDNSViewOutput":
        """<p>Disables a DNS view, preventing it from serving DNS queries.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to disable.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.disable_dns_view_input.DisableDNSViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.disable_dns_view_output.DisableDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disable_dns_view

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.disable_dns_view.async_disable_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.disable_dns_view_input.DisableDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def enable_dns_view(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> (
        "aws_sdk_route53globalresolver.types.enable_dns_view_output.EnableDNSViewOutput"
    ):
        """<p>Enables a disabled DNS view, allowing it to serve DNS queries again.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            dns_view_id: <p>The unique identifier of the DNS view to enable.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.enable_dns_view_input.EnableDNSViewInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.enable_dns_view_output.EnableDNSViewOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.enable_dns_view

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.enable_dns_view.async_enable_dns_view(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.enable_dns_view_input.EnableDNSViewInput = {}  # type: ignore[typeddict-item]
        input["dns_view_id"] = dns_view_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
