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
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input_items
    import aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_items
    import aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_items
    import aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output
    import aws_sdk_route53globalresolver.types.block_override_dns_query_type
    import aws_sdk_route53globalresolver.types.block_override_ttl
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.confidence_threshold
    import aws_sdk_route53globalresolver.types.create_firewall_rule_input
    import aws_sdk_route53globalresolver.types.create_firewall_rule_output
    import aws_sdk_route53globalresolver.types.delete_firewall_rule_input
    import aws_sdk_route53globalresolver.types.delete_firewall_rule_output
    import aws_sdk_route53globalresolver.types.dns_advanced_protection
    import aws_sdk_route53globalresolver.types.dns_query_type
    import aws_sdk_route53globalresolver.types.domain
    import aws_sdk_route53globalresolver.types.filters
    import aws_sdk_route53globalresolver.types.firewall_block_response
    import aws_sdk_route53globalresolver.types.firewall_rule_action
    import aws_sdk_route53globalresolver.types.firewall_rule_priority
    import aws_sdk_route53globalresolver.types.firewall_rules_item
    import aws_sdk_route53globalresolver.types.get_firewall_rule_input
    import aws_sdk_route53globalresolver.types.get_firewall_rule_output
    import aws_sdk_route53globalresolver.types.list_firewall_rules_input
    import aws_sdk_route53globalresolver.types.list_firewall_rules_output
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name
    import aws_sdk_route53globalresolver.types.update_firewall_rule_input
    import aws_sdk_route53globalresolver.types.update_firewall_rule_output
    from aws_sdk_route53globalresolver._services.async_route53_global_resolver import (
        AsyncRoute53GlobalResolverClient,
        AsyncRoute53GlobalResolverClientConfig,
    )
    from aws_sdk_route53globalresolver._services.route53_global_resolver import (
        Route53GlobalResolverClient,
        Route53GlobalResolverClientConfig,
    )


