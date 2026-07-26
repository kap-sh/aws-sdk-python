"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsCompositeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.resources_trends_composite_filter

ResourcesTrendsCompositeFilterList: TypeAlias = list[
    "capo_securityhub.types.resources_trends_composite_filter.ResourcesTrendsCompositeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsCompositeFilterList) -> list:
    import capo_securityhub.types.resources_trends_composite_filter

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.resources_trends_composite_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourcesTrendsCompositeFilterList:
    import capo_securityhub.types.resources_trends_composite_filter

    out: ResourcesTrendsCompositeFilterList = []
    for item in data:
        out.append(
            capo_securityhub.types.resources_trends_composite_filter.deserialize_json(
                item
            )
        )
    return out
