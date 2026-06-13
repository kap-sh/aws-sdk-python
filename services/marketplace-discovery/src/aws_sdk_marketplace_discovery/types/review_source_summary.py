"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ReviewSourceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.non_negative_count
    import aws_sdk_marketplace_discovery.types.review_source_id
    import aws_sdk_marketplace_discovery.types.url


class ReviewSourceSummary(TypedDict):
    source_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The name of the review source, such as AWS Marketplace.</p>"""
    source_id: "aws_sdk_marketplace_discovery.types.review_source_id.ReviewSourceId"
    """<p>The machine-readable identifier of the review source.</p>"""
    source_url: NotRequired["aws_sdk_marketplace_discovery.types.url.URL"]
    """<p>The URL where the reviews can be accessed at the source.</p>"""
    average_rating: (
        "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>The average rating across all reviews from this source.</p>"""
    total_reviews: (
        "aws_sdk_marketplace_discovery.types.non_negative_count.NonNegativeCount"
    )
    """<p>The total number of reviews available from this source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReviewSourceSummary) -> dict:
    out: dict = {}
    out["sourceName"] = value["source_name"]
    import aws_sdk_marketplace_discovery.types.review_source_id

    out["sourceId"] = (
        aws_sdk_marketplace_discovery.types.review_source_id.serialize_json(
            value["source_id"]
        )
    )
    if "source_url" in value:
        out["sourceUrl"] = value["source_url"]
    out["averageRating"] = value["average_rating"]
    out["totalReviews"] = value["total_reviews"]
    return out


def deserialize_json(data: dict) -> ReviewSourceSummary:
    out: ReviewSourceSummary = {}  # type: ignore[typeddict-item]
    if "sourceName" in data:
        out["source_name"] = data["sourceName"]
    else:
        raise DeserializationError("ReviewSourceSummary.source_name required")
    if "sourceId" in data:
        import aws_sdk_marketplace_discovery.types.review_source_id

        out["source_id"] = (
            aws_sdk_marketplace_discovery.types.review_source_id.deserialize_json(
                data["sourceId"]
            )
        )
    else:
        raise DeserializationError("ReviewSourceSummary.source_id required")
    if "sourceUrl" in data:
        out["source_url"] = data["sourceUrl"]
    if "averageRating" in data:
        out["average_rating"] = data["averageRating"]
    else:
        raise DeserializationError("ReviewSourceSummary.average_rating required")
    if "totalReviews" in data:
        out["total_reviews"] = data["totalReviews"]
    else:
        raise DeserializationError("ReviewSourceSummary.total_reviews required")
    return out
