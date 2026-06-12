"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StartImportFileTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.string


class StartImportFileTaskResponse(TypedDict):
    id: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> The ID for a specific import task. The ID is unique within an AWS account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportFileTaskResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> StartImportFileTaskResponse:
    out: StartImportFileTaskResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
