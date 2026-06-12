"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageRecordResultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_metering.errors import DeserializationError

UsageRecordResultStatus: TypeAlias = Literal[
    "Success",
    "CustomerNotSubscribed",
    "DuplicateRecord",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Success",
        "CustomerNotSubscribed",
        "DuplicateRecord",
    )
)


def serialize_aws_json_1_1(value: UsageRecordResultStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsageRecordResultStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageRecordResultStatus value: {data!r}")
    return cast(UsageRecordResultStatus, data)
