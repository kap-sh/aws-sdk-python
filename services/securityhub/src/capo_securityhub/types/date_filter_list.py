"""Generated from Smithy shape ``com.amazonaws.securityhub#DateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.date_filter

DateFilterList: TypeAlias = list["capo_securityhub.types.date_filter.DateFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: DateFilterList) -> list:
    import capo_securityhub.types.date_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.date_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DateFilterList:
    import capo_securityhub.types.date_filter

    out: DateFilterList = []
    for item in data:
        out.append(capo_securityhub.types.date_filter.deserialize_json(item))
    return out
