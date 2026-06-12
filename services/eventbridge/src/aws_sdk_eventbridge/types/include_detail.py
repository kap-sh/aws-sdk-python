"""Generated from Smithy shape ``com.amazonaws.eventbridge#IncludeDetail``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eventbridge.errors import DeserializationError

IncludeDetail: TypeAlias = Literal[
    "NONE",
    "FULL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "FULL",
    )
)


def serialize_aws_json_1_1(value: IncludeDetail) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IncludeDetail:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludeDetail value: {data!r}")
    return cast(IncludeDetail, data)
