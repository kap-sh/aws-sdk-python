"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ServicePeriodTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.service_period_type

ServicePeriodTypeList: TypeAlias = list[
    "aws_sdk_partnercentral_channel.types.service_period_type.ServicePeriodType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServicePeriodTypeList) -> list:
    import aws_sdk_partnercentral_channel.types.service_period_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_channel.types.service_period_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServicePeriodTypeList:
    import aws_sdk_partnercentral_channel.types.service_period_type

    out: ServicePeriodTypeList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_channel.types.service_period_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
