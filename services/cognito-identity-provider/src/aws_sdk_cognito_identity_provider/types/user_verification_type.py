"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserVerificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

UserVerificationType: TypeAlias = Literal[
    "required",
    "preferred",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "required",
        "preferred",
    )
)


def serialize_aws_json_1_1(value: UserVerificationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserVerificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserVerificationType value: {data!r}")
    return cast(UserVerificationType, data)
