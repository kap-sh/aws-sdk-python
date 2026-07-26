"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostBillingInformationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.max_results1000
    import capo_outposts.types.outpost_identifier
    import capo_outposts.types.token


class GetOutpostBillingInformationInput(TypedDict, closed=True):
    next_token: NotRequired["capo_outposts.types.token.Token"]
    max_results: NotRequired["capo_outposts.types.max_results1000.MaxResults1000"]
    outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outpost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostBillingInformationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOutpostBillingInformationInput:
    out: GetOutpostBillingInformationInput = {}  # type: ignore[typeddict-item]
    return out
