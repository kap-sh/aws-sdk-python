"""Generated from Smithy shape ``com.amazonaws.clouddirectory#EnableDirectoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn


class EnableDirectoryResponse(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The ARN of the enabled directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableDirectoryResponse) -> dict:
    out: dict = {}
    out["DirectoryArn"] = value["directory_arn"]
    return out


def deserialize_json(data: dict) -> EnableDirectoryResponse:
    out: EnableDirectoryResponse = {}  # type: ignore[typeddict-item]
    if "DirectoryArn" in data:
        out["directory_arn"] = data["DirectoryArn"]
    else:
        raise DeserializationError("EnableDirectoryResponse.directory_arn required")
    return out
