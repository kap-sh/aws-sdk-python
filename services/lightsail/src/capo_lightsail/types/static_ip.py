"""Generated from Smithy shape ``com.amazonaws.lightsail#StaticIp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.ip_address
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string


class StaticIp(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the static IP (<code>StaticIP-Ohio-EXAMPLE</code>).</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the static IP (<code>arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE</code>).</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the static IP was created (<code>1479735304.222</code>).</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>The region and Availability Zone where the static IP was created.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The resource type (usually <code>StaticIp</code>).</p>"""
    ip_address: NotRequired["capo_lightsail.types.ip_address.IpAddress"]
    """<p>The static IP address.</p>"""
    attached_to: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The instance where the static IP is attached (<code>Amazon_Linux-1GB-Ohio-1</code>).</p>"""
    is_attached: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the static IP is attached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StaticIp) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "attached_to" in value:
        out["attachedTo"] = value["attached_to"]
    if "is_attached" in value:
        out["isAttached"] = value["is_attached"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StaticIp:
    out: StaticIp = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "supportCode" in data:
        out["support_code"] = data["supportCode"]
    if "createdAt" in data:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "location" in data:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "resourceType" in data:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "attachedTo" in data:
        out["attached_to"] = data["attachedTo"]
    if "isAttached" in data:
        out["is_attached"] = data["isAttached"]
    return out
