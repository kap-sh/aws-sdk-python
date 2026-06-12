"""Generated from Smithy shape ``com.amazonaws.rekognition#ProjectAutoUpdate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

ProjectAutoUpdate: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ProjectAutoUpdate) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProjectAutoUpdate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectAutoUpdate value: {data!r}")
    return cast(ProjectAutoUpdate, data)
