"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DisableDirectoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class DisableDirectoryResponse(TypedDict):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the directory that has been disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableDirectoryResponse) -> dict:
    out: dict = {}
    out["DirectoryArn"] = value["directory_arn"]
    return out


def deserialize_json(data: dict) -> DisableDirectoryResponse:
    out: DisableDirectoryResponse = {}  # type: ignore[typeddict-item]
    if "DirectoryArn" in data:
        out["directory_arn"] = data["DirectoryArn"]
    else:
        raise DeserializationError("DisableDirectoryResponse.directory_arn required")
    return out
