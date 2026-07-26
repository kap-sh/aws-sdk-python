"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_metering.types.usage_record

UsageRecordList: TypeAlias = list[
    "capo_marketplace_metering.types.usage_record.UsageRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageRecordList) -> list:
    import capo_marketplace_metering.types.usage_record

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_metering.types.usage_record.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsageRecordList:
    import capo_marketplace_metering.types.usage_record

    out: UsageRecordList = []
    for item in data:
        out.append(
            capo_marketplace_metering.types.usage_record.deserialize_aws_json_1_1(item)
        )
    return out
