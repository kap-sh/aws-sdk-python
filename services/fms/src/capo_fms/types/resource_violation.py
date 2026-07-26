"""Generated from Smithy shape ``com.amazonaws.fms#ResourceViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_ec2_instance_violation
    import capo_fms.types.aws_ec2_network_interface_violation
    import capo_fms.types.aws_vpc_security_group_violation
    import capo_fms.types.dns_duplicate_rule_group_violation
    import capo_fms.types.dns_rule_group_limit_exceeded_violation
    import capo_fms.types.dns_rule_group_priority_conflict_violation
    import capo_fms.types.firewall_subnet_is_out_of_scope_violation
    import capo_fms.types.firewall_subnet_missing_vpc_endpoint_violation
    import capo_fms.types.invalid_network_acl_entries_violation
    import capo_fms.types.network_firewall_black_hole_route_detected_violation
    import capo_fms.types.network_firewall_internet_traffic_not_inspected_violation
    import capo_fms.types.network_firewall_invalid_route_configuration_violation
    import capo_fms.types.network_firewall_missing_expected_routes_violation
    import capo_fms.types.network_firewall_missing_expected_rt_violation
    import capo_fms.types.network_firewall_missing_firewall_violation
    import capo_fms.types.network_firewall_missing_subnet_violation
    import capo_fms.types.network_firewall_policy_modified_violation
    import capo_fms.types.network_firewall_unexpected_firewall_routes_violation
    import capo_fms.types.network_firewall_unexpected_gateway_routes_violation
    import capo_fms.types.possible_remediation_actions
    import capo_fms.types.route_has_out_of_scope_endpoint_violation
    import capo_fms.types.third_party_firewall_missing_expected_route_table_violation
    import capo_fms.types.third_party_firewall_missing_firewall_violation
    import capo_fms.types.third_party_firewall_missing_subnet_violation
    import capo_fms.types.web_acl_has_incompatible_configuration_violation
    import capo_fms.types.web_acl_has_out_of_scope_resources_violation


class ResourceViolation(TypedDict, closed=True):
    aws_vpc_security_group_violation: NotRequired[
        "capo_fms.types.aws_vpc_security_group_violation.AwsVPCSecurityGroupViolation"
    ]
    """<p>Violation detail for security groups.</p>"""
    aws_ec2_network_interface_violation: NotRequired[
        "capo_fms.types.aws_ec2_network_interface_violation.AwsEc2NetworkInterfaceViolation"
    ]
    """<p>Violation detail for a network interface.</p>"""
    aws_ec2_instance_violation: NotRequired[
        "capo_fms.types.aws_ec2_instance_violation.AwsEc2InstanceViolation"
    ]
    """<p>Violation detail for an EC2 instance.</p>"""
    network_firewall_missing_firewall_violation: NotRequired[
        "capo_fms.types.network_firewall_missing_firewall_violation.NetworkFirewallMissingFirewallViolation"
    ]
    """<p>Violation detail for an Network Firewall policy that indicates that a subnet has no Firewall Manager managed firewall in its VPC. </p>"""
    network_firewall_missing_subnet_violation: NotRequired[
        "capo_fms.types.network_firewall_missing_subnet_violation.NetworkFirewallMissingSubnetViolation"
    ]
    """<p>Violation detail for an Network Firewall policy that indicates that an Availability Zone is missing the expected Firewall Manager managed subnet.</p>"""
    network_firewall_missing_expected_rt_violation: NotRequired[
        "capo_fms.types.network_firewall_missing_expected_rt_violation.NetworkFirewallMissingExpectedRTViolation"
    ]
    """<p>Violation detail for an Network Firewall policy that indicates that a subnet is not associated with the expected Firewall Manager managed route table. </p>"""
    network_firewall_policy_modified_violation: NotRequired[
        "capo_fms.types.network_firewall_policy_modified_violation.NetworkFirewallPolicyModifiedViolation"
    ]
    """<p>Violation detail for an Network Firewall policy that indicates that a firewall policy in an individual account has been modified in a way that makes it noncompliant. For example, the individual account owner might have deleted a rule group, changed the priority of a stateless rule group, or changed a policy default action.</p>"""
    network_firewall_internet_traffic_not_inspected_violation: NotRequired[
        "capo_fms.types.network_firewall_internet_traffic_not_inspected_violation.NetworkFirewallInternetTrafficNotInspectedViolation"
    ]
    """<p>Violation detail for the subnet for which internet traffic hasn't been inspected.</p>"""
    network_firewall_invalid_route_configuration_violation: NotRequired[
        "capo_fms.types.network_firewall_invalid_route_configuration_violation.NetworkFirewallInvalidRouteConfigurationViolation"
    ]
    """<p>The route configuration is invalid.</p>"""
    network_firewall_black_hole_route_detected_violation: NotRequired[
        "capo_fms.types.network_firewall_black_hole_route_detected_violation.NetworkFirewallBlackHoleRouteDetectedViolation"
    ]
    network_firewall_unexpected_firewall_routes_violation: NotRequired[
        "capo_fms.types.network_firewall_unexpected_firewall_routes_violation.NetworkFirewallUnexpectedFirewallRoutesViolation"
    ]
    """<p>There's an unexpected firewall route.</p>"""
    network_firewall_unexpected_gateway_routes_violation: NotRequired[
        "capo_fms.types.network_firewall_unexpected_gateway_routes_violation.NetworkFirewallUnexpectedGatewayRoutesViolation"
    ]
    """<p>There's an unexpected gateway route.</p>"""
    network_firewall_missing_expected_routes_violation: NotRequired[
        "capo_fms.types.network_firewall_missing_expected_routes_violation.NetworkFirewallMissingExpectedRoutesViolation"
    ]
    """<p>Expected routes are missing from Network Firewall.</p>"""
    dns_rule_group_priority_conflict_violation: NotRequired[
        "capo_fms.types.dns_rule_group_priority_conflict_violation.DnsRuleGroupPriorityConflictViolation"
    ]
    """<p>Violation detail for a DNS Firewall policy that indicates that a rule group that Firewall Manager tried to associate with a VPC has the same priority as a rule group that's already associated. </p>"""
    dns_duplicate_rule_group_violation: NotRequired[
        "capo_fms.types.dns_duplicate_rule_group_violation.DnsDuplicateRuleGroupViolation"
    ]
    """<p>Violation detail for a DNS Firewall policy that indicates that a rule group that Firewall Manager tried to associate with a VPC is already associated with the VPC and can't be associated again. </p>"""
    dns_rule_group_limit_exceeded_violation: NotRequired[
        "capo_fms.types.dns_rule_group_limit_exceeded_violation.DnsRuleGroupLimitExceededViolation"
    ]
    """<p>Violation detail for a DNS Firewall policy that indicates that the VPC reached the limit for associated DNS Firewall rule groups. Firewall Manager tried to associate another rule group with the VPC and failed. </p>"""
    firewall_subnet_is_out_of_scope_violation: NotRequired[
        "capo_fms.types.firewall_subnet_is_out_of_scope_violation.FirewallSubnetIsOutOfScopeViolation"
    ]
    """<p>Contains details about the firewall subnet that violates the policy scope.</p>"""
    route_has_out_of_scope_endpoint_violation: NotRequired[
        "capo_fms.types.route_has_out_of_scope_endpoint_violation.RouteHasOutOfScopeEndpointViolation"
    ]
    """<p>Contains details about the route endpoint that violates the policy scope.</p>"""
    third_party_firewall_missing_firewall_violation: NotRequired[
        "capo_fms.types.third_party_firewall_missing_firewall_violation.ThirdPartyFirewallMissingFirewallViolation"
    ]
    """<p>The violation details for a third-party firewall that's been deleted.</p>"""
    third_party_firewall_missing_subnet_violation: NotRequired[
        "capo_fms.types.third_party_firewall_missing_subnet_violation.ThirdPartyFirewallMissingSubnetViolation"
    ]
    """<p>The violation details for a third-party firewall's subnet that's been deleted.</p>"""
    third_party_firewall_missing_expected_route_table_violation: NotRequired[
        "capo_fms.types.third_party_firewall_missing_expected_route_table_violation.ThirdPartyFirewallMissingExpectedRouteTableViolation"
    ]
    """<p>The violation details for a third-party firewall that has the Firewall Manager managed route table that was associated with the third-party firewall has been deleted.</p>"""
    firewall_subnet_missing_vpc_endpoint_violation: NotRequired[
        "capo_fms.types.firewall_subnet_missing_vpc_endpoint_violation.FirewallSubnetMissingVPCEndpointViolation"
    ]
    """<p>The violation details for a third-party firewall's VPC endpoint subnet that was deleted.</p>"""
    invalid_network_acl_entries_violation: NotRequired[
        "capo_fms.types.invalid_network_acl_entries_violation.InvalidNetworkAclEntriesViolation"
    ]
    """<p>Violation detail for the entries in a network ACL resource.</p>"""
    possible_remediation_actions: NotRequired[
        "capo_fms.types.possible_remediation_actions.PossibleRemediationActions"
    ]
    """<p>A list of possible remediation action lists. Each individual possible remediation action is a list of individual remediation actions.</p>"""
    web_acl_has_incompatible_configuration_violation: NotRequired[
        "capo_fms.types.web_acl_has_incompatible_configuration_violation.WebACLHasIncompatibleConfigurationViolation"
    ]
    """<p>The violation details for a web ACL whose configuration is incompatible with the Firewall Manager policy. </p>"""
    web_acl_has_out_of_scope_resources_violation: NotRequired[
        "capo_fms.types.web_acl_has_out_of_scope_resources_violation.WebACLHasOutOfScopeResourcesViolation"
    ]
    """<p>The violation details for a web ACL that's associated with at least one resource that's out of scope of the Firewall Manager policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceViolation) -> dict:
    out: dict = {}
    if "aws_vpc_security_group_violation" in value:
        import capo_fms.types.aws_vpc_security_group_violation

        out["AwsVPCSecurityGroupViolation"] = (
            capo_fms.types.aws_vpc_security_group_violation.serialize_aws_json_1_1(
                value["aws_vpc_security_group_violation"]
            )
        )
    if "aws_ec2_network_interface_violation" in value:
        import capo_fms.types.aws_ec2_network_interface_violation

        out["AwsEc2NetworkInterfaceViolation"] = (
            capo_fms.types.aws_ec2_network_interface_violation.serialize_aws_json_1_1(
                value["aws_ec2_network_interface_violation"]
            )
        )
    if "aws_ec2_instance_violation" in value:
        import capo_fms.types.aws_ec2_instance_violation

        out["AwsEc2InstanceViolation"] = (
            capo_fms.types.aws_ec2_instance_violation.serialize_aws_json_1_1(
                value["aws_ec2_instance_violation"]
            )
        )
    if "network_firewall_missing_firewall_violation" in value:
        import capo_fms.types.network_firewall_missing_firewall_violation

        out["NetworkFirewallMissingFirewallViolation"] = (
            capo_fms.types.network_firewall_missing_firewall_violation.serialize_aws_json_1_1(
                value["network_firewall_missing_firewall_violation"]
            )
        )
    if "network_firewall_missing_subnet_violation" in value:
        import capo_fms.types.network_firewall_missing_subnet_violation

        out["NetworkFirewallMissingSubnetViolation"] = (
            capo_fms.types.network_firewall_missing_subnet_violation.serialize_aws_json_1_1(
                value["network_firewall_missing_subnet_violation"]
            )
        )
    if "network_firewall_missing_expected_rt_violation" in value:
        import capo_fms.types.network_firewall_missing_expected_rt_violation

        out["NetworkFirewallMissingExpectedRTViolation"] = (
            capo_fms.types.network_firewall_missing_expected_rt_violation.serialize_aws_json_1_1(
                value["network_firewall_missing_expected_rt_violation"]
            )
        )
    if "network_firewall_policy_modified_violation" in value:
        import capo_fms.types.network_firewall_policy_modified_violation

        out["NetworkFirewallPolicyModifiedViolation"] = (
            capo_fms.types.network_firewall_policy_modified_violation.serialize_aws_json_1_1(
                value["network_firewall_policy_modified_violation"]
            )
        )
    if "network_firewall_internet_traffic_not_inspected_violation" in value:
        import capo_fms.types.network_firewall_internet_traffic_not_inspected_violation

        out["NetworkFirewallInternetTrafficNotInspectedViolation"] = (
            capo_fms.types.network_firewall_internet_traffic_not_inspected_violation.serialize_aws_json_1_1(
                value["network_firewall_internet_traffic_not_inspected_violation"]
            )
        )
    if "network_firewall_invalid_route_configuration_violation" in value:
        import capo_fms.types.network_firewall_invalid_route_configuration_violation

        out["NetworkFirewallInvalidRouteConfigurationViolation"] = (
            capo_fms.types.network_firewall_invalid_route_configuration_violation.serialize_aws_json_1_1(
                value["network_firewall_invalid_route_configuration_violation"]
            )
        )
    if "network_firewall_black_hole_route_detected_violation" in value:
        import capo_fms.types.network_firewall_black_hole_route_detected_violation

        out["NetworkFirewallBlackHoleRouteDetectedViolation"] = (
            capo_fms.types.network_firewall_black_hole_route_detected_violation.serialize_aws_json_1_1(
                value["network_firewall_black_hole_route_detected_violation"]
            )
        )
    if "network_firewall_unexpected_firewall_routes_violation" in value:
        import capo_fms.types.network_firewall_unexpected_firewall_routes_violation

        out["NetworkFirewallUnexpectedFirewallRoutesViolation"] = (
            capo_fms.types.network_firewall_unexpected_firewall_routes_violation.serialize_aws_json_1_1(
                value["network_firewall_unexpected_firewall_routes_violation"]
            )
        )
    if "network_firewall_unexpected_gateway_routes_violation" in value:
        import capo_fms.types.network_firewall_unexpected_gateway_routes_violation

        out["NetworkFirewallUnexpectedGatewayRoutesViolation"] = (
            capo_fms.types.network_firewall_unexpected_gateway_routes_violation.serialize_aws_json_1_1(
                value["network_firewall_unexpected_gateway_routes_violation"]
            )
        )
    if "network_firewall_missing_expected_routes_violation" in value:
        import capo_fms.types.network_firewall_missing_expected_routes_violation

        out["NetworkFirewallMissingExpectedRoutesViolation"] = (
            capo_fms.types.network_firewall_missing_expected_routes_violation.serialize_aws_json_1_1(
                value["network_firewall_missing_expected_routes_violation"]
            )
        )
    if "dns_rule_group_priority_conflict_violation" in value:
        import capo_fms.types.dns_rule_group_priority_conflict_violation

        out["DnsRuleGroupPriorityConflictViolation"] = (
            capo_fms.types.dns_rule_group_priority_conflict_violation.serialize_aws_json_1_1(
                value["dns_rule_group_priority_conflict_violation"]
            )
        )
    if "dns_duplicate_rule_group_violation" in value:
        import capo_fms.types.dns_duplicate_rule_group_violation

        out["DnsDuplicateRuleGroupViolation"] = (
            capo_fms.types.dns_duplicate_rule_group_violation.serialize_aws_json_1_1(
                value["dns_duplicate_rule_group_violation"]
            )
        )
    if "dns_rule_group_limit_exceeded_violation" in value:
        import capo_fms.types.dns_rule_group_limit_exceeded_violation

        out["DnsRuleGroupLimitExceededViolation"] = (
            capo_fms.types.dns_rule_group_limit_exceeded_violation.serialize_aws_json_1_1(
                value["dns_rule_group_limit_exceeded_violation"]
            )
        )
    if "firewall_subnet_is_out_of_scope_violation" in value:
        import capo_fms.types.firewall_subnet_is_out_of_scope_violation

        out["FirewallSubnetIsOutOfScopeViolation"] = (
            capo_fms.types.firewall_subnet_is_out_of_scope_violation.serialize_aws_json_1_1(
                value["firewall_subnet_is_out_of_scope_violation"]
            )
        )
    if "route_has_out_of_scope_endpoint_violation" in value:
        import capo_fms.types.route_has_out_of_scope_endpoint_violation

        out["RouteHasOutOfScopeEndpointViolation"] = (
            capo_fms.types.route_has_out_of_scope_endpoint_violation.serialize_aws_json_1_1(
                value["route_has_out_of_scope_endpoint_violation"]
            )
        )
    if "third_party_firewall_missing_firewall_violation" in value:
        import capo_fms.types.third_party_firewall_missing_firewall_violation

        out["ThirdPartyFirewallMissingFirewallViolation"] = (
            capo_fms.types.third_party_firewall_missing_firewall_violation.serialize_aws_json_1_1(
                value["third_party_firewall_missing_firewall_violation"]
            )
        )
    if "third_party_firewall_missing_subnet_violation" in value:
        import capo_fms.types.third_party_firewall_missing_subnet_violation

        out["ThirdPartyFirewallMissingSubnetViolation"] = (
            capo_fms.types.third_party_firewall_missing_subnet_violation.serialize_aws_json_1_1(
                value["third_party_firewall_missing_subnet_violation"]
            )
        )
    if "third_party_firewall_missing_expected_route_table_violation" in value:
        import capo_fms.types.third_party_firewall_missing_expected_route_table_violation

        out["ThirdPartyFirewallMissingExpectedRouteTableViolation"] = (
            capo_fms.types.third_party_firewall_missing_expected_route_table_violation.serialize_aws_json_1_1(
                value["third_party_firewall_missing_expected_route_table_violation"]
            )
        )
    if "firewall_subnet_missing_vpc_endpoint_violation" in value:
        import capo_fms.types.firewall_subnet_missing_vpc_endpoint_violation

        out["FirewallSubnetMissingVPCEndpointViolation"] = (
            capo_fms.types.firewall_subnet_missing_vpc_endpoint_violation.serialize_aws_json_1_1(
                value["firewall_subnet_missing_vpc_endpoint_violation"]
            )
        )
    if "invalid_network_acl_entries_violation" in value:
        import capo_fms.types.invalid_network_acl_entries_violation

        out["InvalidNetworkAclEntriesViolation"] = (
            capo_fms.types.invalid_network_acl_entries_violation.serialize_aws_json_1_1(
                value["invalid_network_acl_entries_violation"]
            )
        )
    if "possible_remediation_actions" in value:
        import capo_fms.types.possible_remediation_actions

        out["PossibleRemediationActions"] = (
            capo_fms.types.possible_remediation_actions.serialize_aws_json_1_1(
                value["possible_remediation_actions"]
            )
        )
    if "web_acl_has_incompatible_configuration_violation" in value:
        import capo_fms.types.web_acl_has_incompatible_configuration_violation

        out["WebACLHasIncompatibleConfigurationViolation"] = (
            capo_fms.types.web_acl_has_incompatible_configuration_violation.serialize_aws_json_1_1(
                value["web_acl_has_incompatible_configuration_violation"]
            )
        )
    if "web_acl_has_out_of_scope_resources_violation" in value:
        import capo_fms.types.web_acl_has_out_of_scope_resources_violation

        out["WebACLHasOutOfScopeResourcesViolation"] = (
            capo_fms.types.web_acl_has_out_of_scope_resources_violation.serialize_aws_json_1_1(
                value["web_acl_has_out_of_scope_resources_violation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceViolation:
    out: ResourceViolation = {}  # type: ignore[typeddict-item]
    if "AwsVPCSecurityGroupViolation" in data:
        import capo_fms.types.aws_vpc_security_group_violation

        out["aws_vpc_security_group_violation"] = (
            capo_fms.types.aws_vpc_security_group_violation.deserialize_aws_json_1_1(
                data["AwsVPCSecurityGroupViolation"]
            )
        )
    if "AwsEc2NetworkInterfaceViolation" in data:
        import capo_fms.types.aws_ec2_network_interface_violation

        out["aws_ec2_network_interface_violation"] = (
            capo_fms.types.aws_ec2_network_interface_violation.deserialize_aws_json_1_1(
                data["AwsEc2NetworkInterfaceViolation"]
            )
        )
    if "AwsEc2InstanceViolation" in data:
        import capo_fms.types.aws_ec2_instance_violation

        out["aws_ec2_instance_violation"] = (
            capo_fms.types.aws_ec2_instance_violation.deserialize_aws_json_1_1(
                data["AwsEc2InstanceViolation"]
            )
        )
    if "NetworkFirewallMissingFirewallViolation" in data:
        import capo_fms.types.network_firewall_missing_firewall_violation

        out["network_firewall_missing_firewall_violation"] = (
            capo_fms.types.network_firewall_missing_firewall_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallMissingFirewallViolation"]
            )
        )
    if "NetworkFirewallMissingSubnetViolation" in data:
        import capo_fms.types.network_firewall_missing_subnet_violation

        out["network_firewall_missing_subnet_violation"] = (
            capo_fms.types.network_firewall_missing_subnet_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallMissingSubnetViolation"]
            )
        )
    if "NetworkFirewallMissingExpectedRTViolation" in data:
        import capo_fms.types.network_firewall_missing_expected_rt_violation

        out["network_firewall_missing_expected_rt_violation"] = (
            capo_fms.types.network_firewall_missing_expected_rt_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallMissingExpectedRTViolation"]
            )
        )
    if "NetworkFirewallPolicyModifiedViolation" in data:
        import capo_fms.types.network_firewall_policy_modified_violation

        out["network_firewall_policy_modified_violation"] = (
            capo_fms.types.network_firewall_policy_modified_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallPolicyModifiedViolation"]
            )
        )
    if "NetworkFirewallInternetTrafficNotInspectedViolation" in data:
        import capo_fms.types.network_firewall_internet_traffic_not_inspected_violation

        out["network_firewall_internet_traffic_not_inspected_violation"] = (
            capo_fms.types.network_firewall_internet_traffic_not_inspected_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallInternetTrafficNotInspectedViolation"]
            )
        )
    if "NetworkFirewallInvalidRouteConfigurationViolation" in data:
        import capo_fms.types.network_firewall_invalid_route_configuration_violation

        out["network_firewall_invalid_route_configuration_violation"] = (
            capo_fms.types.network_firewall_invalid_route_configuration_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallInvalidRouteConfigurationViolation"]
            )
        )
    if "NetworkFirewallBlackHoleRouteDetectedViolation" in data:
        import capo_fms.types.network_firewall_black_hole_route_detected_violation

        out["network_firewall_black_hole_route_detected_violation"] = (
            capo_fms.types.network_firewall_black_hole_route_detected_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallBlackHoleRouteDetectedViolation"]
            )
        )
    if "NetworkFirewallUnexpectedFirewallRoutesViolation" in data:
        import capo_fms.types.network_firewall_unexpected_firewall_routes_violation

        out["network_firewall_unexpected_firewall_routes_violation"] = (
            capo_fms.types.network_firewall_unexpected_firewall_routes_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallUnexpectedFirewallRoutesViolation"]
            )
        )
    if "NetworkFirewallUnexpectedGatewayRoutesViolation" in data:
        import capo_fms.types.network_firewall_unexpected_gateway_routes_violation

        out["network_firewall_unexpected_gateway_routes_violation"] = (
            capo_fms.types.network_firewall_unexpected_gateway_routes_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallUnexpectedGatewayRoutesViolation"]
            )
        )
    if "NetworkFirewallMissingExpectedRoutesViolation" in data:
        import capo_fms.types.network_firewall_missing_expected_routes_violation

        out["network_firewall_missing_expected_routes_violation"] = (
            capo_fms.types.network_firewall_missing_expected_routes_violation.deserialize_aws_json_1_1(
                data["NetworkFirewallMissingExpectedRoutesViolation"]
            )
        )
    if "DnsRuleGroupPriorityConflictViolation" in data:
        import capo_fms.types.dns_rule_group_priority_conflict_violation

        out["dns_rule_group_priority_conflict_violation"] = (
            capo_fms.types.dns_rule_group_priority_conflict_violation.deserialize_aws_json_1_1(
                data["DnsRuleGroupPriorityConflictViolation"]
            )
        )
    if "DnsDuplicateRuleGroupViolation" in data:
        import capo_fms.types.dns_duplicate_rule_group_violation

        out["dns_duplicate_rule_group_violation"] = (
            capo_fms.types.dns_duplicate_rule_group_violation.deserialize_aws_json_1_1(
                data["DnsDuplicateRuleGroupViolation"]
            )
        )
    if "DnsRuleGroupLimitExceededViolation" in data:
        import capo_fms.types.dns_rule_group_limit_exceeded_violation

        out["dns_rule_group_limit_exceeded_violation"] = (
            capo_fms.types.dns_rule_group_limit_exceeded_violation.deserialize_aws_json_1_1(
                data["DnsRuleGroupLimitExceededViolation"]
            )
        )
    if "FirewallSubnetIsOutOfScopeViolation" in data:
        import capo_fms.types.firewall_subnet_is_out_of_scope_violation

        out["firewall_subnet_is_out_of_scope_violation"] = (
            capo_fms.types.firewall_subnet_is_out_of_scope_violation.deserialize_aws_json_1_1(
                data["FirewallSubnetIsOutOfScopeViolation"]
            )
        )
    if "RouteHasOutOfScopeEndpointViolation" in data:
        import capo_fms.types.route_has_out_of_scope_endpoint_violation

        out["route_has_out_of_scope_endpoint_violation"] = (
            capo_fms.types.route_has_out_of_scope_endpoint_violation.deserialize_aws_json_1_1(
                data["RouteHasOutOfScopeEndpointViolation"]
            )
        )
    if "ThirdPartyFirewallMissingFirewallViolation" in data:
        import capo_fms.types.third_party_firewall_missing_firewall_violation

        out["third_party_firewall_missing_firewall_violation"] = (
            capo_fms.types.third_party_firewall_missing_firewall_violation.deserialize_aws_json_1_1(
                data["ThirdPartyFirewallMissingFirewallViolation"]
            )
        )
    if "ThirdPartyFirewallMissingSubnetViolation" in data:
        import capo_fms.types.third_party_firewall_missing_subnet_violation

        out["third_party_firewall_missing_subnet_violation"] = (
            capo_fms.types.third_party_firewall_missing_subnet_violation.deserialize_aws_json_1_1(
                data["ThirdPartyFirewallMissingSubnetViolation"]
            )
        )
    if "ThirdPartyFirewallMissingExpectedRouteTableViolation" in data:
        import capo_fms.types.third_party_firewall_missing_expected_route_table_violation

        out["third_party_firewall_missing_expected_route_table_violation"] = (
            capo_fms.types.third_party_firewall_missing_expected_route_table_violation.deserialize_aws_json_1_1(
                data["ThirdPartyFirewallMissingExpectedRouteTableViolation"]
            )
        )
    if "FirewallSubnetMissingVPCEndpointViolation" in data:
        import capo_fms.types.firewall_subnet_missing_vpc_endpoint_violation

        out["firewall_subnet_missing_vpc_endpoint_violation"] = (
            capo_fms.types.firewall_subnet_missing_vpc_endpoint_violation.deserialize_aws_json_1_1(
                data["FirewallSubnetMissingVPCEndpointViolation"]
            )
        )
    if "InvalidNetworkAclEntriesViolation" in data:
        import capo_fms.types.invalid_network_acl_entries_violation

        out["invalid_network_acl_entries_violation"] = (
            capo_fms.types.invalid_network_acl_entries_violation.deserialize_aws_json_1_1(
                data["InvalidNetworkAclEntriesViolation"]
            )
        )
    if "PossibleRemediationActions" in data:
        import capo_fms.types.possible_remediation_actions

        out["possible_remediation_actions"] = (
            capo_fms.types.possible_remediation_actions.deserialize_aws_json_1_1(
                data["PossibleRemediationActions"]
            )
        )
    if "WebACLHasIncompatibleConfigurationViolation" in data:
        import capo_fms.types.web_acl_has_incompatible_configuration_violation

        out["web_acl_has_incompatible_configuration_violation"] = (
            capo_fms.types.web_acl_has_incompatible_configuration_violation.deserialize_aws_json_1_1(
                data["WebACLHasIncompatibleConfigurationViolation"]
            )
        )
    if "WebACLHasOutOfScopeResourcesViolation" in data:
        import capo_fms.types.web_acl_has_out_of_scope_resources_violation

        out["web_acl_has_out_of_scope_resources_violation"] = (
            capo_fms.types.web_acl_has_out_of_scope_resources_violation.deserialize_aws_json_1_1(
                data["WebACLHasOutOfScopeResourcesViolation"]
            )
        )
    return out
