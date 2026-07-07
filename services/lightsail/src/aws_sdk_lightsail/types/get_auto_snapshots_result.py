"""Generated from Smithy shape ``com.amazonaws.lightsail#GetAutoSnapshotsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.auto_snapshot_details_list
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type


class GetAutoSnapshotsResult(TypedDict, closed=True):
    resource_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the source instance or disk for the automatic snapshots.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The resource type of the automatic snapshot. The possible values are <code>Instance</code>, and <code>Disk</code>.</p>"""
    auto_snapshots: NotRequired[
        "aws_sdk_lightsail.types.auto_snapshot_details_list.AutoSnapshotDetailsList"
    ]
    """<p>An array of objects that describe the automatic snapshots that are available for the specified source instance or disk.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutoSnapshotsResult) -> dict:
    out: dict = {}
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "resource_type" in value:
        import aws_sdk_lightsail.types.resource_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "auto_snapshots" in value:
        import aws_sdk_lightsail.types.auto_snapshot_details_list

        out["autoSnapshots"] = (
            aws_sdk_lightsail.types.auto_snapshot_details_list.serialize_aws_json_1_1(
                value["auto_snapshots"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutoSnapshotsResult:
    out: GetAutoSnapshotsResult = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "resourceType" in data:
        import aws_sdk_lightsail.types.resource_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "autoSnapshots" in data:
        import aws_sdk_lightsail.types.auto_snapshot_details_list

        out["auto_snapshots"] = (
            aws_sdk_lightsail.types.auto_snapshot_details_list.deserialize_aws_json_1_1(
                data["autoSnapshots"]
            )
        )
    return out
