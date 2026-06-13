"""Generated from Smithy shape ``com.amazonaws.mailmanager#LambdaInvocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

LambdaInvocationType: TypeAlias = Literal[
    "EVENT",
    "REQUEST_RESPONSE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EVENT",
        "REQUEST_RESPONSE",
    )
)


def serialize_aws_json_1_0(value: LambdaInvocationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaInvocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LambdaInvocationType value: {data!r}")
    return cast(LambdaInvocationType, data)
