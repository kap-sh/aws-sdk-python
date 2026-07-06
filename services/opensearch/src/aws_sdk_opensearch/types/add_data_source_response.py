"""Generated from Smithy shape ``com.amazonaws.opensearch#AddDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.string


class AddDataSourceResponse(TypedDict, closed=True):
    message: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>A message associated with creation of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddDataSourceResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AddDataSourceResponse:
    out: AddDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
