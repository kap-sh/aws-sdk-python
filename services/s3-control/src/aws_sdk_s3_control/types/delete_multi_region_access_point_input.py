"""Generated from Smithy shape ``com.amazonaws.s3control#DeleteMultiRegionAccessPointInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.multi_region_access_point_name


class DeleteMultiRegionAccessPointInput(TypedDict):
    name: "aws_sdk_s3_control.types.multi_region_access_point_name.MultiRegionAccessPointName"
    """<p>The name of the Multi-Region Access Point associated with this request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteMultiRegionAccessPointInput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])


def deserialize_xml(el: Element) -> DeleteMultiRegionAccessPointInput:
    out: DeleteMultiRegionAccessPointInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("DeleteMultiRegionAccessPointInput.name required")
    return out
