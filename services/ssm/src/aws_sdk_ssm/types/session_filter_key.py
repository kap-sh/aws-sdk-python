"""Generated from Smithy shape ``com.amazonaws.ssm#SessionFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

SessionFilterKey: TypeAlias = Literal[
    "InvokedAfter",
    "InvokedBefore",
    "Target",
    "Owner",
    "Status",
    "SessionId",
    "AccessType",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvokedAfter",
        "InvokedBefore",
        "Target",
        "Owner",
        "Status",
        "SessionId",
        "AccessType",
    )
)


def serialize_aws_json_1_1(value: SessionFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SessionFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionFilterKey value: {data!r}")
    return cast(SessionFilterKey, data)
