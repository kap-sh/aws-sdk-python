"""Generated from Smithy shape ``com.amazonaws.ssm#NotificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

NotificationType: TypeAlias = Literal[
    "Command",
    "Invocation",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Command",
        "Invocation",
    )
)


def serialize_aws_json_1_1(value: NotificationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationType value: {data!r}")
    return cast(NotificationType, data)
