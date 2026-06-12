"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#OutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.s3_uri


class OutputConfiguration(TypedDict):
    s3_uri: "aws_sdk_bedrock_data_automation.types.s3_uri.S3Uri"
    """S3 Uri"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputConfiguration) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> OutputConfiguration:
    out: OutputConfiguration = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("OutputConfiguration.s3_uri required")
    return out
