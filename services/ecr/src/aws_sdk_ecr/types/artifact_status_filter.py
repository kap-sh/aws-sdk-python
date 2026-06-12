"""Generated from Smithy shape ``com.amazonaws.ecr#ArtifactStatusFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ArtifactStatusFilter: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ACTIVATING",
    "ANY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ARCHIVED",
        "ACTIVATING",
        "ANY",
    )
)


def serialize_aws_json_1_1(value: ArtifactStatusFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactStatusFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactStatusFilter value: {data!r}")
    return cast(ArtifactStatusFilter, data)
