"""Generated from Smithy shape ``com.amazonaws.gamelift#FlexMatchMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

FlexMatchMode: TypeAlias = Literal[
    "STANDALONE",
    "WITH_QUEUE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDALONE",
        "WITH_QUEUE",
    )
)


def serialize_aws_json_1_1(value: FlexMatchMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlexMatchMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlexMatchMode value: {data!r}")
    return cast(FlexMatchMode, data)
