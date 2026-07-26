"""Generated from Smithy shape ``com.amazonaws.securityagent#CategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.category

CategoryList: TypeAlias = list["capo_securityagent.types.category.Category"]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryList) -> list:
    import capo_securityagent.types.category

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.category.serialize_json(item))
    return out


def deserialize_json(data: list) -> CategoryList:
    import capo_securityagent.types.category

    out: CategoryList = []
    for item in data:
        out.append(capo_securityagent.types.category.deserialize_json(item))
    return out