class FirewallRule:
    def __init__(self, service: Route53GlobalResolverClient) -> None:
        self._service = service

    def create(
        self,
        action: "aws_sdk_route53globalresolver.types.firewall_rule_action.FirewallRuleAction",
        name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName",
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        block_override_dns_type: Optional[
            "aws_sdk_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "aws_sdk_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "aws_sdk_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "aws_sdk_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        client_token: Optional[
            "aws_sdk_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        confidence_threshold: Optional[
            "aws_sdk_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "aws_sdk_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        firewall_domain_list_id: Optional[
            "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
        priority: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
        q_type: Optional[
            "aws_sdk_route53globalresolver.types.dns_query_type.DnsQueryType"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput":
        """<p>Creates a DNS firewall rule. Firewall rules define actions (ALLOW, BLOCK, or ALERT) to take on DNS queries that match specified domain lists, managed domain lists, or advanced threat protections.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through.</p> </li> <li> <p> <code>ALERT</code> - Permit the request and send metrics and logs to CloudWatch.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. This option requires additional details in the rule's <code>BlockResponse</code>.</p> </li> </ul>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_response: <p>The response to return when the action is BLOCK. Valid values are NXDOMAIN (domain does not exist), NODATA (domain exists but no records), or OVERRIDE (return custom response).</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for advanced threat detection. Valid values are HIGH, MEDIUM, or LOW, indicating the accuracy level required for threat detection.</p>
            description: <p>An optional description for the firewall rule.</p>
            dns_advanced_protection: <p>Whether to enable advanced DNS threat protection for this rule. Advanced protection can detect and block DNS tunneling and Domain Generation Algorithm (DGA) threats.</p>
            firewall_domain_list_id: <p>The ID of the firewall domain list to use in this rule.</p>
            name: <p>A descriptive name for the firewall rule.</p>
            priority: <p>The priority of this rule. Rules are evaluated in priority order, with lower numbers having higher priority. When a DNS query matches multiple rules, the rule with the highest priority (lowest number) is applied.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this firewall rule.</p>
            q_type: <p>The DNS query type to match for this rule. Examples include A (IPv4 address), AAAA (IPv6 address), MX (mail exchange), or TXT (text record).</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule.create_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["action"] = action
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        if client_token is not None:
            input_["client_token"] = client_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        if firewall_domain_list_id is not None:
            input_["firewall_domain_list_id"] = firewall_domain_list_id
        input_["name"] = name
        if priority is not None:
            input_["priority"] = priority
        input_["dns_view_id"] = dns_view_id
        if q_type is not None:
            input_["q_type"] = q_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput":
        """<p>Retrieves information about a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>ID of the DNS Firewall rule.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule.get_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rule_id"] = firewall_rule_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        client_token: "aws_sdk_route53globalresolver.types.client_token.ClientToken",
        firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        action: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
        ] = None,
        block_override_dns_type: Optional[
            "aws_sdk_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "aws_sdk_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "aws_sdk_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "aws_sdk_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        confidence_threshold: Optional[
            "aws_sdk_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "aws_sdk_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        priority: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput":
        """<p>Updates the configuration of a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule.</p>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_response: <p>The way that you want DNS Firewall to block the request. Used for the rule action setting <code>BLOCK</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.</p>
            description: <p>The description for the Firewall rule.</p>
            dns_advanced_protection: <p>The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS_TUNNELING, and DICTIONARY_DGA.</p>
            firewall_rule_id: <p>The ID of the DNS Firewall rule.</p>
            name: <p>The name of the DNS Firewall rule.</p>
            priority: <p>The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule.update_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput = {}  # type: ignore[typeddict-item]
        if action is not None:
            input_["action"] = action
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        input_["client_token"] = client_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        input_["firewall_rule_id"] = firewall_rule_id
        if name is not None:
            input_["name"] = name
        if priority is not None:
            input_["priority"] = priority

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput":
        """<p>Deletes a DNS firewall rule. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>The unique identifier of the firewall rule to delete.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule.delete_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rule_id"] = firewall_rule_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["aws_sdk_route53globalresolver.types.filters.Filters"] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput":
        """<p>Lists all DNS firewall rules for a DNS view with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            dns_view_id: <p>ID of the DNS view.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules.list_firewall_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["dns_view_id"] = dns_view_id
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_create_firewall_rule(
        self,
        firewall_rules: "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input_items.BatchCreateFirewallRuleInputItems",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput":
        """<p>Creates multiple DNS firewall rules in a single operation. This is more efficient than creating rules individually when you need to set up multiple rules at once.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The <code>BatchCreateFirewallRuleInputItem</code> objects contain the information for each Firewall rule.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule.batch_create_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rules"] = firewall_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_delete_firewall_rule(
        self,
        firewall_rules: "aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_items.BatchDeleteFirewallRuleInputItems",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput":
        """<p>Deletes multiple DNS firewall rules in a single operation. This is more efficient than deleting rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>An array of the DNS Firewall IDs to be deleted.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule.batch_delete_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rules"] = firewall_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_update_firewall_rule(
        self,
        firewall_rules: "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_items.BatchUpdateFirewallRuleInputItems",
        *,
        config_overrides: Optional[Route53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput":
        """<p>Updates multiple DNS firewall rules in a single operation. This is more efficient than updating rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The DNS Firewall rule IDs to be updated.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput]",
        ) -> OperationResponse[
            "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule

            output, http_response = (
                aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule.batch_update_firewall_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rules"] = firewall_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncFirewallRule:
    def __init__(self, service: AsyncRoute53GlobalResolverClient) -> None:
        self._service = service

    async def create(
        self,
        action: "aws_sdk_route53globalresolver.types.firewall_rule_action.FirewallRuleAction",
        name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName",
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        block_override_dns_type: Optional[
            "aws_sdk_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "aws_sdk_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "aws_sdk_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "aws_sdk_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        client_token: Optional[
            "aws_sdk_route53globalresolver.types.client_token.ClientToken"
        ] = None,
        confidence_threshold: Optional[
            "aws_sdk_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "aws_sdk_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        firewall_domain_list_id: Optional[
            "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
        ] = None,
        priority: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
        q_type: Optional[
            "aws_sdk_route53globalresolver.types.dns_query_type.DnsQueryType"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput":
        """<p>Creates a DNS firewall rule. Firewall rules define actions (ALLOW, BLOCK, or ALERT) to take on DNS queries that match specified domain lists, managed domain lists, or advanced threat protections.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through.</p> </li> <li> <p> <code>ALERT</code> - Permit the request and send metrics and logs to CloudWatch.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. This option requires additional details in the rule's <code>BlockResponse</code>.</p> </li> </ul>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p> <p>This setting is required if the <code>BlockResponse</code> setting is <code>OVERRIDE</code>.</p>
            block_response: <p>The response to return when the action is BLOCK. Valid values are NXDOMAIN (domain does not exist), NODATA (domain exists but no records), or OVERRIDE (return custom response).</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for advanced threat detection. Valid values are HIGH, MEDIUM, or LOW, indicating the accuracy level required for threat detection.</p>
            description: <p>An optional description for the firewall rule.</p>
            dns_advanced_protection: <p>Whether to enable advanced DNS threat protection for this rule. Advanced protection can detect and block DNS tunneling and Domain Generation Algorithm (DGA) threats.</p>
            firewall_domain_list_id: <p>The ID of the firewall domain list to use in this rule.</p>
            name: <p>A descriptive name for the firewall rule.</p>
            priority: <p>The priority of this rule. Rules are evaluated in priority order, with lower numbers having higher priority. When a DNS query matches multiple rules, the rule with the highest priority (lowest number) is applied.</p>
            dns_view_id: <p>The ID of the DNS view to associate with this firewall rule.</p>
            q_type: <p>The DNS query type to match for this rule. Examples include A (IPv4 address), AAAA (IPv6 address), MX (mail exchange), or TXT (text record).</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.create_firewall_rule_output.CreateFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.create_firewall_rule.async_create_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.create_firewall_rule_input.CreateFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["action"] = action
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        if client_token is not None:
            input_["client_token"] = client_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        if firewall_domain_list_id is not None:
            input_["firewall_domain_list_id"] = firewall_domain_list_id
        input_["name"] = name
        if priority is not None:
            input_["priority"] = priority
        input_["dns_view_id"] = dns_view_id
        if q_type is not None:
            input_["q_type"] = q_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput":
        """<p>Retrieves information about a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>ID of the DNS Firewall rule.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.get_firewall_rule_output.GetFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.get_firewall_rule.async_get_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.get_firewall_rule_input.GetFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rule_id"] = firewall_rule_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        client_token: "aws_sdk_route53globalresolver.types.client_token.ClientToken",
        firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        action: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
        ] = None,
        block_override_dns_type: Optional[
            "aws_sdk_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
        ] = None,
        block_override_domain: Optional[
            "aws_sdk_route53globalresolver.types.domain.Domain"
        ] = None,
        block_override_ttl: Optional[
            "aws_sdk_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
        ] = None,
        block_response: Optional[
            "aws_sdk_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
        ] = None,
        confidence_threshold: Optional[
            "aws_sdk_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
        ] = None,
        description: Optional[
            "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
        ] = None,
        dns_advanced_protection: Optional[
            "aws_sdk_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
        ] = None,
        name: Optional[
            "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
        ] = None,
        priority: Optional[
            "aws_sdk_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
        ] = None,
    ) -> "aws_sdk_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput":
        """<p>Updates the configuration of a DNS firewall rule.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            action: <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule.</p>
            block_override_dns_type: <p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_domain: <p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_override_ttl: <p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>
            block_response: <p>The way that you want DNS Firewall to block the request. Used for the rule action setting <code>BLOCK</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>
            confidence_threshold: <p>The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule.</p>
            description: <p>The description for the Firewall rule.</p>
            dns_advanced_protection: <p>The type of the DNS Firewall Advanced rule. Valid values are DGA, DNS_TUNNELING, and DICTIONARY_DGA.</p>
            firewall_rule_id: <p>The ID of the DNS Firewall rule.</p>
            name: <p>The name of the DNS Firewall rule.</p>
            priority: <p>The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed one or more service quotas. Check your current usage and quotas, then try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.update_firewall_rule_output.UpdateFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.update_firewall_rule.async_update_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.update_firewall_rule_input.UpdateFirewallRuleInput = {}  # type: ignore[typeddict-item]
        if action is not None:
            input_["action"] = action
        if block_override_dns_type is not None:
            input_["block_override_dns_type"] = block_override_dns_type
        if block_override_domain is not None:
            input_["block_override_domain"] = block_override_domain
        if block_override_ttl is not None:
            input_["block_override_ttl"] = block_override_ttl
        if block_response is not None:
            input_["block_response"] = block_response
        input_["client_token"] = client_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if description is not None:
            input_["description"] = description
        if dns_advanced_protection is not None:
            input_["dns_advanced_protection"] = dns_advanced_protection
        input_["firewall_rule_id"] = firewall_rule_id
        if name is not None:
            input_["name"] = name
        if priority is not None:
            input_["priority"] = priority

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        firewall_rule_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput":
        """<p>Deletes a DNS firewall rule. This operation cannot be undone.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rule_id: <p>The unique identifier of the firewall rule to delete.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.delete_firewall_rule_output.DeleteFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.delete_firewall_rule.async_delete_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.delete_firewall_rule_input.DeleteFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rule_id"] = firewall_rule_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional["aws_sdk_route53globalresolver.types.filters.Filters"] = None,
    ) -> "aws_sdk_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput":
        """<p>Lists all DNS firewall rules for a DNS view with pagination support.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            max_results: <p>The maximum number of results to retrieve in a single call.</p>
            next_token: <p>A pagination token used for large sets of results that can't be returned in a single response.</p>
            dns_view_id: <p>ID of the DNS view.</p>
            filters: <p>Values to filter the results.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify the resource ID and try again.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.list_firewall_rules_output.ListFirewallRulesOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.list_firewall_rules.async_list_firewall_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.list_firewall_rules_input.ListFirewallRulesInput = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["dns_view_id"] = dns_view_id
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_create_firewall_rule(
        self,
        firewall_rules: "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input_items.BatchCreateFirewallRuleInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput":
        """<p>Creates multiple DNS firewall rules in a single operation. This is more efficient than creating rules individually when you need to set up multiple rules at once.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The <code>BatchCreateFirewallRuleInputItem</code> objects contain the information for each Firewall rule.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.batch_create_firewall_rule_output.BatchCreateFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_create_firewall_rule.async_batch_create_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.batch_create_firewall_rule_input.BatchCreateFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rules"] = firewall_rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_delete_firewall_rule(
        self,
        firewall_rules: "aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input_items.BatchDeleteFirewallRuleInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput":
        """<p>Deletes multiple DNS firewall rules in a single operation. This is more efficient than deleting rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>An array of the DNS Firewall IDs to be deleted.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_output.BatchDeleteFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_delete_firewall_rule.async_batch_delete_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.batch_delete_firewall_rule_input.BatchDeleteFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rules"] = firewall_rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def batch_update_firewall_rule(
        self,
        firewall_rules: "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input_items.BatchUpdateFirewallRuleInputItems",
        *,
        config_overrides: Optional[AsyncRoute53GlobalResolverClientConfig] = None,
    ) -> "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput":
        """<p>Updates multiple DNS firewall rules in a single operation. This is more efficient than updating rules individually.</p> <important> <p>Route 53 Global Resolver is a global service that supports resolvers in multiple Amazon Web Services Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify <code>--region us-east-2</code> on Amazon Web Services CLI commands.</p> </important>

        Args:
            firewall_rules: <p>The DNS Firewall rule IDs to be updated.</p>

        Raises:
            aws_sdk_route53globalresolver.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check your IAM permissions and try again.</p>
            aws_sdk_route53globalresolver.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Try again later.</p>
            aws_sdk_route53globalresolver.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Wait a moment and try again.</p>
            aws_sdk_route53globalresolver.errors.validation_exception.ValidationException: <p>The input parameters are invalid. Check the parameter values and try again.</p>
            aws_sdk_route53globalresolver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput]",
        ) -> AsyncOperationResponse[
            "aws_sdk_route53globalresolver.types.batch_update_firewall_rule_output.BatchUpdateFirewallRuleOutput"
        ]:
            import aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule

            (
                output,
                http_response,
            ) = await aws_sdk_route53globalresolver._operations.ec2_dns_global_resolver_customer_api.batch_update_firewall_rule.async_batch_update_firewall_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_route53globalresolver.types.batch_update_firewall_rule_input.BatchUpdateFirewallRuleInput = {}  # type: ignore[typeddict-item]
        input_["firewall_rules"] = firewall_rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
