"""Generated from Smithy shape ``com.amazonaws.batch#FairshareCapacityUtilization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.fairshare_capacity_usage_list
    import aws_sdk_batch.types.string


class FairshareCapacityUtilization(TypedDict):
    share_identifier: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The share identifier for the fairshare scheduling job queue.</p>"""
    capacity_usage: NotRequired[
        "aws_sdk_batch.types.fairshare_capacity_usage_list.FairshareCapacityUsageList"
    ]
    """<p>The capacity usage information for this share, including the unit of measure and quantity being used. This is <code>VCPU</code> for Amazon EC2 and <code>cpu</code> for Amazon EKS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FairshareCapacityUtilization) -> dict:
    out: dict = {}
    if "share_identifier" in value:
        out["shareIdentifier"] = value["share_identifier"]
    if "capacity_usage" in value:
        import aws_sdk_batch.types.fairshare_capacity_usage_list

        out["capacityUsage"] = (
            aws_sdk_batch.types.fairshare_capacity_usage_list.serialize_json(
                value["capacity_usage"]
            )
        )
    return out


def deserialize_json(data: dict) -> FairshareCapacityUtilization:
    out: FairshareCapacityUtilization = {}  # type: ignore[typeddict-item]
    if "shareIdentifier" in data:
        out["share_identifier"] = data["shareIdentifier"]
    if "capacityUsage" in data:
        import aws_sdk_batch.types.fairshare_capacity_usage_list

        out["capacity_usage"] = (
            aws_sdk_batch.types.fairshare_capacity_usage_list.deserialize_json(
                data["capacityUsage"]
            )
        )
    return out
