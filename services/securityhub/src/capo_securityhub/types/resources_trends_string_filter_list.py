"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.resources_trends_string_filter

ResourcesTrendsStringFilterList: TypeAlias = list[
    "capo_securityhub.types.resources_trends_string_filter.ResourcesTrendsStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsStringFilterList) -> list:
    import capo_securityhub.types.resources_trends_string_filter

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.resources_trends_string_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourcesTrendsStringFilterList:
    import capo_securityhub.types.resources_trends_string_filter

    out: ResourcesTrendsStringFilterList = []
    for item in data:
        out.append(
            capo_securityhub.types.resources_trends_string_filter.deserialize_json(item)
        )
    return out
