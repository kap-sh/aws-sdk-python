"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ChallengeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

ChallengeName: TypeAlias = Literal[
    "Password",
    "Mfa",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Password",
        "Mfa",
    )
)


def serialize_aws_json_1_1(value: ChallengeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChallengeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChallengeName value: {data!r}")
    return cast(ChallengeName, data)
