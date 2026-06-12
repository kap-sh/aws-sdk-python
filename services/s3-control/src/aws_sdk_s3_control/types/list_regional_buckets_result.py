"""Generated from Smithy shape ``com.amazonaws.s3control#ListRegionalBucketsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.non_empty_max_length1024_string
    import aws_sdk_s3_control.types.regional_bucket_list


class ListRegionalBucketsResult(TypedDict):
    regional_bucket_list: NotRequired[
        "aws_sdk_s3_control.types.regional_bucket_list.RegionalBucketList"
    ]
    """<p></p>"""
    next_token: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    ]
    """<p> <code>NextToken</code> is sent when <code>isTruncated</code> is true, which means there are more buckets that can be listed. The next list requests to Amazon S3 can be continued with this <code>NextToken</code>. <code>NextToken</code> is obfuscated and is not a real key.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListRegionalBucketsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "regional_bucket_list" in value:
        import aws_sdk_s3_control.types.regional_bucket_list

        aws_sdk_s3_control.types.regional_bucket_list.serialize_xml(
            value["regional_bucket_list"], el, "RegionalBucketList"
        )
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])


def deserialize_xml(el: Element) -> ListRegionalBucketsResult:
    out: ListRegionalBucketsResult = {}  # type: ignore[typeddict-item]
    child_regional_bucket_list = el.find("RegionalBucketList")
    if child_regional_bucket_list is not None:
        import aws_sdk_s3_control.types.regional_bucket_list

        out["regional_bucket_list"] = (
            aws_sdk_s3_control.types.regional_bucket_list.deserialize_xml(
                child_regional_bucket_list
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
