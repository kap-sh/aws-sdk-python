"""Generated from Smithy shape ``com.amazonaws.s3control#MultiRegionAccessPointsAsyncResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.multi_region_access_point_regional_response_list


class MultiRegionAccessPointsAsyncResponse(TypedDict):
    regions: NotRequired[
        "aws_sdk_s3_control.types.multi_region_access_point_regional_response_list.MultiRegionAccessPointRegionalResponseList"
    ]
    """<p>A collection of status information for the different Regions that a Multi-Region Access Point supports.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: MultiRegionAccessPointsAsyncResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "regions" in value:
        import aws_sdk_s3_control.types.multi_region_access_point_regional_response_list

        aws_sdk_s3_control.types.multi_region_access_point_regional_response_list.serialize_xml(
            value["regions"], el, "Regions"
        )


def deserialize_xml(el: Element) -> MultiRegionAccessPointsAsyncResponse:
    out: MultiRegionAccessPointsAsyncResponse = {}  # type: ignore[typeddict-item]
    child_regions = el.find("Regions")
    if child_regions is not None:
        import aws_sdk_s3_control.types.multi_region_access_point_regional_response_list

        out["regions"] = (
            aws_sdk_s3_control.types.multi_region_access_point_regional_response_list.deserialize_xml(
                child_regions
            )
        )
    return out
