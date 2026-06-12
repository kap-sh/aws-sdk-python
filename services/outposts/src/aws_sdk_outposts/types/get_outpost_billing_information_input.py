"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostBillingInformationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.token


class GetOutpostBillingInformationInput(TypedDict):
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outpost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostBillingInformationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOutpostBillingInformationInput:
    out: GetOutpostBillingInformationInput = {}  # type: ignore[typeddict-item]
    return out
