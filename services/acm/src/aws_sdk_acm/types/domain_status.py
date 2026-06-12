"""Generated from Smithy shape ``com.amazonaws.acm#DomainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

DomainStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_VALIDATION",
        "SUCCESS",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: DomainStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainStatus value: {data!r}")
    return cast(DomainStatus, data)
