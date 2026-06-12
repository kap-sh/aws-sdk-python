"""Generated from Smithy shape ``com.amazonaws.ecr#ArtifactStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ArtifactStatus: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ACTIVATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ARCHIVED",
        "ACTIVATING",
    )
)


def serialize_aws_json_1_1(value: ArtifactStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactStatus value: {data!r}")
    return cast(ArtifactStatus, data)
