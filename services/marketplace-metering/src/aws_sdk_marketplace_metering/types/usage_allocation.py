"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#UsageAllocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_metering.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.allocated_usage_quantity
    import aws_sdk_marketplace_metering.types.tag_list


class UsageAllocation(TypedDict):
    allocated_usage_quantity: "aws_sdk_marketplace_metering.types.allocated_usage_quantity.AllocatedUsageQuantity"
    """<p>The total quantity allocated to this bucket of usage.</p>"""
    tags: NotRequired["aws_sdk_marketplace_metering.types.tag_list.TagList"]
    """<p>The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageAllocation) -> dict:
    out: dict = {}
    out["AllocatedUsageQuantity"] = value["allocated_usage_quantity"]
    if "tags" in value:
        import aws_sdk_marketplace_metering.types.tag_list

        out["Tags"] = (
            aws_sdk_marketplace_metering.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UsageAllocation:
    out: UsageAllocation = {}  # type: ignore[typeddict-item]
    if "AllocatedUsageQuantity" in data:
        out["allocated_usage_quantity"] = data["AllocatedUsageQuantity"]
    else:
        raise DeserializationError("UsageAllocation.allocated_usage_quantity required")
    if "Tags" in data:
        import aws_sdk_marketplace_metering.types.tag_list

        out["tags"] = (
            aws_sdk_marketplace_metering.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    return out
