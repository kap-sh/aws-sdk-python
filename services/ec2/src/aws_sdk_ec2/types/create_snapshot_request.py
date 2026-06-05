"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.snapshot_location_enum
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.volume_id


class CreateSnapshotRequest(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the snapshot.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<note> <p>Only supported for volumes on Outposts. If the source volume is not on an Outpost, omit this parameter.</p> </note> <ul> <li> <p>To create the snapshot on the same Outpost as the source volume, specify the ARN of that Outpost. The snapshot must be created on the same Outpost as the volume.</p> </li> <li> <p>To create the snapshot in the parent Region of the Outpost, omit this parameter.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#create-snapshot\">Create local snapshots from volumes on an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the Amazon EBS volume.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the snapshot during creation.</p>"""
    location: NotRequired[
        "aws_sdk_ec2.types.snapshot_location_enum.SnapshotLocationEnum"
    ]
    """<note> <p>Only supported for volumes in Local Zones. If the source volume is not in a Local Zone, omit this parameter.</p> </note> <ul> <li> <p>To create a local snapshot in the same Local Zone as the source volume, specify <code>local</code>.</p> </li> <li> <p>To create a regional snapshot in the parent Region of the Local Zone, specify <code>regional</code> or omit this parameter.</p> </li> </ul> <p>Default value: <code>regional</code> </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSnapshotRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "outpost_arn" in value:
        pairs.append((f"{prefix}.OutpostArn", str(value["outpost_arn"])))
    if "volume_id" in value:
        pairs.append((f"{prefix}.VolumeId", str(value["volume_id"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "location" in value:
        import aws_sdk_ec2.types.snapshot_location_enum

        aws_sdk_ec2.types.snapshot_location_enum.serialize_ec2_query(
            value["location"], pairs, f"{prefix}.Location"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateSnapshotRequest:
    out: CreateSnapshotRequest = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_location = el.find("Location")
    if child_location is not None:
        import aws_sdk_ec2.types.snapshot_location_enum

        out["location"] = (
            aws_sdk_ec2.types.snapshot_location_enum.deserialize_ec2_query(
                child_location
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
