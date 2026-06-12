"""Generated from Smithy shape ``com.amazonaws.s3control#SubmitMultiRegionAccessPointRoutesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.multi_region_access_point_id
    import aws_sdk_s3_control.types.route_list


class SubmitMultiRegionAccessPointRoutesRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>"""
    mrap: (
        "aws_sdk_s3_control.types.multi_region_access_point_id.MultiRegionAccessPointId"
    )
    """<p>The Multi-Region Access Point ARN.</p>"""
    route_updates: "aws_sdk_s3_control.types.route_list.RouteList"
    """<p>The different routes that make up the new route configuration. Active routes return a value of <code>100</code>, and passive routes return a value of <code>0</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: SubmitMultiRegionAccessPointRoutesRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.route_list

    aws_sdk_s3_control.types.route_list.serialize_xml(
        value["route_updates"], el, "RouteUpdates"
    )


def deserialize_xml(el: Element) -> SubmitMultiRegionAccessPointRoutesRequest:
    out: SubmitMultiRegionAccessPointRoutesRequest = {}  # type: ignore[typeddict-item]
    child_route_updates = el.find("RouteUpdates")
    if child_route_updates is not None:
        import aws_sdk_s3_control.types.route_list

        out["route_updates"] = aws_sdk_s3_control.types.route_list.deserialize_xml(
            child_route_updates
        )
    else:
        raise DeserializationError(
            "SubmitMultiRegionAccessPointRoutesRequest.route_updates required"
        )
    return out
