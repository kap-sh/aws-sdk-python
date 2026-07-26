"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StopRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class StopRecommenderRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    recommender_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the recommender to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopRecommenderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopRecommenderRequest:
    out: StopRecommenderRequest = {}  # type: ignore[typeddict-item]
    return out
