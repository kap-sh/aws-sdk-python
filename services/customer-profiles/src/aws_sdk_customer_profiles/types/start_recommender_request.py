"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StartRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class StartRecommenderRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the recommender to start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRecommenderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartRecommenderRequest:
    out: StartRecommenderRequest = {}  # type: ignore[typeddict-item]
    return out
