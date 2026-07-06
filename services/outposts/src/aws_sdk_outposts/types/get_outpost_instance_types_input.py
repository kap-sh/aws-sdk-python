"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostInstanceTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.outpost_id
    import aws_sdk_outposts.types.token


class GetOutpostInstanceTypesInput(TypedDict, closed=True):
    outpost_id: "aws_sdk_outposts.types.outpost_id.OutpostId"
    """<p> The ID or ARN of the Outpost. </p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostInstanceTypesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOutpostInstanceTypesInput:
    out: GetOutpostInstanceTypesInput = {}  # type: ignore[typeddict-item]
    return out
