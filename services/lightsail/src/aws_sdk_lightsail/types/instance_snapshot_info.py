"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceSnapshotInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.disk_info_list
    import aws_sdk_lightsail.types.non_empty_string


class InstanceSnapshotInfo(TypedDict, closed=True):
    from_bundle_id: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The bundle ID from which the source instance was created (<code>micro_x_x</code>).</p>"""
    from_blueprint_id: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The blueprint ID from which the source instance (<code>amazon_linux_2023</code>).</p>"""
    from_disk_info: NotRequired["aws_sdk_lightsail.types.disk_info_list.DiskInfoList"]
    """<p>A list of objects describing the disks that were attached to the source instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceSnapshotInfo) -> dict:
    out: dict = {}
    if "from_bundle_id" in value:
        out["fromBundleId"] = value["from_bundle_id"]
    if "from_blueprint_id" in value:
        out["fromBlueprintId"] = value["from_blueprint_id"]
    if "from_disk_info" in value:
        import aws_sdk_lightsail.types.disk_info_list

        out["fromDiskInfo"] = (
            aws_sdk_lightsail.types.disk_info_list.serialize_aws_json_1_1(
                value["from_disk_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceSnapshotInfo:
    out: InstanceSnapshotInfo = {}  # type: ignore[typeddict-item]
    if "fromBundleId" in data:
        out["from_bundle_id"] = data["fromBundleId"]
    if "fromBlueprintId" in data:
        out["from_blueprint_id"] = data["fromBlueprintId"]
    if "fromDiskInfo" in data:
        import aws_sdk_lightsail.types.disk_info_list

        out["from_disk_info"] = (
            aws_sdk_lightsail.types.disk_info_list.deserialize_aws_json_1_1(
                data["fromDiskInfo"]
            )
        )
    return out
