"""Generated from Smithy shape ``com.amazonaws.s3#ListBucketAnalyticsConfigurationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.analytics_configuration_list
    import aws_sdk_s3.types.is_truncated
    import aws_sdk_s3.types.next_token
    import aws_sdk_s3.types.token


class ListBucketAnalyticsConfigurationsOutput(TypedDict):
    is_truncated: NotRequired["aws_sdk_s3.types.is_truncated.IsTruncated"]
    """<p>Indicates whether the returned list of analytics configurations is complete. A value of true indicates that the list is not complete and the NextContinuationToken will be provided for a subsequent request.</p>"""
    continuation_token: NotRequired["aws_sdk_s3.types.token.Token"]
    """<p>The marker that is used as a starting point for this analytics configuration list response. This value is present if it was sent in the request.</p>"""
    next_continuation_token: NotRequired["aws_sdk_s3.types.next_token.NextToken"]
    """<p> <code>NextContinuationToken</code> is sent when <code>isTruncated</code> is true, which indicates that there are more analytics configurations to list. The next request must include this <code>NextContinuationToken</code>. The token is obfuscated and is not a usable value.</p>"""
    analytics_configuration_list: NotRequired[
        "aws_sdk_s3.types.analytics_configuration_list.AnalyticsConfigurationList"
    ]
    """<p>The list of analytics configurations for a bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListBucketAnalyticsConfigurationsOutput, parent: Element, tag: str
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
    if "analytics_configuration_list" in value:
        import aws_sdk_s3.types.analytics_configuration_list

        aws_sdk_s3.types.analytics_configuration_list.serialize_xml_flat(
            value["analytics_configuration_list"], el, "AnalyticsConfiguration"
        )


def deserialize_xml(el: Element) -> ListBucketAnalyticsConfigurationsOutput:
    out: ListBucketAnalyticsConfigurationsOutput = {}  # type: ignore[typeddict-item]
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    child_continuation_token = el.find("ContinuationToken")
    if child_continuation_token is not None:
        out["continuation_token"] = str(child_continuation_token.text or "")
    child_next_continuation_token = el.find("NextContinuationToken")
    if child_next_continuation_token is not None:
        out["next_continuation_token"] = str(child_next_continuation_token.text or "")
    if el.find("AnalyticsConfiguration") is not None:
        import aws_sdk_s3.types.analytics_configuration_list

        out["analytics_configuration_list"] = (
            aws_sdk_s3.types.analytics_configuration_list.deserialize_xml_flat(
                el, "AnalyticsConfiguration"
            )
        )
    return out
