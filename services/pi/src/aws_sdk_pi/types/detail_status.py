"""Generated from Smithy shape ``com.amazonaws.pi#DetailStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

DetailStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PROCESSING",
    "UNAVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PROCESSING",
        "UNAVAILABLE",
    )
)


def serialize_aws_json_1_1(value: DetailStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetailStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetailStatus value: {data!r}")
    return cast(DetailStatus, data)
