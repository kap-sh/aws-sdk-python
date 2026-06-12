"""Generated from Smithy shape ``com.amazonaws.emr#ScalingRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.scaling_rule

ScalingRuleList: TypeAlias = list["aws_sdk_emr.types.scaling_rule.ScalingRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingRuleList) -> list:
    import aws_sdk_emr.types.scaling_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.scaling_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingRuleList:
    import aws_sdk_emr.types.scaling_rule

    out: ScalingRuleList = []
    for item in data:
        out.append(aws_sdk_emr.types.scaling_rule.deserialize_aws_json_1_1(item))
    return out
