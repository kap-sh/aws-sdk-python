"""Generated from Smithy shape ``com.amazonaws.connect#AttributeOrConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.attribute_and_condition

AttributeOrConditionList: TypeAlias = list[
    "capo_connect.types.attribute_and_condition.AttributeAndCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeOrConditionList) -> list:
    import capo_connect.types.attribute_and_condition

    out: list = []
    for item in value:
        out.append(capo_connect.types.attribute_and_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributeOrConditionList:
    import capo_connect.types.attribute_and_condition

    out: AttributeOrConditionList = []
    for item in data:
        out.append(capo_connect.types.attribute_and_condition.deserialize_json(item))
    return out
