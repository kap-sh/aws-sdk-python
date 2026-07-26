"""Generated from Smithy shape ``com.amazonaws.appflow#FilterOperatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.operator

FilterOperatorList: TypeAlias = list["capo_appflow.types.operator.Operator"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperatorList) -> list:
    import capo_appflow.types.operator

    out: list = []
    for item in value:
        out.append(capo_appflow.types.operator.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterOperatorList:
    import capo_appflow.types.operator

    out: FilterOperatorList = []
    for item in data:
        out.append(capo_appflow.types.operator.deserialize_json(item))
    return out
