"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.resources_string_filter

ResourcesStringFilterList: TypeAlias = list[
    "capo_securityhub.types.resources_string_filter.ResourcesStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesStringFilterList) -> list:
    import capo_securityhub.types.resources_string_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.resources_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcesStringFilterList:
    import capo_securityhub.types.resources_string_filter

    out: ResourcesStringFilterList = []
    for item in data:
        out.append(
            capo_securityhub.types.resources_string_filter.deserialize_json(item)
        )
    return out
