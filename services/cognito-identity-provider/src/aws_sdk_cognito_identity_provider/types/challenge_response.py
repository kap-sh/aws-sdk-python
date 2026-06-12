"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ChallengeResponse``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

ChallengeResponse: TypeAlias = Literal[
    "Success",
    "Failure",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Success",
        "Failure",
    )
)


def serialize_aws_json_1_1(value: ChallengeResponse) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChallengeResponse:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChallengeResponse value: {data!r}")
    return cast(ChallengeResponse, data)
