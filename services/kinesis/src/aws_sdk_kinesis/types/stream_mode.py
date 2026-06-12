"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis.errors import DeserializationError

StreamMode: TypeAlias = Literal[
    "PROVISIONED",
    "ON_DEMAND",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONED",
        "ON_DEMAND",
    )
)


def serialize_aws_json_1_1(value: StreamMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamMode value: {data!r}")
    return cast(StreamMode, data)
