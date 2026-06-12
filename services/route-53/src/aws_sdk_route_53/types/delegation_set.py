"""Generated from Smithy shape ``com.amazonaws.route53#DelegationSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.delegation_set_name_servers
    import aws_sdk_route_53.types.nonce
    import aws_sdk_route_53.types.resource_id


class DelegationSet(TypedDict):
    id: NotRequired["aws_sdk_route_53.types.resource_id.ResourceId"]
    """<p>The ID that Amazon Route 53 assigns to a reusable delegation set.</p>"""
    caller_reference: NotRequired["aws_sdk_route_53.types.nonce.Nonce"]
    """<p>The value that you specified for <code>CallerReference</code> when you created the reusable delegation set.</p>"""
    name_servers: (
        "aws_sdk_route_53.types.delegation_set_name_servers.DelegationSetNameServers"
    )
    """<p>A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DelegationSet, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])
    if "caller_reference" in value:
        SubElement(el, "CallerReference").text = str(value["caller_reference"])
    import aws_sdk_route_53.types.delegation_set_name_servers

    aws_sdk_route_53.types.delegation_set_name_servers.serialize_xml(
        value["name_servers"], el, "NameServers"
    )


def deserialize_xml(el: Element) -> DelegationSet:
    out: DelegationSet = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    child_name_servers = el.find("NameServers")
    if child_name_servers is not None:
        import aws_sdk_route_53.types.delegation_set_name_servers

        out["name_servers"] = (
            aws_sdk_route_53.types.delegation_set_name_servers.deserialize_xml(
                child_name_servers
            )
        )
    else:
        raise DeserializationError("DelegationSet.name_servers required")
    return out
