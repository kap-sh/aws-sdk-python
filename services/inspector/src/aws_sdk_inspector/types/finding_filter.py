"""Generated from Smithy shape ``com.amazonaws.inspector#FindingFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_id_list
    import aws_sdk_inspector.types.attribute_list
    import aws_sdk_inspector.types.auto_scaling_group_list
    import aws_sdk_inspector.types.filter_rules_package_arn_list
    import aws_sdk_inspector.types.rule_name_list
    import aws_sdk_inspector.types.severity_list
    import aws_sdk_inspector.types.timestamp_range


class FindingFilter(TypedDict, closed=True):
    agent_ids: NotRequired["aws_sdk_inspector.types.agent_id_list.AgentIdList"]
    """<p>For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the <b>agentId</b> property of the <a>Finding</a> data type.</p>"""
    auto_scaling_groups: NotRequired[
        "aws_sdk_inspector.types.auto_scaling_group_list.AutoScalingGroupList"
    ]
    """<p>For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the <b>autoScalingGroup</b> property of the <a>Finding</a> data type.</p>"""
    rule_names: NotRequired["aws_sdk_inspector.types.rule_name_list.RuleNameList"]
    """<p>For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the <b>ruleName</b> property of the <a>Finding</a> data type.</p>"""
    severities: NotRequired["aws_sdk_inspector.types.severity_list.SeverityList"]
    """<p>For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the <b>severity</b> property of the <a>Finding</a> data type.</p>"""
    rules_package_arns: NotRequired[
        "aws_sdk_inspector.types.filter_rules_package_arn_list.FilterRulesPackageArnList"
    ]
    """<p>For a record to match a filter, one of the values that is specified for this data type property must be the exact match of the value of the <b>rulesPackageArn</b> property of the <a>Finding</a> data type.</p>"""
    attributes: NotRequired["aws_sdk_inspector.types.attribute_list.AttributeList"]
    """<p>For a record to match a filter, the list of values that are specified for this data type property must be contained in the list of values of the <b>attributes</b> property of the <a>Finding</a> data type.</p>"""
    user_attributes: NotRequired["aws_sdk_inspector.types.attribute_list.AttributeList"]
    """<p>For a record to match a filter, the value that is specified for this data type property must be contained in the list of values of the <b>userAttributes</b> property of the <a>Finding</a> data type.</p>"""
    creation_time_range: NotRequired[
        "aws_sdk_inspector.types.timestamp_range.TimestampRange"
    ]
    """<p>The time range during which the finding is generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FindingFilter) -> dict:
    out: dict = {}
    if "agent_ids" in value:
        import aws_sdk_inspector.types.agent_id_list

        out["agentIds"] = aws_sdk_inspector.types.agent_id_list.serialize_aws_json_1_1(
            value["agent_ids"]
        )
    if "auto_scaling_groups" in value:
        import aws_sdk_inspector.types.auto_scaling_group_list

        out["autoScalingGroups"] = (
            aws_sdk_inspector.types.auto_scaling_group_list.serialize_aws_json_1_1(
                value["auto_scaling_groups"]
            )
        )
    if "rule_names" in value:
        import aws_sdk_inspector.types.rule_name_list

        out["ruleNames"] = (
            aws_sdk_inspector.types.rule_name_list.serialize_aws_json_1_1(
                value["rule_names"]
            )
        )
    if "severities" in value:
        import aws_sdk_inspector.types.severity_list

        out["severities"] = (
            aws_sdk_inspector.types.severity_list.serialize_aws_json_1_1(
                value["severities"]
            )
        )
    if "rules_package_arns" in value:
        import aws_sdk_inspector.types.filter_rules_package_arn_list

        out["rulesPackageArns"] = (
            aws_sdk_inspector.types.filter_rules_package_arn_list.serialize_aws_json_1_1(
                value["rules_package_arns"]
            )
        )
    if "attributes" in value:
        import aws_sdk_inspector.types.attribute_list

        out["attributes"] = (
            aws_sdk_inspector.types.attribute_list.serialize_aws_json_1_1(
                value["attributes"]
            )
        )
    if "user_attributes" in value:
        import aws_sdk_inspector.types.attribute_list

        out["userAttributes"] = (
            aws_sdk_inspector.types.attribute_list.serialize_aws_json_1_1(
                value["user_attributes"]
            )
        )
    if "creation_time_range" in value:
        import aws_sdk_inspector.types.timestamp_range

        out["creationTimeRange"] = (
            aws_sdk_inspector.types.timestamp_range.serialize_aws_json_1_1(
                value["creation_time_range"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FindingFilter:
    out: FindingFilter = {}  # type: ignore[typeddict-item]
    if "agentIds" in data:
        import aws_sdk_inspector.types.agent_id_list

        out["agent_ids"] = (
            aws_sdk_inspector.types.agent_id_list.deserialize_aws_json_1_1(
                data["agentIds"]
            )
        )
    if "autoScalingGroups" in data:
        import aws_sdk_inspector.types.auto_scaling_group_list

        out["auto_scaling_groups"] = (
            aws_sdk_inspector.types.auto_scaling_group_list.deserialize_aws_json_1_1(
                data["autoScalingGroups"]
            )
        )
    if "ruleNames" in data:
        import aws_sdk_inspector.types.rule_name_list

        out["rule_names"] = (
            aws_sdk_inspector.types.rule_name_list.deserialize_aws_json_1_1(
                data["ruleNames"]
            )
        )
    if "severities" in data:
        import aws_sdk_inspector.types.severity_list

        out["severities"] = (
            aws_sdk_inspector.types.severity_list.deserialize_aws_json_1_1(
                data["severities"]
            )
        )
    if "rulesPackageArns" in data:
        import aws_sdk_inspector.types.filter_rules_package_arn_list

        out["rules_package_arns"] = (
            aws_sdk_inspector.types.filter_rules_package_arn_list.deserialize_aws_json_1_1(
                data["rulesPackageArns"]
            )
        )
    if "attributes" in data:
        import aws_sdk_inspector.types.attribute_list

        out["attributes"] = (
            aws_sdk_inspector.types.attribute_list.deserialize_aws_json_1_1(
                data["attributes"]
            )
        )
    if "userAttributes" in data:
        import aws_sdk_inspector.types.attribute_list

        out["user_attributes"] = (
            aws_sdk_inspector.types.attribute_list.deserialize_aws_json_1_1(
                data["userAttributes"]
            )
        )
    if "creationTimeRange" in data:
        import aws_sdk_inspector.types.timestamp_range

        out["creation_time_range"] = (
            aws_sdk_inspector.types.timestamp_range.deserialize_aws_json_1_1(
                data["creationTimeRange"]
            )
        )
    return out
