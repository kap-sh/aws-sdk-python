"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class DeleteRecommenderRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The recommender name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommenderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRecommenderRequest:
    out: DeleteRecommenderRequest = {}  # type: ignore[typeddict-item]
    return out
