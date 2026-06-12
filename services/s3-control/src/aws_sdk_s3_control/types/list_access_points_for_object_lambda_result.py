"""Generated from Smithy shape ``com.amazonaws.s3control#ListAccessPointsForObjectLambdaResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.non_empty_max_length1024_string
    import aws_sdk_s3_control.types.object_lambda_access_point_list


class ListAccessPointsForObjectLambdaResult(TypedDict):
    object_lambda_access_point_list: NotRequired[
        "aws_sdk_s3_control.types.object_lambda_access_point_list.ObjectLambdaAccessPointList"
    ]
    """<p>Returns list of Object Lambda Access Points.</p>"""
    next_token: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p>If the list has more access points than can be returned in one call to this API, this field contains a continuation token that you can provide in subsequent calls to this API to retrieve additional access points.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListAccessPointsForObjectLambdaResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "object_lambda_access_point_list" in value:
        import aws_sdk_s3_control.types.object_lambda_access_point_list

        aws_sdk_s3_control.types.object_lambda_access_point_list.serialize_xml(
            value["object_lambda_access_point_list"], el, "ObjectLambdaAccessPointList"
        )
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])


def deserialize_xml(el: Element) -> ListAccessPointsForObjectLambdaResult:
    out: ListAccessPointsForObjectLambdaResult = {}  # type: ignore[typeddict-item]
    child_object_lambda_access_point_list = el.find("ObjectLambdaAccessPointList")
    if child_object_lambda_access_point_list is not None:
        import aws_sdk_s3_control.types.object_lambda_access_point_list

        out["object_lambda_access_point_list"] = (
            aws_sdk_s3_control.types.object_lambda_access_point_list.deserialize_xml(
                child_object_lambda_access_point_list
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
