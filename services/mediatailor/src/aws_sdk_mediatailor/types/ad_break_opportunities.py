"""Generated from Smithy shape ``com.amazonaws.mediatailor#AdBreakOpportunities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.ad_break_opportunity

AdBreakOpportunities: TypeAlias = list[
    "aws_sdk_mediatailor.types.ad_break_opportunity.AdBreakOpportunity"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdBreakOpportunities) -> list:
    import aws_sdk_mediatailor.types.ad_break_opportunity

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.ad_break_opportunity.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdBreakOpportunities:
    import aws_sdk_mediatailor.types.ad_break_opportunity

    out: AdBreakOpportunities = []
    for item in data:
        out.append(
            aws_sdk_mediatailor.types.ad_break_opportunity.deserialize_json(item)
        )
    return out
