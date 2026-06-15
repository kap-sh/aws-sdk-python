"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDiskFromSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.add_on_request_list
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.tag_list


class CreateDiskFromSnapshotRequest(TypedDict):
    disk_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The unique Lightsail disk name (<code>my-disk</code>).</p>"""
    disk_snapshot_name: NotRequired[
        "aws_sdk_lightsail.types.resource_name.ResourceName"
    ]
    """<p>The name of the disk snapshot (<code>my-snapshot</code>) from which to create the new storage disk.</p> <p>Constraint:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>source disk name</code> parameter. The <code>disk snapshot name</code> and <code>source disk name</code> parameters are mutually exclusive.</p> </li> </ul>"""
    availability_zone: "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The Availability Zone where you want to create the disk (<code>us-east-2a</code>). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.</p> <p>Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.</p>"""
    size_in_gb: "aws_sdk_lightsail.types.integer.integer"
    """<p>The size of the disk in GB (<code>32</code>).</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""
    add_ons: NotRequired["aws_sdk_lightsail.types.add_on_request_list.AddOnRequestList"]
    """<p>An array of objects that represent the add-ons to enable for the new disk.</p>"""
    source_disk_name: NotRequired["aws_sdk_lightsail.types.string.string"]
    r"""<p>The name of the source disk from which the source automatic snapshot was created.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>disk snapshot name</code> parameter. The <code>source disk name</code> and <code>disk snapshot name</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots\">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""
    restore_date: NotRequired["aws_sdk_lightsail.types.string.string"]
    r"""<p>The date of the automatic snapshot to use for the new disk. Use the <code>get auto snapshots</code> operation to identify the dates of the available automatic snapshots.</p> <p>Constraints:</p> <ul> <li> <p>Must be specified in <code>YYYY-MM-DD</code> format.</p> </li> <li> <p>This parameter cannot be defined together with the <code>use latest restorable auto snapshot</code> parameter. The <code>restore date</code> and <code>use latest restorable auto snapshot</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots\">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""
    use_latest_restorable_auto_snapshot: NotRequired[
        "aws_sdk_lightsail.types.boolean.boolean"
    ]
    r"""<p>A Boolean value to indicate whether to use the latest available automatic snapshot.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>restore date</code> parameter. The <code>use latest restorable auto snapshot</code> and <code>restore date</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots\">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDiskFromSnapshotRequest) -> dict:
    out: dict = {}
    out["diskName"] = value["disk_name"]
    if "disk_snapshot_name" in value:
        out["diskSnapshotName"] = value["disk_snapshot_name"]
    out["availabilityZone"] = value["availability_zone"]
    out["sizeInGb"] = value["size_in_gb"]
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "add_ons" in value:
        import aws_sdk_lightsail.types.add_on_request_list

        out["addOns"] = (
            aws_sdk_lightsail.types.add_on_request_list.serialize_aws_json_1_1(
                value["add_ons"]
            )
        )
    if "source_disk_name" in value:
        out["sourceDiskName"] = value["source_disk_name"]
    if "restore_date" in value:
        out["restoreDate"] = value["restore_date"]
    if "use_latest_restorable_auto_snapshot" in value:
        out["useLatestRestorableAutoSnapshot"] = value[
            "use_latest_restorable_auto_snapshot"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDiskFromSnapshotRequest:
    out: CreateDiskFromSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "diskName" in data:
        out["disk_name"] = data["diskName"]
    else:
        raise DeserializationError("CreateDiskFromSnapshotRequest.disk_name required")
    if "diskSnapshotName" in data:
        out["disk_snapshot_name"] = data["diskSnapshotName"]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    else:
        raise DeserializationError(
            "CreateDiskFromSnapshotRequest.availability_zone required"
        )
    if "sizeInGb" in data:
        out["size_in_gb"] = data["sizeInGb"]
    else:
        raise DeserializationError("CreateDiskFromSnapshotRequest.size_in_gb required")
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "addOns" in data:
        import aws_sdk_lightsail.types.add_on_request_list

        out["add_ons"] = (
            aws_sdk_lightsail.types.add_on_request_list.deserialize_aws_json_1_1(
                data["addOns"]
            )
        )
    if "sourceDiskName" in data:
        out["source_disk_name"] = data["sourceDiskName"]
    if "restoreDate" in data:
        out["restore_date"] = data["restoreDate"]
    if "useLatestRestorableAutoSnapshot" in data:
        out["use_latest_restorable_auto_snapshot"] = data[
            "useLatestRestorableAutoSnapshot"
        ]
    return out
