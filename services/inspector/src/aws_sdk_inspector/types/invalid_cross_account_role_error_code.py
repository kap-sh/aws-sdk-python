"""Generated from Smithy shape ``com.amazonaws.inspector#InvalidCrossAccountRoleErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

InvalidCrossAccountRoleErrorCode: TypeAlias = Literal[
    "ROLE_DOES_NOT_EXIST_OR_INVALID_TRUST_RELATIONSHIP",
    "ROLE_DOES_NOT_HAVE_CORRECT_POLICY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROLE_DOES_NOT_EXIST_OR_INVALID_TRUST_RELATIONSHIP",
        "ROLE_DOES_NOT_HAVE_CORRECT_POLICY",
    )
)


def serialize_aws_json_1_1(value: InvalidCrossAccountRoleErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InvalidCrossAccountRoleErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InvalidCrossAccountRoleErrorCode value: {data!r}"
        )
    return cast(InvalidCrossAccountRoleErrorCode, data)
