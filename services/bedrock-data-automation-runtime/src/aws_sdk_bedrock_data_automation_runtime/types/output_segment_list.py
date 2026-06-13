"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#OutputSegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.output_segment

OutputSegmentList: TypeAlias = list[
    "aws_sdk_bedrock_data_automation_runtime.types.output_segment.OutputSegment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputSegmentList) -> list:
    import aws_sdk_bedrock_data_automation_runtime.types.output_segment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation_runtime.types.output_segment.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OutputSegmentList:
    import aws_sdk_bedrock_data_automation_runtime.types.output_segment

    out: OutputSegmentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation_runtime.types.output_segment.deserialize_aws_json_1_1(
                item
            )
        )
    return out
