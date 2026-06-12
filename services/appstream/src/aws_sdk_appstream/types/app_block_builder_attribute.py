"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilderAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

AppBlockBuilderAttribute: TypeAlias = Literal[
    "IAM_ROLE_ARN",
    "ACCESS_ENDPOINTS",
    "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM_ROLE_ARN",
        "ACCESS_ENDPOINTS",
        "VPC_CONFIGURATION_SECURITY_GROUP_IDS",
    )
)


def serialize_aws_json_1_1(value: AppBlockBuilderAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppBlockBuilderAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppBlockBuilderAttribute value: {data!r}")
    return cast(AppBlockBuilderAttribute, data)
