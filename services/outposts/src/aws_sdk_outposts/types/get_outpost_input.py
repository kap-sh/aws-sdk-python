"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost_id


class GetOutpostInput(TypedDict, closed=True):
    outpost_id: "aws_sdk_outposts.types.outpost_id.OutpostId"
    """<p>The ID or ARN of the Outpost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOutpostInput:
    out: GetOutpostInput = {}  # type: ignore[typeddict-item]
    return out
