"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.analysis_component
    import aws_sdk_ec2.types.analysis_component_list
    import aws_sdk_ec2.types.rule_group_rule_options_pair_list
    import aws_sdk_ec2.types.rule_group_type_pair_list
    import aws_sdk_ec2.types.rule_option_list
    import aws_sdk_ec2.types.string


class AdditionalDetail(TypedDict):
    additional_detail_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The additional detail code.</p>"""
    component: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>The path component.</p>"""
    vpc_endpoint_service: NotRequired[
        "aws_sdk_ec2.types.analysis_component.AnalysisComponent"
    ]
    """<p>The VPC endpoint service.</p>"""
    rule_options: NotRequired["aws_sdk_ec2.types.rule_option_list.RuleOptionList"]
    """<p>The rule options.</p>"""
    rule_group_type_pairs: NotRequired[
        "aws_sdk_ec2.types.rule_group_type_pair_list.RuleGroupTypePairList"
    ]
    """<p>The rule group type.</p>"""
    rule_group_rule_options_pairs: NotRequired[
        "aws_sdk_ec2.types.rule_group_rule_options_pair_list.RuleGroupRuleOptionsPairList"
    ]
    """<p>The rule options.</p>"""
    service_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the VPC endpoint service.</p>"""
    load_balancers: NotRequired[
        "aws_sdk_ec2.types.analysis_component_list.AnalysisComponentList"
    ]
    """<p>The load balancers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AdditionalDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "additional_detail_type" in value:
        pairs.append(
            (f"{prefix}.AdditionalDetailType", str(value["additional_detail_type"]))
        )
    if "component" in value:
        import aws_sdk_ec2.types.analysis_component

        aws_sdk_ec2.types.analysis_component.serialize_ec2_query(
            value["component"], pairs, f"{prefix}.Component"
        )
    if "vpc_endpoint_service" in value:
        import aws_sdk_ec2.types.analysis_component

        aws_sdk_ec2.types.analysis_component.serialize_ec2_query(
            value["vpc_endpoint_service"], pairs, f"{prefix}.VpcEndpointService"
        )
    if "rule_options" in value:
        import aws_sdk_ec2.types.rule_option_list

        aws_sdk_ec2.types.rule_option_list.serialize_ec2_query(
            value["rule_options"], pairs, f"{prefix}.RuleOptionSet"
        )
    if "rule_group_type_pairs" in value:
        import aws_sdk_ec2.types.rule_group_type_pair_list

        aws_sdk_ec2.types.rule_group_type_pair_list.serialize_ec2_query(
            value["rule_group_type_pairs"], pairs, f"{prefix}.RuleGroupTypePairSet"
        )
    if "rule_group_rule_options_pairs" in value:
        import aws_sdk_ec2.types.rule_group_rule_options_pair_list

        aws_sdk_ec2.types.rule_group_rule_options_pair_list.serialize_ec2_query(
            value["rule_group_rule_options_pairs"],
            pairs,
            f"{prefix}.RuleGroupRuleOptionsPairSet",
        )
    if "service_name" in value:
        pairs.append((f"{prefix}.ServiceName", str(value["service_name"])))
    if "load_balancers" in value:
        import aws_sdk_ec2.types.analysis_component_list

        aws_sdk_ec2.types.analysis_component_list.serialize_ec2_query(
            value["load_balancers"], pairs, f"{prefix}.LoadBalancerSet"
        )


def deserialize_ec2_query(el: Element) -> AdditionalDetail:
    out: AdditionalDetail = {}  # type: ignore[typeddict-item]
    child_additional_detail_type = el.find("AdditionalDetailType")
    if child_additional_detail_type is not None:
        out["additional_detail_type"] = str(child_additional_detail_type.text or "")
    child_component = el.find("Component")
    if child_component is not None:
        import aws_sdk_ec2.types.analysis_component

        out["component"] = aws_sdk_ec2.types.analysis_component.deserialize_ec2_query(
            child_component
        )
    child_vpc_endpoint_service = el.find("VpcEndpointService")
    if child_vpc_endpoint_service is not None:
        import aws_sdk_ec2.types.analysis_component

        out["vpc_endpoint_service"] = (
            aws_sdk_ec2.types.analysis_component.deserialize_ec2_query(
                child_vpc_endpoint_service
            )
        )
    if el.find("RuleOptionSet") is not None:
        import aws_sdk_ec2.types.rule_option_list

        out["rule_options"] = aws_sdk_ec2.types.rule_option_list.deserialize_ec2_query(
            el, "RuleOptionSet"
        )
    if el.find("RuleGroupTypePairSet") is not None:
        import aws_sdk_ec2.types.rule_group_type_pair_list

        out["rule_group_type_pairs"] = (
            aws_sdk_ec2.types.rule_group_type_pair_list.deserialize_ec2_query(
                el, "RuleGroupTypePairSet"
            )
        )
    if el.find("RuleGroupRuleOptionsPairSet") is not None:
        import aws_sdk_ec2.types.rule_group_rule_options_pair_list

        out["rule_group_rule_options_pairs"] = (
            aws_sdk_ec2.types.rule_group_rule_options_pair_list.deserialize_ec2_query(
                el, "RuleGroupRuleOptionsPairSet"
            )
        )
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    if el.find("LoadBalancerSet") is not None:
        import aws_sdk_ec2.types.analysis_component_list

        out["load_balancers"] = (
            aws_sdk_ec2.types.analysis_component_list.deserialize_ec2_query(
                el, "LoadBalancerSet"
            )
        )
    return out
