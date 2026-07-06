"""Generated from Smithy shape ``com.amazonaws.dataexchange#DeleteRevisionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.id


class DeleteRevisionRequest(TypedDict, closed=True):
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for a revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRevisionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRevisionRequest:
    out: DeleteRevisionRequest = {}  # type: ignore[typeddict-item]
    return out
