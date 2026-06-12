"""Generated from Smithy shape ``com.amazonaws.glue#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

AuthenticationType: TypeAlias = Literal[
    "BASIC",
    "OAUTH2",
    "CUSTOM",
    "IAM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "OAUTH2",
        "CUSTOM",
        "IAM",
    )
)


def serialize_aws_json_1_1(value: AuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {data!r}")
    return cast(AuthenticationType, data)
