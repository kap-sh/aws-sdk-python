"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConnectionGroupSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.timestamp


class ConnectionGroupSummary(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the connection group.</p>"""
    name: "aws_sdk_cloudfront.types.string.string"
    """<p>The name of the connection group.</p>"""
    arn: "aws_sdk_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the connection group.</p>"""
    routing_endpoint: "aws_sdk_cloudfront.types.string.string"
    """<p>The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.</p>"""
    created_time: "aws_sdk_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the connection group was created.</p>"""
    last_modified_time: "aws_sdk_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the connection group was updated.</p>"""
    e_tag: "aws_sdk_cloudfront.types.string.string"
    """<p>The current version of the connection group.</p>"""
    anycast_ip_list_id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The ID of the Anycast static IP list.</p>"""
    enabled: NotRequired["aws_sdk_cloudfront.types.boolean.boolean"]
    """<p>Whether the connection group is enabled</p>"""
    status: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The status of the connection group.</p>"""
    is_default: NotRequired["aws_sdk_cloudfront.types.boolean.boolean"]
    """<p>Whether the connection group is the default connection group for the distribution tenants.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ConnectionGroupSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Arn").text = str(value["arn"])
    SubElement(el, "RoutingEndpoint").text = str(value["routing_endpoint"])
    import aws_sdk_cloudfront.types.timestamp

    aws_sdk_cloudfront.types.timestamp.serialize_xml(
        value["created_time"], el, "CreatedTime"
    )
    import aws_sdk_cloudfront.types.timestamp

    aws_sdk_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    SubElement(el, "ETag").text = str(value["e_tag"])
    if "anycast_ip_list_id" in value:
        SubElement(el, "AnycastIpListId").text = str(value["anycast_ip_list_id"])
    if "enabled" in value:
        SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    if "status" in value:
        SubElement(el, "Status").text = str(value["status"])
    if "is_default" in value:
        SubElement(el, "IsDefault").text = "true" if value["is_default"] else "false"


def deserialize_xml(el: Element) -> ConnectionGroupSummary:
    out: ConnectionGroupSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("ConnectionGroupSummary.id required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("ConnectionGroupSummary.name required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("ConnectionGroupSummary.arn required")
    child_routing_endpoint = el.find("RoutingEndpoint")
    if child_routing_endpoint is not None:
        out["routing_endpoint"] = str(child_routing_endpoint.text or "")
    else:
        raise DeserializationError("ConnectionGroupSummary.routing_endpoint required")
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import aws_sdk_cloudfront.types.timestamp

        out["created_time"] = aws_sdk_cloudfront.types.timestamp.deserialize_xml(
            child_created_time
        )
    else:
        raise DeserializationError("ConnectionGroupSummary.created_time required")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import aws_sdk_cloudfront.types.timestamp

        out["last_modified_time"] = aws_sdk_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError("ConnectionGroupSummary.last_modified_time required")
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    else:
        raise DeserializationError("ConnectionGroupSummary.e_tag required")
    child_anycast_ip_list_id = el.find("AnycastIpListId")
    if child_anycast_ip_list_id is not None:
        out["anycast_ip_list_id"] = str(child_anycast_ip_list_id.text or "")
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    return out
