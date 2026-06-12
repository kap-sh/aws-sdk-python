"""Generated from Smithy shape ``com.amazonaws.wafv2#Conditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.condition

Conditions: TypeAlias = list["aws_sdk_wafv2.types.condition.Condition"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Conditions) -> list:
    import aws_sdk_wafv2.types.condition

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.condition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Conditions:
    import aws_sdk_wafv2.types.condition

    out: Conditions = []
    for item in data:
        out.append(aws_sdk_wafv2.types.condition.deserialize_aws_json_1_1(item))
    return out
