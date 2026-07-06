"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.disk_list
    import aws_sdk_lightsail.types.instance_snapshot_state
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.tag_list


class InstanceSnapshot(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the snapshot.</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the snapshot (<code>arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE</code>).</p>"""
    support_code: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the snapshot was created (<code>1479907467.024</code>).</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>The region name and Availability Zone where you created the snapshot.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The type of resource (usually <code>InstanceSnapshot</code>).</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    r"""<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags\">Amazon Lightsail Developer Guide</a>.</p>"""
    state: NotRequired[
        "aws_sdk_lightsail.types.instance_snapshot_state.InstanceSnapshotState"
    ]
    """<p>The state the snapshot is in.</p>"""
    progress: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The progress of the snapshot.</p> <note> <p>This is populated only for disk snapshots, and is <code>null</code> for instance snapshots.</p> </note>"""
    from_attached_disks: NotRequired["aws_sdk_lightsail.types.disk_list.DiskList"]
    """<p>An array of disk objects containing information about all block storage disks.</p>"""
    from_instance_name: NotRequired[
        "aws_sdk_lightsail.types.resource_name.ResourceName"
    ]
    """<p>The instance from which the snapshot was created.</p>"""
    from_instance_arn: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the instance from which the snapshot was created (<code>arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE</code>).</p>"""
    from_blueprint_id: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The blueprint ID from which you created the snapshot (<code>amazon_linux_2023</code>). A blueprint is a virtual private server (or <i>instance</i>) image used to create instances quickly.</p>"""
    from_bundle_id: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The bundle ID from which you created the snapshot (<code>micro_x_x</code>).</p>"""
    is_from_auto_snapshot: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the snapshot was created from an automatic snapshot.</p>"""
    size_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The size in GB of the SSD.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceSnapshot) -> dict:
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
    if "state" in value:
        import aws_sdk_lightsail.types.instance_snapshot_state

        out["state"] = (
            aws_sdk_lightsail.types.instance_snapshot_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "progress" in value:
        out["progress"] = value["progress"]
    if "from_attached_disks" in value:
        import aws_sdk_lightsail.types.disk_list

        out["fromAttachedDisks"] = (
            aws_sdk_lightsail.types.disk_list.serialize_aws_json_1_1(
                value["from_attached_disks"]
            )
        )
    if "from_instance_name" in value:
        out["fromInstanceName"] = value["from_instance_name"]
    if "from_instance_arn" in value:
        out["fromInstanceArn"] = value["from_instance_arn"]
    if "from_blueprint_id" in value:
        out["fromBlueprintId"] = value["from_blueprint_id"]
    if "from_bundle_id" in value:
        out["fromBundleId"] = value["from_bundle_id"]
    if "is_from_auto_snapshot" in value:
        out["isFromAutoSnapshot"] = value["is_from_auto_snapshot"]
    if "size_in_gb" in value:
        out["sizeInGb"] = value["size_in_gb"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceSnapshot:
    out: InstanceSnapshot = {}  # type: ignore[typeddict-item]
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
    if "state" in data:
        import aws_sdk_lightsail.types.instance_snapshot_state

        out["state"] = (
            aws_sdk_lightsail.types.instance_snapshot_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    if "progress" in data:
        out["progress"] = data["progress"]
    if "fromAttachedDisks" in data:
        import aws_sdk_lightsail.types.disk_list

        out["from_attached_disks"] = (
            aws_sdk_lightsail.types.disk_list.deserialize_aws_json_1_1(
                data["fromAttachedDisks"]
            )
        )
    if "fromInstanceName" in data:
        out["from_instance_name"] = data["fromInstanceName"]
    if "fromInstanceArn" in data:
        out["from_instance_arn"] = data["fromInstanceArn"]
    if "fromBlueprintId" in data:
        out["from_blueprint_id"] = data["fromBlueprintId"]
    if "fromBundleId" in data:
        out["from_bundle_id"] = data["fromBundleId"]
    if "isFromAutoSnapshot" in data:
        out["is_from_auto_snapshot"] = data["isFromAutoSnapshot"]
    if "sizeInGb" in data:
        out["size_in_gb"] = data["sizeInGb"]
    return out
