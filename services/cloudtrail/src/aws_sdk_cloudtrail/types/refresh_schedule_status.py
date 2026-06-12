"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RefreshScheduleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

RefreshScheduleStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: RefreshScheduleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RefreshScheduleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RefreshScheduleStatus value: {data!r}")
    return cast(RefreshScheduleStatus, data)
