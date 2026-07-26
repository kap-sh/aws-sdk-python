"""Generated from Smithy shape ``com.amazonaws.qconnect#AndConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.tag_condition

AndConditions: TypeAlias = list["capo_qconnect.types.tag_condition.TagCondition"]


# --- restJson1 ser/de ---
def serialize_json(value: AndConditions) -> list:
    import capo_qconnect.types.tag_condition

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.tag_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> AndConditions:
    import capo_qconnect.types.tag_condition

    out: AndConditions = []
    for item in data:
        out.append(capo_qconnect.types.tag_condition.deserialize_json(item))
    return out
