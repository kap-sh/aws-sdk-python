"""Generated from Smithy shape ``com.amazonaws.s3#LocationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.location_name_as_string
    import aws_sdk_s3.types.location_type


class LocationInfo(TypedDict, closed=True):
    type: NotRequired["aws_sdk_s3.types.location_type.LocationType"]
    """<p>The type of location where the bucket will be created.</p>"""
    name: NotRequired["aws_sdk_s3.types.location_name_as_string.LocationNameAsString"]
    """<p>The name of the location where the bucket will be created.</p> <p>For directory buckets, the name of the location is the Zone ID of the Availability Zone (AZ) or Local Zone (LZ) where the bucket will be created. An example AZ ID value is <code>usw2-az1</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: LocationInfo, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "type" in value:
        import aws_sdk_s3.types.location_type

        aws_sdk_s3.types.location_type.serialize_xml(value["type"], el, "Type")
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])


def deserialize_xml(el: Element) -> LocationInfo:
    out: LocationInfo = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_s3.types.location_type

        out["type"] = aws_sdk_s3.types.location_type.deserialize_xml(child_type)
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
