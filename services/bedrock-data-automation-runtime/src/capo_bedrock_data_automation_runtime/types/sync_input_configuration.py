"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#SyncInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.s3_uri


class SyncInputConfiguration(TypedDict, closed=True):
    bytes: NotRequired["bytes"]
    """Input data as bytes"""
    s3_uri: NotRequired["capo_bedrock_data_automation_runtime.types.s3_uri.S3Uri"]
    """S3 URI of the input data"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SyncInputConfiguration) -> dict:
    out: dict = {}
    if "bytes" in value:
        import capo_bedrock_data_automation_runtime.types._prelude.blob

        out["bytes"] = (
            capo_bedrock_data_automation_runtime.types._prelude.blob.serialize_aws_json_1_1(
                value["bytes"]
            )
        )
    if "s3_uri" in value:
        out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SyncInputConfiguration:
    out: SyncInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bytes") is not None:
        import capo_bedrock_data_automation_runtime.types._prelude.blob

        out["bytes"] = (
            capo_bedrock_data_automation_runtime.types._prelude.blob.deserialize_aws_json_1_1(
                data["bytes"]
            )
        )
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    return out
