"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ProfileTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

ProfileTaskStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELED",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "CANCELED",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: ProfileTaskStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProfileTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileTaskStatus value: {data!r}")
    return cast(ProfileTaskStatus, data)
