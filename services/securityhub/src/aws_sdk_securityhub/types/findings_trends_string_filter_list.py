"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsTrendsStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.findings_trends_string_filter

FindingsTrendsStringFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.findings_trends_string_filter.FindingsTrendsStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsTrendsStringFilterList) -> list:
    import aws_sdk_securityhub.types.findings_trends_string_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.findings_trends_string_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FindingsTrendsStringFilterList:
    import aws_sdk_securityhub.types.findings_trends_string_filter

    out: FindingsTrendsStringFilterList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.findings_trends_string_filter.deserialize_json(
                item
            )
        )
    return out
