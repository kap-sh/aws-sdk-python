"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.asset_id
    import capo_outposts.types.capacity_task_id
    import capo_outposts.types.capacity_task_status
    import capo_outposts.types.iso8601_timestamp
    import capo_outposts.types.order_id
    import capo_outposts.types.outpost_id


class CapacityTaskSummary(TypedDict, closed=True):
    capacity_task_id: NotRequired["capo_outposts.types.capacity_task_id.CapacityTaskId"]
    """<p>The ID of the specified capacity task.</p>"""
    outpost_id: NotRequired["capo_outposts.types.outpost_id.OutpostId"]
    """<p>The ID of the Outpost associated with the specified capacity task.</p>"""
    order_id: NotRequired["capo_outposts.types.order_id.OrderId"]
    """<p>The ID of the Amazon Web Services Outposts order of the host associated with the capacity task.</p>"""
    asset_id: NotRequired["capo_outposts.types.asset_id.AssetId"]
    """<p>The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    capacity_task_status: NotRequired[
        "capo_outposts.types.capacity_task_status.CapacityTaskStatus"
    ]
    """<p>The status of the capacity task.</p>"""
    creation_date: NotRequired["capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"]
    """<p>The date that the specified capacity task was created.</p>"""
    completion_date: NotRequired[
        "capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The date that the specified capacity task successfully ran.</p>"""
    last_modified_date: NotRequired[
        "capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"
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
        import capo_outposts.types.capacity_task_status

        out["CapacityTaskStatus"] = (
            capo_outposts.types.capacity_task_status.serialize_json(
                value["capacity_task_status"]
            )
        )
    if "creation_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["CreationDate"] = capo_outposts.types.iso8601_timestamp.serialize_json(
            value["creation_date"]
        )
    if "completion_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["CompletionDate"] = capo_outposts.types.iso8601_timestamp.serialize_json(
            value["completion_date"]
        )
    if "last_modified_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["LastModifiedDate"] = capo_outposts.types.iso8601_timestamp.serialize_json(
            value["last_modified_date"]
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
        import capo_outposts.types.capacity_task_status

        out["capacity_task_status"] = (
            capo_outposts.types.capacity_task_status.deserialize_json(
                data["CapacityTaskStatus"]
            )
        )
    if "CreationDate" in data:
        import capo_outposts.types.iso8601_timestamp

        out["creation_date"] = capo_outposts.types.iso8601_timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "CompletionDate" in data:
        import capo_outposts.types.iso8601_timestamp

        out["completion_date"] = capo_outposts.types.iso8601_timestamp.deserialize_json(
            data["CompletionDate"]
        )
    if "LastModifiedDate" in data:
        import capo_outposts.types.iso8601_timestamp

        out["last_modified_date"] = (
            capo_outposts.types.iso8601_timestamp.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    return out
