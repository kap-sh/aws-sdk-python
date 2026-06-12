"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorParameterToDelete``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

StreamProcessorParameterToDelete: TypeAlias = Literal[
    "ConnectedHomeMinConfidence",
    "RegionsOfInterest",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConnectedHomeMinConfidence",
        "RegionsOfInterest",
    )
)


def serialize_aws_json_1_1(value: StreamProcessorParameterToDelete) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamProcessorParameterToDelete:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StreamProcessorParameterToDelete value: {data!r}"
        )
    return cast(StreamProcessorParameterToDelete, data)
