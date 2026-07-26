"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesCompositeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.resources_composite_filter

ResourcesCompositeFilterList: TypeAlias = list[
    "capo_securityhub.types.resources_composite_filter.ResourcesCompositeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesCompositeFilterList) -> list:
    import capo_securityhub.types.resources_composite_filter

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.resources_composite_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourcesCompositeFilterList:
    import capo_securityhub.types.resources_composite_filter

    out: ResourcesCompositeFilterList = []
    for item in data:
        out.append(
            capo_securityhub.types.resources_composite_filter.deserialize_json(item)
        )
    return out
