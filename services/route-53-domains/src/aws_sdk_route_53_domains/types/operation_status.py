"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

OperationStatus: TypeAlias = Literal[
    "SUBMITTED",
    "IN_PROGRESS",
    "ERROR",
    "SUCCESSFUL",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "IN_PROGRESS",
        "ERROR",
        "SUCCESSFUL",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: OperationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationStatus value: {data!r}")
    return cast(OperationStatus, data)
