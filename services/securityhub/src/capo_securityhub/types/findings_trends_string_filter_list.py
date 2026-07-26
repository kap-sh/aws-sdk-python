"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsTrendsStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.findings_trends_string_filter

FindingsTrendsStringFilterList: TypeAlias = list[
    "capo_securityhub.types.findings_trends_string_filter.FindingsTrendsStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsTrendsStringFilterList) -> list:
    import capo_securityhub.types.findings_trends_string_filter

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.findings_trends_string_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingsTrendsStringFilterList:
    import capo_securityhub.types.findings_trends_string_filter

    out: FindingsTrendsStringFilterList = []
    for item in data:
        out.append(
            capo_securityhub.types.findings_trends_string_filter.deserialize_json(item)
        )
    return out
