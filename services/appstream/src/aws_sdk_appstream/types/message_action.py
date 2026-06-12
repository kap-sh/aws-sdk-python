"""Generated from Smithy shape ``com.amazonaws.appstream#MessageAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

MessageAction: TypeAlias = Literal[
    "SUPPRESS",
    "RESEND",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUPPRESS",
        "RESEND",
    )
)


def serialize_aws_json_1_1(value: MessageAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MessageAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageAction value: {data!r}")
    return cast(MessageAction, data)
