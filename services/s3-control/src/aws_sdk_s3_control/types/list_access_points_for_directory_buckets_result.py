"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessPointsForDirectoryBucketsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_point_list
    import aws_sdk_s3_control.types.non_empty_max_length1024_string


class ListAccessPointsForDirectoryBucketsResult(TypedDict, closed=True):
    access_point_list: NotRequired[
        "aws_sdk_s3_control.types.access_point_list.AccessPointList"
    ]
    """<p>Contains identification and configuration information for one or more access points associated with the directory bucket.</p>"""
    next_token: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p> If <code>NextToken</code> is returned, there are more access points available than requested in the <code>maxResults</code> value. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListAccessPointsForDirectoryBucketsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "access_point_list" in value:
        import aws_sdk_s3_control.types.access_point_list

        aws_sdk_s3_control.types.access_point_list.serialize_xml(
            value["access_point_list"], el, "AccessPointList"
        )
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])


def deserialize_xml(el: Element) -> ListAccessPointsForDirectoryBucketsResult:
    out: ListAccessPointsForDirectoryBucketsResult = {}  # type: ignore[typeddict-item]
    child_access_point_list = el.find("AccessPointList")
    if child_access_point_list is not None:
        import aws_sdk_s3_control.types.access_point_list

        out["access_point_list"] = (
            aws_sdk_s3_control.types.access_point_list.deserialize_xml(
                child_access_point_list
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
