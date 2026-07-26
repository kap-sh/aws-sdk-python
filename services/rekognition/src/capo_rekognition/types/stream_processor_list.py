"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.stream_processor

StreamProcessorList: TypeAlias = list[
    "capo_rekognition.types.stream_processor.StreamProcessor"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorList) -> list:
    import capo_rekognition.types.stream_processor

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.stream_processor.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StreamProcessorList:
    import capo_rekognition.types.stream_processor

    out: StreamProcessorList = []
    for item in data:
        out.append(
            capo_rekognition.types.stream_processor.deserialize_aws_json_1_1(item)
        )
    return out
