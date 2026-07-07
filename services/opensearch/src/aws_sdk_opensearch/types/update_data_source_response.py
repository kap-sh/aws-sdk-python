"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateDataSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.string


class UpdateDataSourceResponse(TypedDict, closed=True):
    message: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>A message associated with the updated data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UpdateDataSourceResponse:
    out: UpdateDataSourceResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
