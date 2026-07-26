"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DeleteDirectoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn


class DeleteDirectoryResponse(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the deleted directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDirectoryResponse) -> dict:
    out: dict = {}
    out["DirectoryArn"] = value["directory_arn"]
    return out


def deserialize_json(data: dict) -> DeleteDirectoryResponse:
    out: DeleteDirectoryResponse = {}  # type: ignore[typeddict-item]
    if "DirectoryArn" in data:
        out["directory_arn"] = data["DirectoryArn"]
    else:
        raise DeserializationError("DeleteDirectoryResponse.directory_arn required")
    return out
