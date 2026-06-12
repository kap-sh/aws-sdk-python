"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserImportJobStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

UserImportJobStatusType: TypeAlias = Literal[
    "Created",
    "Pending",
    "InProgress",
    "Stopping",
    "Expired",
    "Stopped",
    "Failed",
    "Succeeded",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Created",
        "Pending",
        "InProgress",
        "Stopping",
        "Expired",
        "Stopped",
        "Failed",
        "Succeeded",
    )
)


def serialize_aws_json_1_1(value: UserImportJobStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserImportJobStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserImportJobStatusType value: {data!r}")
    return cast(UserImportJobStatusType, data)
