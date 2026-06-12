"""Generated from Smithy shape ``com.amazonaws.comprehend#Split``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

Split: TypeAlias = Literal[
    "TRAIN",
    "TEST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRAIN",
        "TEST",
    )
)


def serialize_aws_json_1_1(value: Split) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Split:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Split value: {data!r}")
    return cast(Split, data)
