"""Generated from Smithy shape ``com.amazonaws.servicequotas#RequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_quotas.errors import DeserializationError

RequestStatus: TypeAlias = Literal[
    "PENDING",
    "CASE_OPENED",
    "APPROVED",
    "DENIED",
    "CASE_CLOSED",
    "NOT_APPROVED",
    "INVALID_REQUEST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "CASE_OPENED",
        "APPROVED",
        "DENIED",
        "CASE_CLOSED",
        "NOT_APPROVED",
        "INVALID_REQUEST",
    )
)


def serialize_aws_json_1_1(value: RequestStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RequestStatus value: {data!r}")
    return cast(RequestStatus, data)
