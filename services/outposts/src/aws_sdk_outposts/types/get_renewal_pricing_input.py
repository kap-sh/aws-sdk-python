"""Generated from Smithy shape ``com.amazonaws.outposts#GetRenewalPricingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost_identifier


class GetRenewalPricingInput(TypedDict, closed=True):
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outpost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRenewalPricingInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRenewalPricingInput:
    out: GetRenewalPricingInput = {}  # type: ignore[typeddict-item]
    return out
