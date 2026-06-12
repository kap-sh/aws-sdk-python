"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteSummaryListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.quote_summary

QuoteSummaryListDefinition: TypeAlias = list[
    "aws_sdk_outposts.types.quote_summary.QuoteSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuoteSummaryListDefinition) -> list:
    import aws_sdk_outposts.types.quote_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.quote_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuoteSummaryListDefinition:
    import aws_sdk_outposts.types.quote_summary

    out: QuoteSummaryListDefinition = []
    for item in data:
        out.append(aws_sdk_outposts.types.quote_summary.deserialize_json(item))
    return out
