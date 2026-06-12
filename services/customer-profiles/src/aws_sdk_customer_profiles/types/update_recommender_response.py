"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateRecommenderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class UpdateRecommenderResponse(TypedDict):
    recommender_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the recommender that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommenderResponse) -> dict:
    out: dict = {}
    out["RecommenderName"] = value["recommender_name"]
    return out


def deserialize_json(data: dict) -> UpdateRecommenderResponse:
    out: UpdateRecommenderResponse = {}  # type: ignore[typeddict-item]
    if "RecommenderName" in data:
        out["recommender_name"] = data["RecommenderName"]
    else:
        raise DeserializationError(
            "UpdateRecommenderResponse.recommender_name required"
        )
    return out
