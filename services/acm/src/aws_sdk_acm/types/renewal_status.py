"""Generated from Smithy shape ``com.amazonaws.acm#RenewalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

RenewalStatus: TypeAlias = Literal[
    "PENDING_AUTO_RENEWAL",
    "PENDING_VALIDATION",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_AUTO_RENEWAL",
        "PENDING_VALIDATION",
        "SUCCESS",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: RenewalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RenewalStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RenewalStatus value: {data!r}")
    return cast(RenewalStatus, data)
