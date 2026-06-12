"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessGrantsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.access_grants_list
    import aws_sdk_s3_control.types.continuation_token


class ListAccessGrantsResult(TypedDict):
    next_token: NotRequired[
        "aws_sdk_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p>A pagination token to request the next page of results. Pass this value into a subsequent <code>List Access Grants</code> request in order to retrieve the next page of results.</p>"""
    access_grants_list: NotRequired[
        "aws_sdk_s3_control.types.access_grants_list.AccessGrantsList"
    ]
    """<p>A container for a list of grants in an S3 Access Grants instance.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListAccessGrantsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])
    if "access_grants_list" in value:
        import aws_sdk_s3_control.types.access_grants_list

        aws_sdk_s3_control.types.access_grants_list.serialize_xml(
            value["access_grants_list"], el, "AccessGrantsList"
        )


def deserialize_xml(el: Element) -> ListAccessGrantsResult:
    out: ListAccessGrantsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_access_grants_list = el.find("AccessGrantsList")
    if child_access_grants_list is not None:
        import aws_sdk_s3_control.types.access_grants_list

        out["access_grants_list"] = (
            aws_sdk_s3_control.types.access_grants_list.deserialize_xml(
                child_access_grants_list
            )
        )
    return out
