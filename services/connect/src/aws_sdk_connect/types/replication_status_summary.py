"""Generated from Smithy shape ``com.amazonaws.connect#ReplicationStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.aws_region
    import aws_sdk_connect.types.instance_replication_status
    import aws_sdk_connect.types.replication_status_reason


class ReplicationStatusSummary(TypedDict, closed=True):
    region: NotRequired["aws_sdk_connect.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region. This can be either the source or the replica Region, depending where it appears in the summary list.</p>"""
    replication_status: NotRequired[
        "aws_sdk_connect.types.instance_replication_status.InstanceReplicationStatus"
    ]
    """<p>The state of the replication.</p>"""
    replication_status_reason: NotRequired[
        "aws_sdk_connect.types.replication_status_reason.ReplicationStatusReason"
    ]
    """<p>A description of the replication status. Use this information to resolve any issues that are preventing the successful replication of your Connect Customer instance to another Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationStatusSummary) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "replication_status" in value:
        import aws_sdk_connect.types.instance_replication_status

        out["ReplicationStatus"] = (
            aws_sdk_connect.types.instance_replication_status.serialize_json(
                value["replication_status"]
            )
        )
    if "replication_status_reason" in value:
        out["ReplicationStatusReason"] = value["replication_status_reason"]
    return out


def deserialize_json(data: dict) -> ReplicationStatusSummary:
    out: ReplicationStatusSummary = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "ReplicationStatus" in data:
        import aws_sdk_connect.types.instance_replication_status

        out["replication_status"] = (
            aws_sdk_connect.types.instance_replication_status.deserialize_json(
                data["ReplicationStatus"]
            )
        )
    if "ReplicationStatusReason" in data:
        out["replication_status_reason"] = data["ReplicationStatusReason"]
    return out
