"""Generated from Smithy shape ``com.amazonaws.lightsail#Origin``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.integer
    import capo_lightsail.types.origin_ip_address_type_enum
    import capo_lightsail.types.origin_protocol_policy_enum
    import capo_lightsail.types.region_name
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type


class Origin(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the origin resource.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The resource type of the origin resource (<i>Instance</i>).</p>"""
    region_name: NotRequired["capo_lightsail.types.region_name.RegionName"]
    """<p>The AWS Region name of the origin resource.</p>"""
    protocol_policy: NotRequired[
        "capo_lightsail.types.origin_protocol_policy_enum.OriginProtocolPolicyEnum"
    ]
    """<p>The protocol that your Amazon Lightsail distribution uses when establishing a connection with your origin to pull content.</p>"""
    response_timeout: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The amount of time, in seconds, that the distribution waits for a response after forwarding a request to the origin. The minimum timeout is 1 second, the maximum is 60 seconds, and the default (if you don't specify otherwise) is 30 seconds.</p>"""
    ip_address_type: NotRequired[
        "capo_lightsail.types.origin_ip_address_type_enum.OriginIpAddressTypeEnum"
    ]
    """<p>The IP address type that the distribution uses when connecting to the origin.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Origin) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "region_name" in value:
        import capo_lightsail.types.region_name

        out["regionName"] = capo_lightsail.types.region_name.serialize_aws_json_1_1(
            value["region_name"]
        )
    if "protocol_policy" in value:
        import capo_lightsail.types.origin_protocol_policy_enum

        out["protocolPolicy"] = (
            capo_lightsail.types.origin_protocol_policy_enum.serialize_aws_json_1_1(
                value["protocol_policy"]
            )
        )
    if "response_timeout" in value:
        out["responseTimeout"] = value["response_timeout"]
    if "ip_address_type" in value:
        import capo_lightsail.types.origin_ip_address_type_enum

        out["ipAddressType"] = (
            capo_lightsail.types.origin_ip_address_type_enum.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Origin:
    out: Origin = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "resourceType" in data:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "regionName" in data:
        import capo_lightsail.types.region_name

        out["region_name"] = capo_lightsail.types.region_name.deserialize_aws_json_1_1(
            data["regionName"]
        )
    if "protocolPolicy" in data:
        import capo_lightsail.types.origin_protocol_policy_enum

        out["protocol_policy"] = (
            capo_lightsail.types.origin_protocol_policy_enum.deserialize_aws_json_1_1(
                data["protocolPolicy"]
            )
        )
    if "responseTimeout" in data:
        out["response_timeout"] = data["responseTimeout"]
    if "ipAddressType" in data:
        import capo_lightsail.types.origin_ip_address_type_enum

        out["ip_address_type"] = (
            capo_lightsail.types.origin_ip_address_type_enum.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    return out
