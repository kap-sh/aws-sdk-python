"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageAllocations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.usage_allocation

UsageAllocations: TypeAlias = list[
    "aws_sdk_marketplace_metering.types.usage_allocation.UsageAllocation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageAllocations) -> list:
    import aws_sdk_marketplace_metering.types.usage_allocation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_metering.types.usage_allocation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsageAllocations:
    import aws_sdk_marketplace_metering.types.usage_allocation

    out: UsageAllocations = []
    for item in data:
        out.append(
            aws_sdk_marketplace_metering.types.usage_allocation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
