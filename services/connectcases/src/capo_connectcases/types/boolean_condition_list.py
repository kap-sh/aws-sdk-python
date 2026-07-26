"""Generated from Smithy shape ``com.amazonaws.connectcases#BooleanConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.boolean_condition

BooleanConditionList: TypeAlias = list[
    "capo_connectcases.types.boolean_condition.BooleanCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: BooleanConditionList) -> list:
    import capo_connectcases.types.boolean_condition

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.boolean_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> BooleanConditionList:
    import capo_connectcases.types.boolean_condition

    out: BooleanConditionList = []
    for item in data:
        out.append(capo_connectcases.types.boolean_condition.deserialize_json(item))
    return out
