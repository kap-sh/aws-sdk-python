"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareCapacityUtilization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.quota_share_capacity_usage_list
    import aws_sdk_batch.types.string


class QuotaShareCapacityUtilization(TypedDict):
    quota_share_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the quota share.</p>"""
    capacity_usage: NotRequired[
        "aws_sdk_batch.types.quota_share_capacity_usage_list.QuotaShareCapacityUsageList"
    ]
    """<p>The capacity usage information for this quota share, including the units of compute capacity and quantity being used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareCapacityUtilization) -> dict:
    out: dict = {}
    if "quota_share_name" in value:
        out["quotaShareName"] = value["quota_share_name"]
    if "capacity_usage" in value:
        import aws_sdk_batch.types.quota_share_capacity_usage_list

        out["capacityUsage"] = (
            aws_sdk_batch.types.quota_share_capacity_usage_list.serialize_json(
                value["capacity_usage"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuotaShareCapacityUtilization:
    out: QuotaShareCapacityUtilization = {}  # type: ignore[typeddict-item]
    if "quotaShareName" in data:
        out["quota_share_name"] = data["quotaShareName"]
    if "capacityUsage" in data:
        import aws_sdk_batch.types.quota_share_capacity_usage_list

        out["capacity_usage"] = (
            aws_sdk_batch.types.quota_share_capacity_usage_list.deserialize_json(
                data["capacityUsage"]
            )
        )
    return out
