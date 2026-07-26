"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateRecommenderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.arn
    import capo_customer_profiles.types.tag_map


class CreateRecommenderResponse(TypedDict, closed=True):
    recommender_arn: "capo_customer_profiles.types.arn.Arn"
    """<p>The ARN of the recommender</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommenderResponse) -> dict:
    out: dict = {}
    out["RecommenderArn"] = value["recommender_arn"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRecommenderResponse:
    out: CreateRecommenderResponse = {}  # type: ignore[typeddict-item]
    if "RecommenderArn" in data:
        out["recommender_arn"] = data["RecommenderArn"]
    else:
        raise DeserializationError("CreateRecommenderResponse.recommender_arn required")
    if "Tags" in data:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
