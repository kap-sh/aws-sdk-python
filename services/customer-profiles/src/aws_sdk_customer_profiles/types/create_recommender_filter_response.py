"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.arn
    import aws_sdk_customer_profiles.types.tag_map


class CreateRecommenderFilterResponse(TypedDict, closed=True):
    recommender_filter_arn: "aws_sdk_customer_profiles.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recommender filter.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderFilterResponse) -> dict:
    out: dict = {}
    out["RecommenderFilterArn"] = value["recommender_filter_arn"]
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRecommenderFilterResponse:
    out: CreateRecommenderFilterResponse = {}  # type: ignore[typeddict-item]
    if "RecommenderFilterArn" in data:
        out["recommender_filter_arn"] = data["RecommenderFilterArn"]
    else:
        raise DeserializationError(
            "CreateRecommenderFilterResponse.recommender_filter_arn required"
        )
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
