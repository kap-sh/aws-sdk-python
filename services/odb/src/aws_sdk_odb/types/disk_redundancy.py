"""Generated from Smithy shape ``com.amazonaws.odb#DiskRedundancy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DiskRedundancy: TypeAlias = Literal[
    "HIGH",
    "NORMAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "NORMAL",
    )
)


def serialize_aws_json_1_0(value: DiskRedundancy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DiskRedundancy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiskRedundancy value: {data!r}")
    return cast(DiskRedundancy, data)
