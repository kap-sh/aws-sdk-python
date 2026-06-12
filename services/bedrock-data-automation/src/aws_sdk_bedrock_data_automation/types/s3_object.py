"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#S3Object``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.s3_object_version
    import aws_sdk_bedrock_data_automation.types.s3_uri


class S3Object(TypedDict):
    s3_uri: "aws_sdk_bedrock_data_automation.types.s3_uri.S3Uri"
    """S3 uri."""
    version: NotRequired[
        "aws_sdk_bedrock_data_automation.types.s3_object_version.S3ObjectVersion"
    ]
    """S3 object version."""


# --- restJson1 ser/de ---
def serialize_json(value: S3Object) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("S3Object.s3_uri required")
    if "version" in data:
        out["version"] = data["version"]
    return out
