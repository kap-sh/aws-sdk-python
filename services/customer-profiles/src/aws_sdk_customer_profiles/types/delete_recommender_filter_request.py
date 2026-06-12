"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteRecommenderFilterRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.recommender_filter_name


class DeleteRecommenderFilterRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_filter_name: (
        "aws_sdk_customer_profiles.types.recommender_filter_name.RecommenderFilterName"
    )
    """<p>The name of the recommender filter to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommenderFilterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRecommenderFilterRequest:
    out: DeleteRecommenderFilterRequest = {}  # type: ignore[typeddict-item]
    return out
