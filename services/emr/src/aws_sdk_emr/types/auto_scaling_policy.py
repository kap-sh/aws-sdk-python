"""Generated from Smithy shape ``com.amazonaws.emr#AutoScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.scaling_constraints
    import aws_sdk_emr.types.scaling_rule_list


class AutoScalingPolicy(TypedDict, closed=True):
    constraints: NotRequired["aws_sdk_emr.types.scaling_constraints.ScalingConstraints"]
    """<p>The upper and lower Amazon EC2 instance limits for an automatic scaling policy. Automatic scaling activity will not cause an instance group to grow above or below these limits.</p>"""
    rules: NotRequired["aws_sdk_emr.types.scaling_rule_list.ScalingRuleList"]
    """<p>The scale-in and scale-out rules that comprise the automatic scaling policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoScalingPolicy) -> dict:
    out: dict = {}
    if "constraints" in value:
        import aws_sdk_emr.types.scaling_constraints

        out["Constraints"] = (
            aws_sdk_emr.types.scaling_constraints.serialize_aws_json_1_1(
                value["constraints"]
            )
        )
    if "rules" in value:
        import aws_sdk_emr.types.scaling_rule_list

        out["Rules"] = aws_sdk_emr.types.scaling_rule_list.serialize_aws_json_1_1(
            value["rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoScalingPolicy:
    out: AutoScalingPolicy = {}  # type: ignore[typeddict-item]
    if "Constraints" in data:
        import aws_sdk_emr.types.scaling_constraints

        out["constraints"] = (
            aws_sdk_emr.types.scaling_constraints.deserialize_aws_json_1_1(
                data["Constraints"]
            )
        )
    if "Rules" in data:
        import aws_sdk_emr.types.scaling_rule_list

        out["rules"] = aws_sdk_emr.types.scaling_rule_list.deserialize_aws_json_1_1(
            data["Rules"]
        )
    return out
