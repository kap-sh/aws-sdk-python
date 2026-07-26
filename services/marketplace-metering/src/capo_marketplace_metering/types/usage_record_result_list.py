"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageRecordResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_metering.types.usage_record_result

UsageRecordResultList: TypeAlias = list[
    "capo_marketplace_metering.types.usage_record_result.UsageRecordResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageRecordResultList) -> list:
    import capo_marketplace_metering.types.usage_record_result

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_metering.types.usage_record_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsageRecordResultList:
    import capo_marketplace_metering.types.usage_record_result

    out: UsageRecordResultList = []
    for item in data:
        out.append(
            capo_marketplace_metering.types.usage_record_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
