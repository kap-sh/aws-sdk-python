"""Generated from Smithy shape ``com.amazonaws.dataexchange#GetRevisionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.id


class GetRevisionRequest(TypedDict, closed=True):
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for a revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRevisionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRevisionRequest:
    out: GetRevisionRequest = {}  # type: ignore[typeddict-item]
    return out
