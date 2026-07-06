"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_id
    import aws_sdk_outposts.types.capacity_task_id
    import aws_sdk_outposts.types.capacity_task_status
    import aws_sdk_outposts.types.iso8601_timestamp
    import aws_sdk_outposts.types.order_id
    import aws_sdk_outposts.types.outpost_id


class CapacityTaskSummary(TypedDict, closed=True):
    capacity_task_id: NotRequired[
        "aws_sdk_outposts.types.capacity_task_id.CapacityTaskId"
    ]
    """<p>The ID of the specified capacity task.</p>"""
    outpost_id: NotRequired["aws_sdk_outposts.types.outpost_id.OutpostId"]
    """<p>The ID of the Outpost associated with the specified capacity task.</p>"""
    order_id: NotRequired["aws_sdk_outposts.types.order_id.OrderId"]
    """<p>The ID of the Amazon Web Services Outposts order of the host associated with the capacity task.</p>"""
    asset_id: NotRequired["aws_sdk_outposts.types.asset_id.AssetId"]
    """<p>The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    capacity_task_status: NotRequired[
        "aws_sdk_outposts.types.capacity_task_status.CapacityTaskStatus"
    ]
    """<p>The status of the capacity task.</p>"""
    creation_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The date that the specified capacity task was created.</p>"""
    completion_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The date that the specified capacity task successfully ran.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The date that the specified capacity was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityTaskSummary) -> dict:
    out: dict = {}
    if "capacity_task_id" in value:
        out["CapacityTaskId"] = value["capacity_task_id"]
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    if "order_id" in value:
        out["OrderId"] = value["order_id"]
    if "asset_id" in value:
        out["AssetId"] = value["asset_id"]
    if "capacity_task_status" in value:
        import aws_sdk_outposts.types.capacity_task_status

        out["CapacityTaskStatus"] = (
            aws_sdk_outposts.types.capacity_task_status.serialize_json(
                value["capacity_task_status"]
            )
        )
    if "creation_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["CreationDate"] = aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
            value["creation_date"]
        )
    if "completion_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["CompletionDate"] = aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
            value["completion_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["LastModifiedDate"] = (
            aws_sdk_outposts.types.iso8601_timestamp.serialize_json(
                value["last_modified_date"]
            )
        )
    return out


def deserialize_json(data: dict) -> CapacityTaskSummary:
    out: CapacityTaskSummary = {}  # type: ignore[typeddict-item]
    if "CapacityTaskId" in data:
        out["capacity_task_id"] = data["CapacityTaskId"]
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    if "OrderId" in data:
        out["order_id"] = data["OrderId"]
    if "AssetId" in data:
        out["asset_id"] = data["AssetId"]
    if "CapacityTaskStatus" in data:
        import aws_sdk_outposts.types.capacity_task_status

        out["capacity_task_status"] = (
            aws_sdk_outposts.types.capacity_task_status.deserialize_json(
                data["CapacityTaskStatus"]
            )
        )
    if "CreationDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["creation_date"] = (
            aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
                data["CreationDate"]
            )
        )
    if "CompletionDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["completion_date"] = (
            aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
                data["CompletionDate"]
            )
        )
    if "LastModifiedDate" in data:
        import aws_sdk_outposts.types.iso8601_timestamp

        out["last_modified_date"] = (
            aws_sdk_outposts.types.iso8601_timestamp.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    return out
