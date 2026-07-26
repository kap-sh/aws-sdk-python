"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedOperatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.operators

SupportedOperatorList: TypeAlias = list["capo_appflow.types.operators.Operators"]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedOperatorList) -> list:
    import capo_appflow.types.operators

    out: list = []
    for item in value:
        out.append(capo_appflow.types.operators.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportedOperatorList:
    import capo_appflow.types.operators

    out: SupportedOperatorList = []
    for item in data:
        out.append(capo_appflow.types.operators.deserialize_json(item))
    return out
