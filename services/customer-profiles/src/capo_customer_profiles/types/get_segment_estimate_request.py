"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentEstimateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to255


class GetSegmentEstimateRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    estimate_id: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The query Id passed by a previous <code>CreateSegmentEstimate</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentEstimateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSegmentEstimateRequest:
    out: GetSegmentEstimateRequest = {}  # type: ignore[typeddict-item]
    return out
