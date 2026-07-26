"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsTrendsCompositeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.findings_trends_composite_filter

FindingsTrendsCompositeFilterList: TypeAlias = list[
    "capo_securityhub.types.findings_trends_composite_filter.FindingsTrendsCompositeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsTrendsCompositeFilterList) -> list:
    import capo_securityhub.types.findings_trends_composite_filter

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.findings_trends_composite_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingsTrendsCompositeFilterList:
    import capo_securityhub.types.findings_trends_composite_filter

    out: FindingsTrendsCompositeFilterList = []
    for item in data:
        out.append(
            capo_securityhub.types.findings_trends_composite_filter.deserialize_json(
                item
            )
        )
    return out
