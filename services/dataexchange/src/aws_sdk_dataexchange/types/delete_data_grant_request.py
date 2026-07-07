"""Generated from Smithy shape ``com.amazonaws.dataexchange#DeleteDataGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.data_grant_id


class DeleteDataGrantRequest(TypedDict, closed=True):
    data_grant_id: "aws_sdk_dataexchange.types.data_grant_id.DataGrantId"
    """<p>The ID of the data grant to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataGrantRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataGrantRequest:
    out: DeleteDataGrantRequest = {}  # type: ignore[typeddict-item]
    return out
