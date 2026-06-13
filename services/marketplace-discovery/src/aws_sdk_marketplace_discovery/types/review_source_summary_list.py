"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ReviewSourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.review_source_summary

ReviewSourceSummaryList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.review_source_summary.ReviewSourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewSourceSummaryList) -> list:
    import aws_sdk_marketplace_discovery.types.review_source_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.review_source_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReviewSourceSummaryList:
    import aws_sdk_marketplace_discovery.types.review_source_summary

    out: ReviewSourceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.review_source_summary.deserialize_json(
                item
            )
        )
    return out
