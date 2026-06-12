"""Generated from Smithy shape ``com.amazonaws.ssm#AccessRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AccessRequestStatus: TypeAlias = Literal[
    "Approved",
    "Rejected",
    "Revoked",
    "Expired",
    "Pending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Approved",
        "Rejected",
        "Revoked",
        "Expired",
        "Pending",
    )
)


def serialize_aws_json_1_1(value: AccessRequestStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessRequestStatus value: {data!r}")
    return cast(AccessRequestStatus, data)
