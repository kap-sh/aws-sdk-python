"""Generated from Smithy shape ``com.amazonaws.wafv2#Rules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.rule

Rules: TypeAlias = list["capo_wafv2.types.rule.Rule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rules) -> list:
    import capo_wafv2.types.rule

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Rules:
    import capo_wafv2.types.rule

    out: Rules = []
    for item in data:
        out.append(capo_wafv2.types.rule.deserialize_aws_json_1_1(item))
    return out
