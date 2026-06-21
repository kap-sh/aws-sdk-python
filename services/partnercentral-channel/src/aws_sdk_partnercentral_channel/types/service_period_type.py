"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ServicePeriodType``."""

from typing import Literal, TypeAlias, cast

ServicePeriodType: TypeAlias = Literal[
    "MINIMUM_NOTICE_PERIOD",
    "FIXED_COMMITMENT_PERIOD",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServicePeriodType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ServicePeriodType:
    return cast(ServicePeriodType, data)
