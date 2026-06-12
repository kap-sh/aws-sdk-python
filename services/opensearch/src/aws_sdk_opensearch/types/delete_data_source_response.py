"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteDataSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.string


class DeleteDataSourceResponse(TypedDict):
    message: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>A message associated with deletion of the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataSourceResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteDataSourceResponse:
    out: DeleteDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
