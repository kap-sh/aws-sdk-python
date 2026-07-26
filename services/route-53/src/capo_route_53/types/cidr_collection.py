"""Generated from Smithy shape ``com.amazonaws.route53#CidrCollection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.arn
    import capo_route_53.types.collection_name
    import capo_route_53.types.collection_version
    import capo_route_53.types.uuid


class CidrCollection(TypedDict, closed=True):
    arn: NotRequired["capo_route_53.types.arn.ARN"]
    """<p>The ARN of the collection. Can be used to reference the collection in IAM policy or in another Amazon Web Services account.</p>"""
    id: NotRequired["capo_route_53.types.uuid.UUID"]
    """<p>The unique ID of the CIDR collection.</p>"""
    name: NotRequired["capo_route_53.types.collection_name.CollectionName"]
    """<p>The name of a CIDR collection.</p>"""
    version: NotRequired["capo_route_53.types.collection_version.CollectionVersion"]
    """<p>A sequential counter that Route 53 sets to 1 when you create a CIDR collection and increments by 1 each time you update settings for the CIDR collection.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CidrCollection, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "arn" in value:
        SubElement(el, "Arn").text = str(value["arn"])
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "version" in value:
        SubElement(el, "Version").text = str(value["version"])


def deserialize_xml(el: Element) -> CidrCollection:
    out: CidrCollection = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = int(child_version.text or "")
    return out
