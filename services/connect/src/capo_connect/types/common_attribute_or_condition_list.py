"""Generated from Smithy shape ``com.amazonaws.connect#CommonAttributeOrConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.common_attribute_and_condition

CommonAttributeOrConditionList: TypeAlias = list[
    "capo_connect.types.common_attribute_and_condition.CommonAttributeAndCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommonAttributeOrConditionList) -> list:
    import capo_connect.types.common_attribute_and_condition

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.common_attribute_and_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CommonAttributeOrConditionList:
    import capo_connect.types.common_attribute_and_condition

    out: CommonAttributeOrConditionList = []
    for item in data:
        out.append(
            capo_connect.types.common_attribute_and_condition.deserialize_json(item)
        )
    return out
