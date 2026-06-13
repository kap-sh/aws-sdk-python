"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateBrandPublishedVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.string


class UpdateBrandPublishedVersionResponse(TypedDict):
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    version_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the published version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandPublishedVersionResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> UpdateBrandPublishedVersionResponse:
    out: UpdateBrandPublishedVersionResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
