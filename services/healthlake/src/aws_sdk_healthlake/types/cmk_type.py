"""Generated from Smithy shape ``com.amazonaws.healthlake#CmkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_healthlake.errors import DeserializationError

CmkType: TypeAlias = Literal[
    "CUSTOMER_MANAGED_KMS_KEY",
    "AWS_OWNED_KMS_KEY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_MANAGED_KMS_KEY",
        "AWS_OWNED_KMS_KEY",
    )
)


def serialize_aws_json_1_0(value: CmkType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CmkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmkType value: {data!r}")
    return cast(CmkType, data)
