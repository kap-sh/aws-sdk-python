"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#OutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.s3_uri


class OutputConfiguration(TypedDict, closed=True):
    s3_uri: "aws_sdk_bedrock_data_automation_runtime.types.s3_uri.S3Uri"
    """S3 uri."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputConfiguration) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputConfiguration:
    out: OutputConfiguration = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("OutputConfiguration.s3_uri required")
    return out
