"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentEstimateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to255


class GetSegmentEstimateRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    estimate_id: "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    """<p>The query Id passed by a previous <code>CreateSegmentEstimate</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentEstimateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSegmentEstimateRequest:
    out: GetSegmentEstimateRequest = {}  # type: ignore[typeddict-item]
    return out
