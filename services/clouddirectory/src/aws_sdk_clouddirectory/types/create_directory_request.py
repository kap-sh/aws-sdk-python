"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateDirectoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.directory_name


class CreateDirectoryRequest(TypedDict):
    name: "aws_sdk_clouddirectory.types.directory_name.DirectoryName"
    """<p>The name of the <a>Directory</a>. Should be unique per account, per region.</p>"""
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the published schema that will be copied into the data <a>Directory</a>. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDirectoryRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateDirectoryRequest:
    out: CreateDirectoryRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDirectoryRequest.name required")
    return out
