"""Generated from Smithy shape ``com.amazonaws.s3control#ListMultiRegionAccessPointsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.multi_region_access_point_report_list
    import capo_s3_control.types.non_empty_max_length1024_string


class ListMultiRegionAccessPointsResult(TypedDict, closed=True):
    access_points: NotRequired[
        "capo_s3_control.types.multi_region_access_point_report_list.MultiRegionAccessPointReportList"
    ]
    """<p>The list of Multi-Region Access Points associated with the user.</p>"""
    next_token: NotRequired[
        "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p>If the specified bucket has more Multi-Region Access Points than can be returned in one call to this action, this field contains a continuation token. You can use this token tin subsequent calls to this action to retrieve additional Multi-Region Access Points.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListMultiRegionAccessPointsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "access_points" in value:
        import capo_s3_control.types.multi_region_access_point_report_list

        capo_s3_control.types.multi_region_access_point_report_list.serialize_xml(
            value["access_points"], el, "AccessPoints"
        )
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])


def deserialize_xml(el: Element) -> ListMultiRegionAccessPointsResult:
    out: ListMultiRegionAccessPointsResult = {}  # type: ignore[typeddict-item]
    child_access_points = el.find("AccessPoints")
    if child_access_points is not None:
        import capo_s3_control.types.multi_region_access_point_report_list

        out["access_points"] = (
            capo_s3_control.types.multi_region_access_point_report_list.deserialize_xml(
                child_access_points
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
