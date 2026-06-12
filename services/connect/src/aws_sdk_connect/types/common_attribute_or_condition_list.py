"""Generated from Smithy shape ``com.amazonaws.connect#CommonAttributeOrConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.common_attribute_and_condition

CommonAttributeOrConditionList: TypeAlias = list[
    "aws_sdk_connect.types.common_attribute_and_condition.CommonAttributeAndCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommonAttributeOrConditionList) -> list:
    import aws_sdk_connect.types.common_attribute_and_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.common_attribute_and_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CommonAttributeOrConditionList:
    import aws_sdk_connect.types.common_attribute_and_condition

    out: CommonAttributeOrConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.common_attribute_and_condition.deserialize_json(item)
        )
    return out
