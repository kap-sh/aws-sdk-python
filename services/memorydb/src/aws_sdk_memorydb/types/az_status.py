"""Generated from Smithy shape ``com.amazonaws.memorydb#AZStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_memorydb.errors import DeserializationError

AZStatus: TypeAlias = Literal[
    "singleaz",
    "multiaz",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "singleaz",
        "multiaz",
    )
)


def serialize_aws_json_1_1(value: AZStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AZStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AZStatus value: {data!r}")
    return cast(AZStatus, data)
