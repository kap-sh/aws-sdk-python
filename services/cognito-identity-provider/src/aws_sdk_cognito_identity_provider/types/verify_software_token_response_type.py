"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#VerifySoftwareTokenResponseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

VerifySoftwareTokenResponseType: TypeAlias = Literal[
    "SUCCESS",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: VerifySoftwareTokenResponseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VerifySoftwareTokenResponseType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VerifySoftwareTokenResponseType value: {data!r}"
        )
    return cast(VerifySoftwareTokenResponseType, data)
