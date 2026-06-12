"""Generated from Smithy shape ``com.amazonaws.apprunner#VpcIngressConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

VpcIngressConnectionStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING_CREATION",
    "PENDING_UPDATE",
    "PENDING_DELETION",
    "FAILED_CREATION",
    "FAILED_UPDATE",
    "FAILED_DELETION",
    "DELETED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING_CREATION",
        "PENDING_UPDATE",
        "PENDING_DELETION",
        "FAILED_CREATION",
        "FAILED_UPDATE",
        "FAILED_DELETION",
        "DELETED",
    )
)


def serialize_aws_json_1_0(value: VpcIngressConnectionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VpcIngressConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VpcIngressConnectionStatus value: {data!r}"
        )
    return cast(VpcIngressConnectionStatus, data)
