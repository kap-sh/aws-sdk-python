"""Generated from Smithy shape ``com.amazonaws.securityhub#StringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.string_filter

StringFilterList: TypeAlias = list["capo_securityhub.types.string_filter.StringFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: StringFilterList) -> list:
    import capo_securityhub.types.string_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> StringFilterList:
    import capo_securityhub.types.string_filter

    out: StringFilterList = []
    for item in data:
        out.append(capo_securityhub.types.string_filter.deserialize_json(item))
    return out
