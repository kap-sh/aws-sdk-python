"""Generated from Smithy shape ``com.amazonaws.s3control#ListCallerAccessGrantsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.caller_access_grants_list
    import aws_sdk_s3_control.types.continuation_token


class ListCallerAccessGrantsResult(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_s3_control.types.continuation_token.ContinuationToken"
    ]
    """<p>A pagination token that you can use to request the next page of results. Pass this value into a subsequent <code>List Caller Access Grants</code> request in order to retrieve the next page of results.</p>"""
    caller_access_grants_list: NotRequired[
        "aws_sdk_s3_control.types.caller_access_grants_list.CallerAccessGrantsList"
    ]
    """<p>A list of the caller's access grants that were created using S3 Access Grants and that grant the caller access to the S3 data of the Amazon Web Services account ID that was specified in the request. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListCallerAccessGrantsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])
    if "caller_access_grants_list" in value:
        import aws_sdk_s3_control.types.caller_access_grants_list

        aws_sdk_s3_control.types.caller_access_grants_list.serialize_xml(
            value["caller_access_grants_list"], el, "CallerAccessGrantsList"
        )


def deserialize_xml(el: Element) -> ListCallerAccessGrantsResult:
    out: ListCallerAccessGrantsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_caller_access_grants_list = el.find("CallerAccessGrantsList")
    if child_caller_access_grants_list is not None:
        import aws_sdk_s3_control.types.caller_access_grants_list

        out["caller_access_grants_list"] = (
            aws_sdk_s3_control.types.caller_access_grants_list.deserialize_xml(
                child_caller_access_grants_list
            )
        )
    return out
