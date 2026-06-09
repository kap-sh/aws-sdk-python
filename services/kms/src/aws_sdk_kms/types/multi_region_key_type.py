"""Generated from Smithy shape ``com.amazonaws.kms#MultiRegionKeyType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

MultiRegionKeyType: TypeAlias = Literal[
    "PRIMARY",
    "REPLICA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "REPLICA",
    )
)


def serialize_aws_json_1_1(value: MultiRegionKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MultiRegionKeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MultiRegionKeyType value: {data!r}")
    return cast(MultiRegionKeyType, data)
