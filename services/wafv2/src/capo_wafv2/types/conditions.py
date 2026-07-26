"""Generated from Smithy shape ``com.amazonaws.wafv2#Conditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.condition

Conditions: TypeAlias = list["capo_wafv2.types.condition.Condition"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Conditions) -> list:
    import capo_wafv2.types.condition

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.condition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Conditions:
    import capo_wafv2.types.condition

    out: Conditions = []
    for item in data:
        out.append(capo_wafv2.types.condition.deserialize_aws_json_1_1(item))
    return out
