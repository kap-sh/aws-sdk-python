"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

ProjectStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: ProjectStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectStatus value: {data!r}")
    return cast(ProjectStatus, data)
