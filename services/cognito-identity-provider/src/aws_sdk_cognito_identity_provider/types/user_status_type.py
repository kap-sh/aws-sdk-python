"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

UserStatusType: TypeAlias = Literal[
    "UNCONFIRMED",
    "CONFIRMED",
    "ARCHIVED",
    "COMPROMISED",
    "UNKNOWN",
    "RESET_REQUIRED",
    "FORCE_CHANGE_PASSWORD",
    "EXTERNAL_PROVIDER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNCONFIRMED",
        "CONFIRMED",
        "ARCHIVED",
        "COMPROMISED",
        "UNKNOWN",
        "RESET_REQUIRED",
        "FORCE_CHANGE_PASSWORD",
        "EXTERNAL_PROVIDER",
    )
)


def serialize_aws_json_1_1(value: UserStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserStatusType value: {data!r}")
    return cast(UserStatusType, data)
