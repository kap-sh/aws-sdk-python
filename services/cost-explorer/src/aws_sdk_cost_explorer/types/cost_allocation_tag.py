"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAllocationTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_allocation_tag_status
    import aws_sdk_cost_explorer.types.cost_allocation_tag_type
    import aws_sdk_cost_explorer.types.tag_key
    import aws_sdk_cost_explorer.types.zoned_date_time


class CostAllocationTag(TypedDict, closed=True):
    tag_key: "aws_sdk_cost_explorer.types.tag_key.TagKey"
    """<p>The key for the cost allocation tag. </p>"""
    type: "aws_sdk_cost_explorer.types.cost_allocation_tag_type.CostAllocationTagType"
    """<p>The type of cost allocation tag. You can use <code>AWSGenerated</code> or <code>UserDefined</code> type tags. <code>AWSGenerated</code> type tags are tags that Amazon Web Services defines and applies to support Amazon Web Services resources for cost allocation purposes. <code>UserDefined</code> type tags are tags that you define, create, and apply to resources. </p>"""
    status: (
        "aws_sdk_cost_explorer.types.cost_allocation_tag_status.CostAllocationTagStatus"
    )
    """<p>The status of a cost allocation tag. </p>"""
    last_updated_date: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The last date that the tag was either activated or deactivated.</p>"""
    last_used_date: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The last month that the tag was used on an Amazon Web Services resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAllocationTag) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    import aws_sdk_cost_explorer.types.cost_allocation_tag_type

    out["Type"] = (
        aws_sdk_cost_explorer.types.cost_allocation_tag_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    import aws_sdk_cost_explorer.types.cost_allocation_tag_status

    out["Status"] = (
        aws_sdk_cost_explorer.types.cost_allocation_tag_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "last_updated_date" in value:
        out["LastUpdatedDate"] = value["last_updated_date"]
    if "last_used_date" in value:
        out["LastUsedDate"] = value["last_used_date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CostAllocationTag:
    out: CostAllocationTag = {}  # type: ignore[typeddict-item]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    else:
        raise DeserializationError("CostAllocationTag.tag_key required")
    if "Type" in data:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_type

        out["type"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("CostAllocationTag.type required")
    if "Status" in data:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_status

        out["status"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CostAllocationTag.status required")
    if "LastUpdatedDate" in data:
        out["last_updated_date"] = data["LastUpdatedDate"]
    if "LastUsedDate" in data:
        out["last_used_date"] = data["LastUsedDate"]
    return out
