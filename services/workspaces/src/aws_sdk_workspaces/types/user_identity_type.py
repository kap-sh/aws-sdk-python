"""Generated from Smithy shape ``com.amazonaws.workspaces#UserIdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

UserIdentityType: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_DIRECTORY_SERVICE",
    "AWS_IAM_IDENTITY_CENTER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_MANAGED",
        "AWS_DIRECTORY_SERVICE",
        "AWS_IAM_IDENTITY_CENTER",
    )
)


def serialize_aws_json_1_1(value: UserIdentityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserIdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserIdentityType value: {data!r}")
    return cast(UserIdentityType, data)
