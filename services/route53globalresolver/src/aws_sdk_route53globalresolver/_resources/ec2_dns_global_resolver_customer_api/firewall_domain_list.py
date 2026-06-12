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
    import aws_sdk_route53globalresolver.types.create_firewall_domain_list_input
    import aws_sdk_route53globalresolver.types.create_firewall_domain_list_output
    import aws_sdk_route53globalresolver.types.delete_firewall_domain_list_input
    import aws_sdk_route53globalresolver.types.delete_firewall_domain_list_output
    import aws_sdk_route53globalresolver.types.domain
    import aws_sdk_route53globalresolver.types.domains
    import aws_sdk_route53globalresolver.types.firewall_domain_lists_item
    import aws_sdk_route53globalresolver.types.get_firewall_domain_list_input
    import aws_sdk_route53globalresolver.types.get_firewall_domain_list_output
    import aws_sdk_route53globalresolver.types.import_firewall_domains_input
    import aws_sdk_route53globalresolver.types.import_firewall_domains_output
    import aws_sdk_route53globalresolver.types.list_firewall_domain_lists_input
    import aws_sdk_route53globalresolver.types.list_firewall_domain_lists_output
    import aws_sdk_route53globalresolver.types.list_firewall_domains_input
    import aws_sdk_route53globalresolver.types.list_firewall_domains_output
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name
    import aws_sdk_route53globalresolver.types.tags
    import aws_sdk_route53globalresolver.types.update_firewall_domains_input
    import aws_sdk_route53globalresolver.types.update_firewall_domains_output
    from aws_sdk_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from aws_sdk_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class FirewallDomainList:
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
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["aws_sdk_route53globalresolver.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput":
        """<p>Creates a firewall domain list. Domain lists are reusable sets of domain specifications that you use in DNS firewall rules to allow, block, or alert on DNS queries to specific domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            global_resolver_id: <p>The ID of the Route 53 Global Resolver that the domain list will be associated with.</p>
            description: <p>An optional description for the firewall domain list.</p>
            name: <p>A descriptive name for the firewall domain list.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list.create_firewall_domain_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["global_resolver_id"] = global_resolver_id
        if description is not None:
            input["description"] = description
        input["name"] = name
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
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput":
        """<p>Retrieves information about a firewall domain list.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>ID of the domain list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list.get_firewall_domain_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput = {}  # type: ignore[typeddict-item]
        input["firewall_domain_list_id"] = firewall_domain_list_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput":
        """<p>Deletes a firewall domain list. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>The unique identifier of the firewall domain list to delete.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list.delete_firewall_domain_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput = {}  # type: ignore[typeddict-item]
        input["firewall_domain_list_id"] = firewall_domain_list_id

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
        global_resolver_id: Optional[
            "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput":
        """<p>Lists all firewall domain lists for a Route 53 Global Resolver with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            global_resolver_id: <p>The ID of the Global Resolver that contains the DNS view the domain lists are associated to.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists.list_firewall_domain_lists(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if global_resolver_id is not None:
            input["global_resolver_id"] = global_resolver_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def import_firewall_domains(
        self,
        domain_file_url: str,
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput":
        """<p>Imports a list of domains from an Amazon S3 file into a firewall domain list. The file should contain one domain per line.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domain_file_url: <p>The fully qualified URL of the file in Amazon S3 that contains the list of domains to import. The file should contain one domain per line.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list that you want to import the domain list to.</p>
            operation: <p>This value is <code>REPLACE</code>, and it updates the domain list to match the list of domains in the imported file.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains.import_firewall_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput = {}  # type: ignore[typeddict-item]
        input["domain_file_url"] = domain_file_url
        input["firewall_domain_list_id"] = firewall_domain_list_id
        input["operation"] = operation

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_firewall_domains(
        self,
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput":
        """<p>Lists all the domains in DNS Firewall domain list you have created.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains.list_firewall_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["firewall_domain_list_id"] = firewall_domain_list_id

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_firewall_domains(
        self,
        domains: "aws_sdk_route53globalresolver.types.domains.Domains",
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput":
        """<p>Updates a DNS Firewall domain list from an array of specified domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domains: <p>A list of the domains. You can add up to 1000 domains per request.</p>
            firewall_domain_list_id: <p>The ID of the DNS Firewall domain list to which you want to add the domains.</p>
            operation: <p>The operation for updating the domain list. The allowed values are ADD, REMOVE, and REPLACE.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains.update_firewall_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput = {}  # type: ignore[typeddict-item]
        input["domains"] = domains
        input["firewall_domain_list_id"] = firewall_domain_list_id
        input["operation"] = operation

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncFirewallDomainList:
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
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["aws_sdk_route53globalresolver.types.tags.Tags"] = None,
    ) -> "aws_sdk_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput":
        """<p>Creates a firewall domain list. Domain lists are reusable sets of domain specifications that you use in DNS firewall rules to allow, block, or alert on DNS queries to specific domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            global_resolver_id: <p>The ID of the Route 53 Global Resolver that the domain list will be associated with.</p>
            description: <p>An optional description for the firewall domain list.</p>
            name: <p>A descriptive name for the firewall domain list.</p>
            tags: <p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.create_firewall_domain_list_output.CreateFirewallDomainListOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_domain_list.async_create_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.create_firewall_domain_list_input.CreateFirewallDomainListInput = {}  # type: ignore[typeddict-item]
        if client_token is not None:
            input["client_token"] = client_token
        input["global_resolver_id"] = global_resolver_id
        if description is not None:
            input["description"] = description
        input["name"] = name
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
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput":
        """<p>Retrieves information about a firewall domain list.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>ID of the domain list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.get_firewall_domain_list_output.GetFirewallDomainListOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_domain_list.async_get_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.get_firewall_domain_list_input.GetFirewallDomainListInput = {}  # type: ignore[typeddict-item]
        input["firewall_domain_list_id"] = firewall_domain_list_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput":
        """<p>Deletes a firewall domain list. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_domain_list_id: <p>The unique identifier of the firewall domain list to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.delete_firewall_domain_list_output.DeleteFirewallDomainListOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_domain_list.async_delete_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.delete_firewall_domain_list_input.DeleteFirewallDomainListInput = {}  # type: ignore[typeddict-item]
        input["firewall_domain_list_id"] = firewall_domain_list_id

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
        global_resolver_id: Optional[
            "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput":
        """<p>Lists all firewall domain lists for a Route 53 Global Resolver with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            global_resolver_id: <p>The ID of the Global Resolver that contains the DNS view the domain lists are associated to.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.list_firewall_domain_lists_output.ListFirewallDomainListsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domain_lists.async_list_firewall_domain_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.list_firewall_domain_lists_input.ListFirewallDomainListsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        if global_resolver_id is not None:
            input["global_resolver_id"] = global_resolver_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def import_firewall_domains(
        self,
        domain_file_url: str,
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput":
        """<p>Imports a list of domains from an Amazon S3 file into a firewall domain list. The file should contain one domain per line.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domain_file_url: <p>The fully qualified URL of the file in Amazon S3 that contains the list of domains to import. The file should contain one domain per line.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list that you want to import the domain list to.</p>
            operation: <p>This value is <code>REPLACE</code>, and it updates the domain list to match the list of domains in the imported file.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.import_firewall_domains_output.ImportFirewallDomainsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.import_firewall_domains.async_import_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.import_firewall_domains_input.ImportFirewallDomainsInput = {}  # type: ignore[typeddict-item]
        input["domain_file_url"] = domain_file_url
        input["firewall_domain_list_id"] = firewall_domain_list_id
        input["operation"] = operation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_firewall_domains(
        self,
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput":
        """<p>Lists all the domains in DNS Firewall domain list you have created.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            firewall_domain_list_id: <p>ID of the DNS Firewall domain list.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.list_firewall_domains_output.ListFirewallDomainsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_domains.async_list_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.list_firewall_domains_input.ListFirewallDomainsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token
        input["firewall_domain_list_id"] = firewall_domain_list_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_firewall_domains(
        self,
        domains: "aws_sdk_route53globalresolver.types.domains.Domains",
        firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        operation: str,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput":
        """<p>Updates a DNS Firewall domain list from an array of specified domains.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            domains: <p>A list of the domains. You can add up to 1000 domains per request.</p>
            firewall_domain_list_id: <p>The ID of the DNS Firewall domain list to which you want to add the domains.</p>
            operation: <p>The operation for updating the domain list. The allowed values are ADD, REMOVE, and REPLACE.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.update_firewall_domains_output.UpdateFirewallDomainsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_domains.async_update_firewall_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_route53globalresolver.types.update_firewall_domains_input.UpdateFirewallDomainsInput = {}  # type: ignore[typeddict-item]
        input["domains"] = domains
        input["firewall_domain_list_id"] = firewall_domain_list_id
        input["operation"] = operation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
