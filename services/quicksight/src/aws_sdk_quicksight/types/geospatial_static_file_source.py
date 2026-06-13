"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialStaticFileSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class GeospatialStaticFileSource(TypedDict):
    static_file_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID of the static file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialStaticFileSource) -> dict:
    out: dict = {}
    out["StaticFileId"] = value["static_file_id"]
    return out


def deserialize_json(data: dict) -> GeospatialStaticFileSource:
    out: GeospatialStaticFileSource = {}  # type: ignore[typeddict-item]
    if "StaticFileId" in data:
        out["static_file_id"] = data["StaticFileId"]
    else:
        raise DeserializationError("GeospatialStaticFileSource.static_file_id required")
    return out
