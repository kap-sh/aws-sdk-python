"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDiskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.add_on_request_list
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.tag_list


class CreateDiskRequest(TypedDict):
    disk_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The unique Lightsail disk name (<code>my-disk</code>).</p>"""
    availability_zone: "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The Availability Zone where you want to create the disk (<code>us-east-2a</code>). Use the same Availability Zone as the Lightsail instance to which you want to attach the disk.</p> <p>Use the <code>get regions</code> operation to list the Availability Zones where Lightsail is currently available.</p>"""
    size_in_gb: "aws_sdk_lightsail.types.integer.integer"
    """<p>The size of the disk in GB (<code>32</code>).</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""
    add_ons: NotRequired["aws_sdk_lightsail.types.add_on_request_list.AddOnRequestList"]
    """<p>An array of objects that represent the add-ons to enable for the new disk.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDiskRequest) -> dict:
    out: dict = {}
    out["diskName"] = value["disk_name"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDiskRequest:
    out: CreateDiskRequest = {}  # type: ignore[typeddict-item]
    if "diskName" in data:
        out["disk_name"] = data["diskName"]
    else:
        raise DeserializationError("CreateDiskRequest.disk_name required")
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    else:
        raise DeserializationError("CreateDiskRequest.availability_zone required")
    if "sizeInGb" in data:
        out["size_in_gb"] = data["sizeInGb"]
    else:
        raise DeserializationError("CreateDiskRequest.size_in_gb required")
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
    return out
