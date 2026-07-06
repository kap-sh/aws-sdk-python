"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateInstancesFromSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.add_on_request_list
    import aws_sdk_lightsail.types.attached_disk_map
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.ip_address_type
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.string_list
    import aws_sdk_lightsail.types.tag_list


class CreateInstancesFromSnapshotRequest(TypedDict, closed=True):
    instance_names: "aws_sdk_lightsail.types.string_list.StringList"
    """<p>The names for your new instances.</p>"""
    attached_disk_mapping: NotRequired[
        "aws_sdk_lightsail.types.attached_disk_map.AttachedDiskMap"
    ]
    """<p>An object containing information about one or more disk mappings.</p>"""
    availability_zone: "aws_sdk_lightsail.types.string.string"
    r"""<p>The Availability Zone where you want to create your instances. Use the following formatting: <code>us-east-2a</code> (case sensitive). You can get a list of Availability Zones by using the <a href=\"http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html\">get regions</a> operation. Be sure to add the <code>include Availability Zones</code> parameter to your request.</p>"""
    instance_snapshot_name: NotRequired[
        "aws_sdk_lightsail.types.resource_name.ResourceName"
    ]
    """<p>The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation to return information about your existing snapshots.</p> <p>Constraint:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>source instance name</code> parameter. The <code>instance snapshot name</code> and <code>source instance name</code> parameters are mutually exclusive.</p> </li> </ul>"""
    bundle_id: "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The bundle of specification information for your virtual private server (or <i>instance</i>), including the pricing plan (<code>micro_x_x</code>).</p>"""
    user_data: NotRequired["aws_sdk_lightsail.types.string.string"]
    r"""<p>You can create a launch script that configures a server with additional user data. For example, <code>apt-get -y update</code>.</p> <note> <p>Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use <code>yum</code>, Debian and Ubuntu use <code>apt-get</code>, and FreeBSD uses <code>pkg</code>. For a complete list, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/compare-options-choose-lightsail-instance-image\">Amazon Lightsail Developer Guide</a>.</p> </note>"""
    key_pair_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name for your key pair.</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""
    add_ons: NotRequired["aws_sdk_lightsail.types.add_on_request_list.AddOnRequestList"]
    """<p>An array of objects representing the add-ons to enable for the new instance.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_lightsail.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type for the instance.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p> <p>The default value is <code>dualstack</code>.</p>"""
    source_instance_name: NotRequired["aws_sdk_lightsail.types.string.string"]
    r"""<p>The name of the source instance from which the source automatic snapshot was created.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>instance snapshot name</code> parameter. The <code>source instance name</code> and <code>instance snapshot name</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots\">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""
    restore_date: NotRequired["aws_sdk_lightsail.types.string.string"]
    r"""<p>The date of the automatic snapshot to use for the new instance. Use the <code>get auto snapshots</code> operation to identify the dates of the available automatic snapshots.</p> <p>Constraints:</p> <ul> <li> <p>Must be specified in <code>YYYY-MM-DD</code> format.</p> </li> <li> <p>This parameter cannot be defined together with the <code>use latest restorable auto snapshot</code> parameter. The <code>restore date</code> and <code>use latest restorable auto snapshot</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots\">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""
    use_latest_restorable_auto_snapshot: NotRequired[
        "aws_sdk_lightsail.types.boolean.boolean"
    ]
    r"""<p>A Boolean value to indicate whether to use the latest available automatic snapshot.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>restore date</code> parameter. The <code>use latest restorable auto snapshot</code> and <code>restore date</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots\">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInstancesFromSnapshotRequest) -> dict:
    out: dict = {}
    import aws_sdk_lightsail.types.string_list

    out["instanceNames"] = aws_sdk_lightsail.types.string_list.serialize_aws_json_1_1(
        value["instance_names"]
    )
    if "attached_disk_mapping" in value:
        import aws_sdk_lightsail.types.attached_disk_map

        out["attachedDiskMapping"] = (
            aws_sdk_lightsail.types.attached_disk_map.serialize_aws_json_1_1(
                value["attached_disk_mapping"]
            )
        )
    out["availabilityZone"] = value["availability_zone"]
    if "instance_snapshot_name" in value:
        out["instanceSnapshotName"] = value["instance_snapshot_name"]
    out["bundleId"] = value["bundle_id"]
    if "user_data" in value:
        out["userData"] = value["user_data"]
    if "key_pair_name" in value:
        out["keyPairName"] = value["key_pair_name"]
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
    if "ip_address_type" in value:
        import aws_sdk_lightsail.types.ip_address_type

        out["ipAddressType"] = (
            aws_sdk_lightsail.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "source_instance_name" in value:
        out["sourceInstanceName"] = value["source_instance_name"]
    if "restore_date" in value:
        out["restoreDate"] = value["restore_date"]
    if "use_latest_restorable_auto_snapshot" in value:
        out["useLatestRestorableAutoSnapshot"] = value[
            "use_latest_restorable_auto_snapshot"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInstancesFromSnapshotRequest:
    out: CreateInstancesFromSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "instanceNames" in data:
        import aws_sdk_lightsail.types.string_list

        out["instance_names"] = (
            aws_sdk_lightsail.types.string_list.deserialize_aws_json_1_1(
                data["instanceNames"]
            )
        )
    else:
        raise DeserializationError(
            "CreateInstancesFromSnapshotRequest.instance_names required"
        )
    if "attachedDiskMapping" in data:
        import aws_sdk_lightsail.types.attached_disk_map

        out["attached_disk_mapping"] = (
            aws_sdk_lightsail.types.attached_disk_map.deserialize_aws_json_1_1(
                data["attachedDiskMapping"]
            )
        )
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    else:
        raise DeserializationError(
            "CreateInstancesFromSnapshotRequest.availability_zone required"
        )
    if "instanceSnapshotName" in data:
        out["instance_snapshot_name"] = data["instanceSnapshotName"]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError(
            "CreateInstancesFromSnapshotRequest.bundle_id required"
        )
    if "userData" in data:
        out["user_data"] = data["userData"]
    if "keyPairName" in data:
        out["key_pair_name"] = data["keyPairName"]
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
    if "ipAddressType" in data:
        import aws_sdk_lightsail.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_lightsail.types.ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    if "sourceInstanceName" in data:
        out["source_instance_name"] = data["sourceInstanceName"]
    if "restoreDate" in data:
        out["restore_date"] = data["restoreDate"]
    if "useLatestRestorableAutoSnapshot" in data:
        out["use_latest_restorable_auto_snapshot"] = data[
            "useLatestRestorableAutoSnapshot"
        ]
    return out
