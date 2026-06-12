"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_memorydb.errors import DeserializationError

UpdateStrategy: TypeAlias = Literal[
    "coordinated",
    "uncoordinated",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "coordinated",
        "uncoordinated",
    )
)


def serialize_aws_json_1_1(value: UpdateStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateStrategy value: {data!r}")
    return cast(UpdateStrategy, data)
