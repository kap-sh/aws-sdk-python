"""Generated from Smithy shape ``com.amazonaws.lightsail#Disk``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.add_on_list
    import aws_sdk_lightsail.types.auto_mount_status
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.disk_state
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.tag_list


class Disk(TypedDict):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The unique name of the disk.</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the disk.</p>"""
    support_code: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The date when the disk was created.</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>The AWS Region and Availability Zone where the disk is located.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type (<code>Disk</code>).</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags\">Amazon Lightsail Developer Guide</a>.</p>"""
    add_ons: NotRequired["aws_sdk_lightsail.types.add_on_list.AddOnList"]
    """<p>An array of objects representing the add-ons enabled on the disk.</p>"""
    size_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The size of the disk in GB.</p>"""
    is_system_disk: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).</p>"""
    iops: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The input/output operations per second (IOPS) of the disk.</p>"""
    path: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The disk path.</p>"""
    state: NotRequired["aws_sdk_lightsail.types.disk_state.DiskState"]
    """<p>Describes the status of the disk.</p>"""
    attached_to: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The resources to which the disk is attached.</p>"""
    is_attached: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the disk is attached.</p>"""
    attachment_state: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>(Discontinued) The attachment state of the disk.</p> <note> <p>In releases prior to November 14, 2017, this parameter returned <code>attached</code> for system disks in the API response. It is now discontinued, but still included in the response. Use <code>isAttached</code> instead.</p> </note>"""
    gb_in_use: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>(Discontinued) The number of GB in use by the disk.</p> <note> <p>In releases prior to November 14, 2017, this parameter was not included in the API response. It is now discontinued.</p> </note>"""
    auto_mount_status: NotRequired[
        "aws_sdk_lightsail.types.auto_mount_status.AutoMountStatus"
    ]
    """<p>The status of automatically mounting a storage disk to a virtual computer.</p> <important> <p>This parameter only applies to Lightsail for Research resources.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Disk) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_lightsail.types.resource_type

        out["resourceType"] = (
            aws_sdk_lightsail.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "add_ons" in value:
        import aws_sdk_lightsail.types.add_on_list

        out["addOns"] = aws_sdk_lightsail.types.add_on_list.serialize_aws_json_1_1(
            value["add_ons"]
        )
    if "size_in_gb" in value:
        out["sizeInGb"] = value["size_in_gb"]
    if "is_system_disk" in value:
        out["isSystemDisk"] = value["is_system_disk"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "path" in value:
        out["path"] = value["path"]
    if "state" in value:
        import aws_sdk_lightsail.types.disk_state

        out["state"] = aws_sdk_lightsail.types.disk_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "attached_to" in value:
        out["attachedTo"] = value["attached_to"]
    if "is_attached" in value:
        out["isAttached"] = value["is_attached"]
    if "attachment_state" in value:
        out["attachmentState"] = value["attachment_state"]
    if "gb_in_use" in value:
        out["gbInUse"] = value["gb_in_use"]
    if "auto_mount_status" in value:
        import aws_sdk_lightsail.types.auto_mount_status

        out["autoMountStatus"] = (
            aws_sdk_lightsail.types.auto_mount_status.serialize_aws_json_1_1(
                value["auto_mount_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Disk:
    out: Disk = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "supportCode" in data:
        out["support_code"] = data["supportCode"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "location" in data:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_lightsail.types.resource_type

        out["resource_type"] = (
            aws_sdk_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "addOns" in data:
        import aws_sdk_lightsail.types.add_on_list

        out["add_ons"] = aws_sdk_lightsail.types.add_on_list.deserialize_aws_json_1_1(
            data["addOns"]
        )
    if "sizeInGb" in data:
        out["size_in_gb"] = data["sizeInGb"]
    if "isSystemDisk" in data:
        out["is_system_disk"] = data["isSystemDisk"]
    if "iops" in data:
        out["iops"] = data["iops"]
    if "path" in data:
        out["path"] = data["path"]
    if "state" in data:
        import aws_sdk_lightsail.types.disk_state

        out["state"] = aws_sdk_lightsail.types.disk_state.deserialize_aws_json_1_1(
            data["state"]
        )
    if "attachedTo" in data:
        out["attached_to"] = data["attachedTo"]
    if "isAttached" in data:
        out["is_attached"] = data["isAttached"]
    if "attachmentState" in data:
        out["attachment_state"] = data["attachmentState"]
    if "gbInUse" in data:
        out["gb_in_use"] = data["gbInUse"]
    if "autoMountStatus" in data:
        import aws_sdk_lightsail.types.auto_mount_status

        out["auto_mount_status"] = (
            aws_sdk_lightsail.types.auto_mount_status.deserialize_aws_json_1_1(
                data["autoMountStatus"]
            )
        )
    return out
