"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorParameterToDelete``."""

from typing import Literal, TypeAlias, cast

StreamProcessorParameterToDelete: TypeAlias = Literal[
    "ConnectedHomeMinConfidence",
    "RegionsOfInterest",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorParameterToDelete) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamProcessorParameterToDelete:
    return cast(StreamProcessorParameterToDelete, data)
