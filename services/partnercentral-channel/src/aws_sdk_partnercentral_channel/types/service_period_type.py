"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ServicePeriodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

ServicePeriodType: TypeAlias = Literal[
    "MINIMUM_NOTICE_PERIOD",
    "FIXED_COMMITMENT_PERIOD",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MINIMUM_NOTICE_PERIOD",
        "FIXED_COMMITMENT_PERIOD",
    )
)


def serialize_aws_json_1_0(value: ServicePeriodType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ServicePeriodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServicePeriodType value: {data!r}")
    return cast(ServicePeriodType, data)
