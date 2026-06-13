"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#SyncInputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.s3_uri


class SyncInputConfiguration(TypedDict):
    bytes: NotRequired["bytes"]
    """Input data as bytes"""
    s3_uri: NotRequired["aws_sdk_bedrock_data_automation_runtime.types.s3_uri.S3Uri"]
    """S3 URI of the input data"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SyncInputConfiguration) -> dict:
    out: dict = {}
    if "bytes" in value:
        import aws_sdk_bedrock_data_automation_runtime.types._prelude.blob

        out["bytes"] = (
            aws_sdk_bedrock_data_automation_runtime.types._prelude.blob.serialize_aws_json_1_1(
                value["bytes"]
            )
        )
    if "s3_uri" in value:
        out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SyncInputConfiguration:
    out: SyncInputConfiguration = {}  # type: ignore[typeddict-item]
    if "bytes" in data:
        import aws_sdk_bedrock_data_automation_runtime.types._prelude.blob

        out["bytes"] = (
            aws_sdk_bedrock_data_automation_runtime.types._prelude.blob.deserialize_aws_json_1_1(
                data["bytes"]
            )
        )
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    return out
