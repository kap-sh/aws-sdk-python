"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#StartServicePeriodTypeSortName``."""

from typing import Literal, TypeAlias, cast

StartServicePeriodTypeSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartServicePeriodTypeSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StartServicePeriodTypeSortName:
    return cast(StartServicePeriodTypeSortName, data)
