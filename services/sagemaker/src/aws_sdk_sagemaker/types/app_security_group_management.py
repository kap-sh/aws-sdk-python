"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppSecurityGroupManagement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AppSecurityGroupManagement: TypeAlias = Literal[
    "Service",
    "Customer",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Service",
        "Customer",
    )
)


def serialize_aws_json_1_1(value: AppSecurityGroupManagement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppSecurityGroupManagement:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AppSecurityGroupManagement value: {data!r}"
        )
    return cast(AppSecurityGroupManagement, data)
