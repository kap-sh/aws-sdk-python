"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ReviewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.review_source_summary_list


class ReviewSummary(TypedDict, closed=True):
    review_source_summaries: "aws_sdk_marketplace_discovery.types.review_source_summary_list.ReviewSourceSummaryList"
    """<p>Review summaries from different sources, such as AWS Marketplace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReviewSummary) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.review_source_summary_list

    out["reviewSourceSummaries"] = (
        aws_sdk_marketplace_discovery.types.review_source_summary_list.serialize_json(
            value["review_source_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ReviewSummary:
    out: ReviewSummary = {}  # type: ignore[typeddict-item]
    if "reviewSourceSummaries" in data:
        import aws_sdk_marketplace_discovery.types.review_source_summary_list

        out["review_source_summaries"] = (
            aws_sdk_marketplace_discovery.types.review_source_summary_list.deserialize_json(
                data["reviewSourceSummaries"]
            )
        )
    else:
        raise DeserializationError("ReviewSummary.review_source_summaries required")
    return out
