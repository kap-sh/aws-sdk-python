"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.analysis_component
    import capo_ec2.types.analysis_component_list
    import capo_ec2.types.rule_group_rule_options_pair_list
    import capo_ec2.types.rule_group_type_pair_list
    import capo_ec2.types.rule_option_list
    import capo_ec2.types.string


class AdditionalDetail(TypedDict, closed=True):
    additional_detail_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The additional detail code.</p>"""
    component: NotRequired["capo_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The path component.</p>"""
    vpc_endpoint_service: NotRequired[
        "capo_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The VPC endpoint service.</p>"""
    rule_options: NotRequired["capo_ec2.types.rule_option_list.RuleOptionList"]
    """<p>The rule options.</p>"""
    rule_group_type_pairs: NotRequired[
        "capo_ec2.types.rule_group_type_pair_list.RuleGroupTypePairList"
    ]
    """<p>The rule group type.</p>"""
    rule_group_rule_options_pairs: NotRequired[
        "capo_ec2.types.rule_group_rule_options_pair_list.RuleGroupRuleOptionsPairList"
    ]
    """<p>The rule options.</p>"""
    service_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the VPC endpoint service.</p>"""
    load_balancers: NotRequired[
        "capo_ec2.types.analysis_component_list.AnalysisComponentList"
    ]
    """<p>The load balancers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AdditionalDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "additional_detail_type" in value:
        pairs.append(
            (f"{key_prefix}AdditionalDetailType", str(value["additional_detail_type"]))
        )
    if "component" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["component"], pairs, f"{key_prefix}Component"
        )
    if "vpc_endpoint_service" in value:
        import capo_ec2.types.analysis_component

        capo_ec2.types.analysis_component.serialize_ec2_query(
            value["vpc_endpoint_service"], pairs, f"{key_prefix}VpcEndpointService"
        )
    if "rule_options" in value:
        import capo_ec2.types.rule_option_list

        capo_ec2.types.rule_option_list.serialize_ec2_query(
            value["rule_options"], pairs, f"{key_prefix}RuleOptionSet"
        )
    if "rule_group_type_pairs" in value:
        import capo_ec2.types.rule_group_type_pair_list

        capo_ec2.types.rule_group_type_pair_list.serialize_ec2_query(
            value["rule_group_type_pairs"], pairs, f"{key_prefix}RuleGroupTypePairSet"
        )
    if "rule_group_rule_options_pairs" in value:
        import capo_ec2.types.rule_group_rule_options_pair_list

        capo_ec2.types.rule_group_rule_options_pair_list.serialize_ec2_query(
            value["rule_group_rule_options_pairs"],
            pairs,
            f"{key_prefix}RuleGroupRuleOptionsPairSet",
        )
    if "service_name" in value:
        pairs.append((f"{key_prefix}ServiceName", str(value["service_name"])))
    if "load_balancers" in value:
        import capo_ec2.types.analysis_component_list

        capo_ec2.types.analysis_component_list.serialize_ec2_query(
            value["load_balancers"], pairs, f"{key_prefix}LoadBalancerSet"
        )


def deserialize_ec2_query(el: Element) -> AdditionalDetail:
    out: AdditionalDetail = {}  # type: ignore[typeddict-item]
    child_additional_detail_type = el.find("additionalDetailType")
    if child_additional_detail_type is not None:
        out["additional_detail_type"] = str(child_additional_detail_type.text or "")
    child_component = el.find("component")
    if child_component is not None:
        import capo_ec2.types.analysis_component

        out["component"] = capo_ec2.types.analysis_component.deserialize_ec2_query(
            child_component
        )
    child_vpc_endpoint_service = el.find("vpcEndpointService")
    if child_vpc_endpoint_service is not None:
        import capo_ec2.types.analysis_component

        out["vpc_endpoint_service"] = (
            capo_ec2.types.analysis_component.deserialize_ec2_query(
                child_vpc_endpoint_service
            )
        )
    if el.find("ruleOptionSet") is not None:
        import capo_ec2.types.rule_option_list

        out["rule_options"] = capo_ec2.types.rule_option_list.deserialize_ec2_query(
            el, "ruleOptionSet"
        )
    if el.find("ruleGroupTypePairSet") is not None:
        import capo_ec2.types.rule_group_type_pair_list

        out["rule_group_type_pairs"] = (
            capo_ec2.types.rule_group_type_pair_list.deserialize_ec2_query(
                el, "ruleGroupTypePairSet"
            )
        )
    if el.find("ruleGroupRuleOptionsPairSet") is not None:
        import capo_ec2.types.rule_group_rule_options_pair_list

        out["rule_group_rule_options_pairs"] = (
            capo_ec2.types.rule_group_rule_options_pair_list.deserialize_ec2_query(
                el, "ruleGroupRuleOptionsPairSet"
            )
        )
    child_service_name = el.find("serviceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    if el.find("loadBalancerSet") is not None:
        import capo_ec2.types.analysis_component_list

        out["load_balancers"] = (
            capo_ec2.types.analysis_component_list.deserialize_ec2_query(
                el, "loadBalancerSet"
            )
        )
    return out
