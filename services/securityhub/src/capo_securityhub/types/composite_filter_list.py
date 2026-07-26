"""Generated from Smithy shape ``com.amazonaws.securityhub#CompositeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.composite_filter

CompositeFilterList: TypeAlias = list[
    "capo_securityhub.types.composite_filter.CompositeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompositeFilterList) -> list:
    import capo_securityhub.types.composite_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.composite_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CompositeFilterList:
    import capo_securityhub.types.composite_filter

    out: CompositeFilterList = []
    for item in data:
        out.append(capo_securityhub.types.composite_filter.deserialize_json(item))
    return out
