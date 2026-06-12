"""Generated from Smithy shape ``com.amazonaws.dataexchange#GetDataGrantRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.data_grant_id


class GetDataGrantRequest(TypedDict):
    data_grant_id: "aws_sdk_dataexchange.types.data_grant_id.DataGrantId"
    """<p>The ID of the data grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataGrantRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataGrantRequest:
    out: GetDataGrantRequest = {}  # type: ignore[typeddict-item]
    return out
