"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.disk_snapshot_state
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.tag_list


class DiskSnapshot(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the disk snapshot (<code>my-disk-snapshot</code>).</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the disk snapshot.</p>"""
    support_code: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The date when the disk snapshot was created.</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>The AWS Region and Availability Zone where the disk snapshot was created.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type (<code>DiskSnapshot</code>).</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    r"""<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags\">Amazon Lightsail Developer Guide</a>.</p>"""
    size_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The size of the disk in GB.</p>"""
    state: NotRequired["aws_sdk_lightsail.types.disk_snapshot_state.DiskSnapshotState"]
    """<p>The status of the disk snapshot operation.</p>"""
    progress: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The progress of the snapshot.</p>"""
    from_disk_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The unique name of the source disk from which the disk snapshot was created.</p>"""
    from_disk_arn: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the source disk from which the disk snapshot was created.</p>"""
    from_instance_name: NotRequired[
        "aws_sdk_lightsail.types.resource_name.ResourceName"
    ]
    """<p>The unique name of the source instance from which the disk (system volume) snapshot was created.</p>"""
    from_instance_arn: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the source instance from which the disk (system volume) snapshot was created.</p>"""
    is_from_auto_snapshot: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the snapshot was created from an automatic snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskSnapshot) -> dict:
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
    if "size_in_gb" in value:
        out["sizeInGb"] = value["size_in_gb"]
    if "state" in value:
        import aws_sdk_lightsail.types.disk_snapshot_state

        out["state"] = (
            aws_sdk_lightsail.types.disk_snapshot_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "progress" in value:
        out["progress"] = value["progress"]
    if "from_disk_name" in value:
        out["fromDiskName"] = value["from_disk_name"]
    if "from_disk_arn" in value:
        out["fromDiskArn"] = value["from_disk_arn"]
    if "from_instance_name" in value:
        out["fromInstanceName"] = value["from_instance_name"]
    if "from_instance_arn" in value:
        out["fromInstanceArn"] = value["from_instance_arn"]
    if "is_from_auto_snapshot" in value:
        out["isFromAutoSnapshot"] = value["is_from_auto_snapshot"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiskSnapshot:
    out: DiskSnapshot = {}  # type: ignore[typeddict-item]
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
    if "sizeInGb" in data:
        out["size_in_gb"] = data["sizeInGb"]
    if "state" in data:
        import aws_sdk_lightsail.types.disk_snapshot_state

        out["state"] = (
            aws_sdk_lightsail.types.disk_snapshot_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    if "progress" in data:
        out["progress"] = data["progress"]
    if "fromDiskName" in data:
        out["from_disk_name"] = data["fromDiskName"]
    if "fromDiskArn" in data:
        out["from_disk_arn"] = data["fromDiskArn"]
    if "fromInstanceName" in data:
        out["from_instance_name"] = data["fromInstanceName"]
    if "fromInstanceArn" in data:
        out["from_instance_arn"] = data["fromInstanceArn"]
    if "isFromAutoSnapshot" in data:
        out["is_from_auto_snapshot"] = data["isFromAutoSnapshot"]
    return out
