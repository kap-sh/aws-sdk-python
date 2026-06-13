"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#VideoSegmentConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_data_automation_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.timestamp_segment


class _VideoSegmentConfiguration_timestampSegment(TypedDict):
    timestampSegment: "aws_sdk_bedrock_data_automation_runtime.types.timestamp_segment.TimestampSegment"


VideoSegmentConfiguration: TypeAlias = _VideoSegmentConfiguration_timestampSegment


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VideoSegmentConfiguration) -> dict:
    if "timestampSegment" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.timestamp_segment

        return {
            "timestampSegment": aws_sdk_bedrock_data_automation_runtime.types.timestamp_segment.serialize_aws_json_1_1(
                value["timestampSegment"]
            )
        }
    else:
        raise SerializationError("VideoSegmentConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> VideoSegmentConfiguration:
    if "timestampSegment" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.timestamp_segment

        return {
            "timestampSegment": aws_sdk_bedrock_data_automation_runtime.types.timestamp_segment.deserialize_aws_json_1_1(
                data["timestampSegment"]
            )
        }
    else:
        raise DeserializationError(
            "VideoSegmentConfiguration: no recognized variant key"
        )
