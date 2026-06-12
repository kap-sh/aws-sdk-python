"""Generated from Smithy shape ``com.amazonaws.fms#StreamExceptionPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

StreamExceptionPolicy: TypeAlias = Literal[
    "DROP",
    "CONTINUE",
    "REJECT",
    "FMS_IGNORE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DROP",
        "CONTINUE",
        "REJECT",
        "FMS_IGNORE",
    )
)


def serialize_aws_json_1_1(value: StreamExceptionPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StreamExceptionPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamExceptionPolicy value: {data!r}")
    return cast(StreamExceptionPolicy, data)
