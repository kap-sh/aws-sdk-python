"""Generated from Smithy shape ``com.amazonaws.glue#DataOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DataOperation: TypeAlias = Literal[
    "READ",
    "WRITE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ",
        "WRITE",
    )
)


def serialize_aws_json_1_1(value: DataOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataOperation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataOperation value: {data!r}")
    return cast(DataOperation, data)
