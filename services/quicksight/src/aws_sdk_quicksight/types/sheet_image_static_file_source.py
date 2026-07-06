"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageStaticFileSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class SheetImageStaticFileSource(TypedDict, closed=True):
    static_file_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the static file that contains the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetImageStaticFileSource) -> dict:
    out: dict = {}
    out["StaticFileId"] = value["static_file_id"]
    return out


def deserialize_json(data: dict) -> SheetImageStaticFileSource:
    out: SheetImageStaticFileSource = {}  # type: ignore[typeddict-item]
    if "StaticFileId" in data:
        out["static_file_id"] = data["StaticFileId"]
    else:
        raise DeserializationError("SheetImageStaticFileSource.static_file_id required")
    return out
