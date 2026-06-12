"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorParametersToDelete``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.stream_processor_parameter_to_delete

StreamProcessorParametersToDelete: TypeAlias = list[
    "aws_sdk_rekognition.types.stream_processor_parameter_to_delete.StreamProcessorParameterToDelete"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorParametersToDelete) -> list:
    import aws_sdk_rekognition.types.stream_processor_parameter_to_delete

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.stream_processor_parameter_to_delete.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StreamProcessorParametersToDelete:
    import aws_sdk_rekognition.types.stream_processor_parameter_to_delete

    out: StreamProcessorParametersToDelete = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.stream_processor_parameter_to_delete.deserialize_aws_json_1_1(
                item
            )
        )
    return out
