"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PreventUserExistenceErrorTypes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

PreventUserExistenceErrorTypes: TypeAlias = Literal[
    "LEGACY",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEGACY",
        "ENABLED",
    )
)


def serialize_aws_json_1_1(value: PreventUserExistenceErrorTypes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreventUserExistenceErrorTypes:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PreventUserExistenceErrorTypes value: {data!r}"
        )
    return cast(PreventUserExistenceErrorTypes, data)
