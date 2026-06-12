"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListUpdateMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

ListUpdateMode: TypeAlias = Literal[
    "REPLACE",
    "APPEND",
    "REMOVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REPLACE",
        "APPEND",
        "REMOVE",
    )
)


def serialize_aws_json_1_1(value: ListUpdateMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListUpdateMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListUpdateMode value: {data!r}")
    return cast(ListUpdateMode, data)
