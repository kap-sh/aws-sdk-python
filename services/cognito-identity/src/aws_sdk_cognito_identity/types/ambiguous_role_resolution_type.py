"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#AmbiguousRoleResolutionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity.errors import DeserializationError

AmbiguousRoleResolutionType: TypeAlias = Literal[
    "AuthenticatedRole",
    "Deny",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AuthenticatedRole",
        "Deny",
    )
)


def serialize_aws_json_1_1(value: AmbiguousRoleResolutionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AmbiguousRoleResolutionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AmbiguousRoleResolutionType value: {data!r}"
        )
    return cast(AmbiguousRoleResolutionType, data)
