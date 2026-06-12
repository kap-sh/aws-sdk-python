"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ProvisionTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

ProvisionTargetType: TypeAlias = Literal[
    "AWS_ACCOUNT",
    "ALL_PROVISIONED_ACCOUNTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_ACCOUNT",
        "ALL_PROVISIONED_ACCOUNTS",
    )
)


def serialize_aws_json_1_1(value: ProvisionTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionTargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisionTargetType value: {data!r}")
    return cast(ProvisionTargetType, data)
