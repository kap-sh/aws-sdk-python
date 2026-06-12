"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessPointsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_point_list
    import aws_sdk_s3_control.types.non_empty_max_length1024_string


class ListAccessPointsResult(TypedDict):
    access_point_list: NotRequired[
        "aws_sdk_s3_control.types.access_point_list.AccessPointList"
    ]
    """<p>Contains identification and configuration information for one or more access points associated with the specified bucket.</p>"""
    next_token: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p>If the specified bucket has more access points than can be returned in one call to this API, this field contains a continuation token that you can provide in subsequent calls to this API to retrieve additional access points.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListAccessPointsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "access_point_list" in value:
        import aws_sdk_s3_control.types.access_point_list

        aws_sdk_s3_control.types.access_point_list.serialize_xml(
            value["access_point_list"], el, "AccessPointList"
        )
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])


def deserialize_xml(el: Element) -> ListAccessPointsResult:
    out: ListAccessPointsResult = {}  # type: ignore[typeddict-item]
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
