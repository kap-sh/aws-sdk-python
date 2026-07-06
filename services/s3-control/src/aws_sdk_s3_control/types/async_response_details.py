"""Generated from Smithy shape ``com.amazonaws.s3control#AsyncResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.async_error_details
    import aws_sdk_s3_control.types.multi_region_access_points_async_response


class AsyncResponseDetails(TypedDict, closed=True):
    multi_region_access_point_details: NotRequired[
        "aws_sdk_s3_control.types.multi_region_access_points_async_response.MultiRegionAccessPointsAsyncResponse"
    ]
    """<p>The details for the Multi-Region Access Point.</p>"""
    error_details: NotRequired[
        "aws_sdk_s3_control.types.async_error_details.AsyncErrorDetails"
    ]
    """<p>Error details for an asynchronous request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AsyncResponseDetails, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "multi_region_access_point_details" in value:
        import aws_sdk_s3_control.types.multi_region_access_points_async_response

        aws_sdk_s3_control.types.multi_region_access_points_async_response.serialize_xml(
            value["multi_region_access_point_details"],
            el,
            "MultiRegionAccessPointDetails",
        )
    if "error_details" in value:
        import aws_sdk_s3_control.types.async_error_details

        aws_sdk_s3_control.types.async_error_details.serialize_xml(
            value["error_details"], el, "ErrorDetails"
        )


def deserialize_xml(el: Element) -> AsyncResponseDetails:
    out: AsyncResponseDetails = {}  # type: ignore[typeddict-item]
    child_multi_region_access_point_details = el.find("MultiRegionAccessPointDetails")
    if child_multi_region_access_point_details is not None:
        import aws_sdk_s3_control.types.multi_region_access_points_async_response

        out["multi_region_access_point_details"] = (
            aws_sdk_s3_control.types.multi_region_access_points_async_response.deserialize_xml(
                child_multi_region_access_point_details
            )
        )
    child_error_details = el.find("ErrorDetails")
    if child_error_details is not None:
        import aws_sdk_s3_control.types.async_error_details

        out["error_details"] = (
            aws_sdk_s3_control.types.async_error_details.deserialize_xml(
                child_error_details
            )
        )
    return out
