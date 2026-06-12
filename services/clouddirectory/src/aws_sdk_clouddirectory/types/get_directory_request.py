"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetDirectoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.directory_arn


class GetDirectoryRequest(TypedDict):
    directory_arn: "aws_sdk_clouddirectory.types.directory_arn.DirectoryArn"
    """<p>The ARN of the directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDirectoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDirectoryRequest:
    out: GetDirectoryRequest = {}  # type: ignore[typeddict-item]
    return out
