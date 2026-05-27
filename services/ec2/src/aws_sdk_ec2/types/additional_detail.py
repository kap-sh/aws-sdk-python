"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
