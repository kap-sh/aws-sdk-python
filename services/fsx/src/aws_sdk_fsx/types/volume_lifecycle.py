"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

VolumeLifecycle: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
    "FAILED",
    "MISCONFIGURED",
    "PENDING",
    "AVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "DELETING",
        "FAILED",
        "MISCONFIGURED",
        "PENDING",
        "AVAILABLE",
    )
)


def serialize_aws_json_1_1(value: VolumeLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeLifecycle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VolumeLifecycle value: {data!r}")
    return cast(VolumeLifecycle, data)
