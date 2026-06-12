"""Generated from Smithy shape ``com.amazonaws.outposts#DeleteOutpostInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost_id


class DeleteOutpostInput(TypedDict):
    outpost_id: "aws_sdk_outposts.types.outpost_id.OutpostId"
    """<p> The ID or ARN of the Outpost. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOutpostInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOutpostInput:
    out: DeleteOutpostInput = {}  # type: ignore[typeddict-item]
    return out
