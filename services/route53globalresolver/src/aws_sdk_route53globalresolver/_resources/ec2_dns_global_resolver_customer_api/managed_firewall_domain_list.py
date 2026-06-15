from __future__ import annotations

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
    import aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_input
    import aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_output
    import aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_input
    import aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_output
    import aws_sdk_route53globalresolver.types.managed_firewall_domain_lists_item
    import aws_sdk_route53globalresolver.types.resource_id
    from aws_sdk_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from aws_sdk_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class ManagedFirewallDomainList:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def read(
        self,
        managed_firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_output.GetManagedFirewallDomainListOutput":
        """<p>Retrieves information about an Amazon Web Services-managed firewall domain list. Managed domain lists contain domains associated with malicious activity, content categories, or specific threats.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            managed_firewall_domain_list_id: <p>ID of the Managed Domain List.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_input.GetManagedFirewallDomainListInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_output.GetManagedFirewallDomainListOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_managed_firewall_domain_list

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_managed_firewall_domain_list.get_managed_firewall_domain_list(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_input.GetManagedFirewallDomainListInput = {}  # type: ignore[typeddict-item]
        input_["managed_firewall_domain_list_id"] = managed_firewall_domain_list_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        managed_firewall_domain_list_type: str,
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_output.ListManagedFirewallDomainListsOutput":
        """<p>Returns a paginated list of the Amazon Web Services Managed DNS Lists and the categories for DNS Firewall. The categories are either <code>THREAT</code> or <code>CONTENT</code>.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            managed_firewall_domain_list_type: <p>The category of the Manage DNS list either <code>THREAT</code> or <code>CONTENT</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_input.ListManagedFirewallDomainListsInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_output.ListManagedFirewallDomainListsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_managed_firewall_domain_lists

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_managed_firewall_domain_lists.list_managed_firewall_domain_lists(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_input.ListManagedFirewallDomainListsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["managed_firewall_domain_list_type"] = managed_firewall_domain_list_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncManagedFirewallDomainList:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def read(
        self,
        managed_firewall_domain_list_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_output.GetManagedFirewallDomainListOutput":
        """<p>Retrieves information about an Amazon Web Services-managed firewall domain list. Managed domain lists contain domains associated with malicious activity, content categories, or specific threats.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            managed_firewall_domain_list_id: <p>ID of the Managed Domain List.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_input.GetManagedFirewallDomainListInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_output.GetManagedFirewallDomainListOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_managed_firewall_domain_list

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_managed_firewall_domain_list.async_get_managed_firewall_domain_list(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.get_managed_firewall_domain_list_input.GetManagedFirewallDomainListInput = {}  # type: ignore[typeddict-item]
        input_["managed_firewall_domain_list_id"] = managed_firewall_domain_list_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        managed_firewall_domain_list_type: str,
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_output.ListManagedFirewallDomainListsOutput":
        """<p>Returns a paginated list of the Amazon Web Services Managed DNS Lists and the categories for DNS Firewall. The categories are either <code>THREAT</code> or <code>CONTENT</code>.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            managed_firewall_domain_list_type: <p>The category of the Manage DNS list either <code>THREAT</code> or <code>CONTENT</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_input.ListManagedFirewallDomainListsInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_output.ListManagedFirewallDomainListsOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_managed_firewall_domain_lists

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_managed_firewall_domain_lists.async_list_managed_firewall_domain_lists(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.list_managed_firewall_domain_lists_input.ListManagedFirewallDomainListsInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["managed_firewall_domain_list_type"] = managed_firewall_domain_list_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
