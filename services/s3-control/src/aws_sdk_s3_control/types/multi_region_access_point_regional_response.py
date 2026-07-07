"""Generated from Smithy shape ``com.amazonaws.s3control#MultiRegionAccessPointRegionalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.async_request_status
    import aws_sdk_s3_control.types.region_name


class MultiRegionAccessPointRegionalResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_s3_control.types.region_name.RegionName"]
    """<p>The name of the Region in the Multi-Region Access Point.</p>"""
    request_status: NotRequired[
        "aws_sdk_s3_control.types.async_request_status.AsyncRequestStatus"
    ]
    """<p>The current status of the Multi-Region Access Point in this Region.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: MultiRegionAccessPointRegionalResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "request_status" in value:
        SubElement(el, "RequestStatus").text = str(value["request_status"])


def deserialize_xml(el: Element) -> MultiRegionAccessPointRegionalResponse:
    out: MultiRegionAccessPointRegionalResponse = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_request_status = el.find("RequestStatus")
    if child_request_status is not None:
        out["request_status"] = str(child_request_status.text or "")
    return out
