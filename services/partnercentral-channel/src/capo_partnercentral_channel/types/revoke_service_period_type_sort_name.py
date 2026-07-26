"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RevokeServicePeriodTypeSortName``."""

from typing import Literal, TypeAlias, cast

RevokeServicePeriodTypeSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RevokeServicePeriodTypeSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RevokeServicePeriodTypeSortName:
    return cast(RevokeServicePeriodTypeSortName, data)
