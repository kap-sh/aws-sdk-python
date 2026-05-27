"""Generated from Smithy shape ``com.amazonaws.s3#ListBucketIntelligentTieringConfigurationsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.intelligent_tiering_configuration_list
    import aws_sdk_s3.types.is_truncated
    import aws_sdk_s3.types.next_token
    import aws_sdk_s3.types.token


class ListBucketIntelligentTieringConfigurationsOutput(TypedDict):
    is_truncated: NotRequired["aws_sdk_s3.types.is_truncated.IsTruncated"]
    """<p>Indicates whether the returned list of analytics configurations is complete. A value of <code>true</code> indicates that the list is not complete and the <code>NextContinuationToken</code> will be provided for a subsequent request.</p>"""
    continuation_token: NotRequired["aws_sdk_s3.types.token.Token"]
    """<p>The <code>ContinuationToken</code> that represents a placeholder from where this request should begin.</p>"""
    next_continuation_token: NotRequired["aws_sdk_s3.types.next_token.NextToken"]
    """<p>The marker used to continue this inventory configuration listing. Use the <code>NextContinuationToken</code> from this response to continue the listing in a subsequent request. The continuation token is an opaque value that Amazon S3 understands.</p>"""
    intelligent_tiering_configuration_list: NotRequired[
        "aws_sdk_s3.types.intelligent_tiering_configuration_list.IntelligentTieringConfigurationList"
    ]
    """<p>The list of S3 Intelligent-Tiering configurations for a bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListBucketIntelligentTieringConfigurationsOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "is_truncated" in value:
        SubElement(el, "IsTruncated").text = (
            "true" if value["is_truncated"] else "false"
        )
    if "continuation_token" in value:
        SubElement(el, "ContinuationToken").text = str(value["continuation_token"])
    if "next_continuation_token" in value:
        SubElement(el, "NextContinuationToken").text = str(
            value["next_continuation_token"]
        )
    if "intelligent_tiering_configuration_list" in value:
        import aws_sdk_s3.types.intelligent_tiering_configuration_list

        aws_sdk_s3.types.intelligent_tiering_configuration_list.serialize_xml_flat(
            value["intelligent_tiering_configuration_list"],
            el,
            "IntelligentTieringConfiguration",
        )


def deserialize_xml(el: Element) -> ListBucketIntelligentTieringConfigurationsOutput:
    out: ListBucketIntelligentTieringConfigurationsOutput = {}  # type: ignore[typeddict-item]
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    child_continuation_token = el.find("ContinuationToken")
    if child_continuation_token is not None:
        out["continuation_token"] = str(child_continuation_token.text or "")
    child_next_continuation_token = el.find("NextContinuationToken")
    if child_next_continuation_token is not None:
        out["next_continuation_token"] = str(child_next_continuation_token.text or "")
    if el.find("IntelligentTieringConfiguration") is not None:
        import aws_sdk_s3.types.intelligent_tiering_configuration_list

        out["intelligent_tiering_configuration_list"] = (
            aws_sdk_s3.types.intelligent_tiering_configuration_list.deserialize_xml_flat(
                el, "IntelligentTieringConfiguration"
            )
        )
    return out
