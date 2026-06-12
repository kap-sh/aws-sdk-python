"""Generated from Smithy shape ``com.amazonaws.servicequotas#AppliedLevelEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

AppliedLevelEnum: TypeAlias = Literal[
    "ACCOUNT",
    "RESOURCE",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "RESOURCE",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: AppliedLevelEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppliedLevelEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppliedLevelEnum value: {data!r}")
    return cast(AppliedLevelEnum, data)
