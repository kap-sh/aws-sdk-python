"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RefreshScheduleFrequencyUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

RefreshScheduleFrequencyUnit: TypeAlias = Literal[
    "HOURS",
    "DAYS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOURS",
        "DAYS",
    )
)


def serialize_aws_json_1_1(value: RefreshScheduleFrequencyUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RefreshScheduleFrequencyUnit:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RefreshScheduleFrequencyUnit value: {data!r}"
        )
    return cast(RefreshScheduleFrequencyUnit, data)
