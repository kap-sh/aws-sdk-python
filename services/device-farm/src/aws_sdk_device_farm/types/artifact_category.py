"""Generated from Smithy shape ``com.amazonaws.devicefarm#ArtifactCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

ArtifactCategory: TypeAlias = Literal[
    "SCREENSHOT",
    "FILE",
    "LOG",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCREENSHOT",
        "FILE",
        "LOG",
    )
)


def serialize_aws_json_1_1(value: ArtifactCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactCategory value: {data!r}")
    return cast(ArtifactCategory, data)
