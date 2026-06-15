"""Generated from Smithy shape ``com.amazonaws.lightsail#Instance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.add_on_list
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.instance_hardware
    import aws_sdk_lightsail.types.instance_metadata_options
    import aws_sdk_lightsail.types.instance_networking
    import aws_sdk_lightsail.types.instance_state
    import aws_sdk_lightsail.types.ip_address
    import aws_sdk_lightsail.types.ip_address_type
    import aws_sdk_lightsail.types.ipv6_address_list
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.resource_type
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.tag_list


class Instance(TypedDict):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name the user gave the instance (<code>Amazon_Linux_2023-1</code>).</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the instance (<code>arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE</code>).</p>"""
    support_code: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the instance was created (<code>1479734909.17</code>) in Unix time format.</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>The region name and Availability Zone where the instance is located.</p>"""
    resource_type: NotRequired["aws_sdk_lightsail.types.resource_type.ResourceType"]
    """<p>The type of resource (usually <code>Instance</code>).</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    r"""<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags\">Amazon Lightsail Developer Guide</a>.</p>"""
    blueprint_id: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The blueprint ID (<code>amazon_linux_2023</code>).</p>"""
    blueprint_name: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The friendly name of the blueprint (<code>Amazon Linux 2023</code>).</p>"""
    bundle_id: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The bundle for the instance (<code>micro_x_x</code>).</p>"""
    add_ons: NotRequired["aws_sdk_lightsail.types.add_on_list.AddOnList"]
    """<p>An array of objects representing the add-ons enabled on the instance.</p>"""
    is_static_ip: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether this instance has a static IP assigned to it.</p>"""
    private_ip_address: NotRequired["aws_sdk_lightsail.types.ip_address.IpAddress"]
    """<p>The private IP address of the instance.</p>"""
    public_ip_address: NotRequired["aws_sdk_lightsail.types.ip_address.IpAddress"]
    """<p>The public IP address of the instance.</p>"""
    ipv6_addresses: NotRequired[
        "aws_sdk_lightsail.types.ipv6_address_list.Ipv6AddressList"
    ]
    """<p>The IPv6 addresses of the instance.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_lightsail.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type of the instance.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p>"""
    hardware: NotRequired["aws_sdk_lightsail.types.instance_hardware.InstanceHardware"]
    """<p>The size of the vCPU and the amount of RAM for the instance.</p>"""
    networking: NotRequired[
        "aws_sdk_lightsail.types.instance_networking.InstanceNetworking"
    ]
    """<p>Information about the public ports and monthly data transfer rates for the instance.</p>"""
    state: NotRequired["aws_sdk_lightsail.types.instance_state.InstanceState"]
    """<p>The status code and the state (<code>running</code>) for the instance.</p>"""
    username: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The user name for connecting to the instance (<code>ec2-user</code>).</p>"""
    ssh_key_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the SSH key being used to connect to the instance (<code>LightsailDefaultKeyPair</code>).</p>"""
    metadata_options: NotRequired[
        "aws_sdk_lightsail.types.instance_metadata_options.InstanceMetadataOptions"
    ]
    """<p>The metadata options for the Amazon Lightsail instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Instance) -> dict:
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
    if "blueprint_id" in value:
        out["blueprintId"] = value["blueprint_id"]
    if "blueprint_name" in value:
        out["blueprintName"] = value["blueprint_name"]
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    if "add_ons" in value:
        import aws_sdk_lightsail.types.add_on_list

        out["addOns"] = aws_sdk_lightsail.types.add_on_list.serialize_aws_json_1_1(
            value["add_ons"]
        )
    if "is_static_ip" in value:
        out["isStaticIp"] = value["is_static_ip"]
    if "private_ip_address" in value:
        out["privateIpAddress"] = value["private_ip_address"]
    if "public_ip_address" in value:
        out["publicIpAddress"] = value["public_ip_address"]
    if "ipv6_addresses" in value:
        import aws_sdk_lightsail.types.ipv6_address_list

        out["ipv6Addresses"] = (
            aws_sdk_lightsail.types.ipv6_address_list.serialize_aws_json_1_1(
                value["ipv6_addresses"]
            )
        )
    if "ip_address_type" in value:
        import aws_sdk_lightsail.types.ip_address_type

        out["ipAddressType"] = (
            aws_sdk_lightsail.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "hardware" in value:
        import aws_sdk_lightsail.types.instance_hardware

        out["hardware"] = (
            aws_sdk_lightsail.types.instance_hardware.serialize_aws_json_1_1(
                value["hardware"]
            )
        )
    if "networking" in value:
        import aws_sdk_lightsail.types.instance_networking

        out["networking"] = (
            aws_sdk_lightsail.types.instance_networking.serialize_aws_json_1_1(
                value["networking"]
            )
        )
    if "state" in value:
        import aws_sdk_lightsail.types.instance_state

        out["state"] = aws_sdk_lightsail.types.instance_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "username" in value:
        out["username"] = value["username"]
    if "ssh_key_name" in value:
        out["sshKeyName"] = value["ssh_key_name"]
    if "metadata_options" in value:
        import aws_sdk_lightsail.types.instance_metadata_options

        out["metadataOptions"] = (
            aws_sdk_lightsail.types.instance_metadata_options.serialize_aws_json_1_1(
                value["metadata_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
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
    if "blueprintId" in data:
        out["blueprint_id"] = data["blueprintId"]
    if "blueprintName" in data:
        out["blueprint_name"] = data["blueprintName"]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    if "addOns" in data:
        import aws_sdk_lightsail.types.add_on_list

        out["add_ons"] = aws_sdk_lightsail.types.add_on_list.deserialize_aws_json_1_1(
            data["addOns"]
        )
    if "isStaticIp" in data:
        out["is_static_ip"] = data["isStaticIp"]
    if "privateIpAddress" in data:
        out["private_ip_address"] = data["privateIpAddress"]
    if "publicIpAddress" in data:
        out["public_ip_address"] = data["publicIpAddress"]
    if "ipv6Addresses" in data:
        import aws_sdk_lightsail.types.ipv6_address_list

        out["ipv6_addresses"] = (
            aws_sdk_lightsail.types.ipv6_address_list.deserialize_aws_json_1_1(
                data["ipv6Addresses"]
            )
        )
    if "ipAddressType" in data:
        import aws_sdk_lightsail.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_lightsail.types.ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    if "hardware" in data:
        import aws_sdk_lightsail.types.instance_hardware

        out["hardware"] = (
            aws_sdk_lightsail.types.instance_hardware.deserialize_aws_json_1_1(
                data["hardware"]
            )
        )
    if "networking" in data:
        import aws_sdk_lightsail.types.instance_networking

        out["networking"] = (
            aws_sdk_lightsail.types.instance_networking.deserialize_aws_json_1_1(
                data["networking"]
            )
        )
    if "state" in data:
        import aws_sdk_lightsail.types.instance_state

        out["state"] = aws_sdk_lightsail.types.instance_state.deserialize_aws_json_1_1(
            data["state"]
        )
    if "username" in data:
        out["username"] = data["username"]
    if "sshKeyName" in data:
        out["ssh_key_name"] = data["sshKeyName"]
    if "metadataOptions" in data:
        import aws_sdk_lightsail.types.instance_metadata_options

        out["metadata_options"] = (
            aws_sdk_lightsail.types.instance_metadata_options.deserialize_aws_json_1_1(
                data["metadataOptions"]
            )
        )
    return out
