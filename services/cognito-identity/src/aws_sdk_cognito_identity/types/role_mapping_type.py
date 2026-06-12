"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#RoleMappingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity.errors import DeserializationError

RoleMappingType: TypeAlias = Literal[
    "Token",
    "Rules",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Token",
        "Rules",
    )
)


def serialize_aws_json_1_1(value: RoleMappingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RoleMappingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoleMappingType value: {data!r}")
    return cast(RoleMappingType, data)
