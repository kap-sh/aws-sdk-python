"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetWorkingLocationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.string_value_length1to63
    import aws_sdk_finspace_data.types.string_value_length1to1024


class GetWorkingLocationResponse(TypedDict):
    s3_uri: NotRequired[
        "aws_sdk_finspace_data.types.string_value_length1to1024.stringValueLength1to1024"
    ]
    """<p>Returns the Amazon S3 URI for the working location.</p>"""
    s3_path: NotRequired[
        "aws_sdk_finspace_data.types.string_value_length1to1024.stringValueLength1to1024"
    ]
    """<p>Returns the Amazon S3 Path for the working location.</p>"""
    s3_bucket: NotRequired[
        "aws_sdk_finspace_data.types.string_value_length1to63.stringValueLength1to63"
    ]
    """<p>Returns the Amazon S3 bucket name for the working location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkingLocationResponse) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["s3Uri"] = value["s3_uri"]
    if "s3_path" in value:
        out["s3Path"] = value["s3_path"]
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    return out


def deserialize_json(data: dict) -> GetWorkingLocationResponse:
    out: GetWorkingLocationResponse = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    if "s3Path" in data:
        out["s3_path"] = data["s3Path"]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    return out
