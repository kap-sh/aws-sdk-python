"""Generated from Smithy shape ``com.amazonaws.securityhub#NumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.number_filter

NumberFilterList: TypeAlias = list["capo_securityhub.types.number_filter.NumberFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: NumberFilterList) -> list:
    import capo_securityhub.types.number_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.number_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> NumberFilterList:
    import capo_securityhub.types.number_filter

    out: NumberFilterList = []
    for item in data:
        out.append(capo_securityhub.types.number_filter.deserialize_json(item))
    return out
