"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DefaultEmailOptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

DefaultEmailOptionType: TypeAlias = Literal[
    "CONFIRM_WITH_LINK",
    "CONFIRM_WITH_CODE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONFIRM_WITH_LINK",
        "CONFIRM_WITH_CODE",
    )
)


def serialize_aws_json_1_1(value: DefaultEmailOptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DefaultEmailOptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefaultEmailOptionType value: {data!r}")
    return cast(DefaultEmailOptionType, data)
