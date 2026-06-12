"""Generated from Smithy shape ``com.amazonaws.appstream#UsageReportSchedule``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

UsageReportSchedule: TypeAlias = Literal["DAILY",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DAILY",))


def serialize_aws_json_1_1(value: UsageReportSchedule) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsageReportSchedule:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageReportSchedule value: {data!r}")
    return cast(UsageReportSchedule, data)
