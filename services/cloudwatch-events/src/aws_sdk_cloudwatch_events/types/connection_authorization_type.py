"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionAuthorizationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_events.errors import DeserializationError

ConnectionAuthorizationType: TypeAlias = Literal[
    "BASIC",
    "OAUTH_CLIENT_CREDENTIALS",
    "API_KEY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "OAUTH_CLIENT_CREDENTIALS",
        "API_KEY",
    )
)


def serialize_aws_json_1_1(value: ConnectionAuthorizationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionAuthorizationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConnectionAuthorizationType value: {data!r}"
        )
    return cast(ConnectionAuthorizationType, data)
