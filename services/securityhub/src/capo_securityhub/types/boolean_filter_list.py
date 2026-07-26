"""Generated from Smithy shape ``com.amazonaws.securityhub#BooleanFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.boolean_filter

BooleanFilterList: TypeAlias = list[
    "capo_securityhub.types.boolean_filter.BooleanFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: BooleanFilterList) -> list:
    import capo_securityhub.types.boolean_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.boolean_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> BooleanFilterList:
    import capo_securityhub.types.boolean_filter

    out: BooleanFilterList = []
    for item in data:
        out.append(capo_securityhub.types.boolean_filter.deserialize_json(item))
    return out
