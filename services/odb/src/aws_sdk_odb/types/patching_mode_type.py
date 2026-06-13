"""Generated from Smithy shape ``com.amazonaws.odb#PatchingModeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

PatchingModeType: TypeAlias = Literal[
    "ROLLING",
    "NONROLLING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROLLING",
        "NONROLLING",
    )
)


def serialize_aws_json_1_0(value: PatchingModeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PatchingModeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchingModeType value: {data!r}")
    return cast(PatchingModeType, data)
