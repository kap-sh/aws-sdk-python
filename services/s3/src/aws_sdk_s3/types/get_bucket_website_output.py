"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketWebsiteOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.error_document
    import aws_sdk_s3.types.index_document
    import aws_sdk_s3.types.redirect_all_requests_to
    import aws_sdk_s3.types.routing_rules


class GetBucketWebsiteOutput(TypedDict):
    redirect_all_requests_to: NotRequired[
        "aws_sdk_s3.types.redirect_all_requests_to.RedirectAllRequestsTo"
    ]
    """<p>Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket.</p>"""
    index_document: NotRequired["aws_sdk_s3.types.index_document.IndexDocument"]
    """<p>The name of the index document for the website (for example <code>index.html</code>).</p>"""
    error_document: NotRequired["aws_sdk_s3.types.error_document.ErrorDocument"]
    """<p>The object key name of the website error document to use for 4XX class errors.</p>"""
    routing_rules: NotRequired["aws_sdk_s3.types.routing_rules.RoutingRules"]
    """<p>Rules that define when a redirect is applied and the redirect behavior.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketWebsiteOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "redirect_all_requests_to" in value:
        import aws_sdk_s3.types.redirect_all_requests_to

        aws_sdk_s3.types.redirect_all_requests_to.serialize_xml(
            value["redirect_all_requests_to"], el, "RedirectAllRequestsTo"
        )
    if "index_document" in value:
        import aws_sdk_s3.types.index_document

        aws_sdk_s3.types.index_document.serialize_xml(
            value["index_document"], el, "IndexDocument"
        )
    if "error_document" in value:
        import aws_sdk_s3.types.error_document

        aws_sdk_s3.types.error_document.serialize_xml(
            value["error_document"], el, "ErrorDocument"
        )
    if "routing_rules" in value:
        import aws_sdk_s3.types.routing_rules

        aws_sdk_s3.types.routing_rules.serialize_xml(
            value["routing_rules"], el, "RoutingRules"
        )


def deserialize_xml(el: Element) -> GetBucketWebsiteOutput:
    out: GetBucketWebsiteOutput = {}  # type: ignore[typeddict-item]
    child_redirect_all_requests_to = el.find("RedirectAllRequestsTo")
    if child_redirect_all_requests_to is not None:
        import aws_sdk_s3.types.redirect_all_requests_to

        out["redirect_all_requests_to"] = (
            aws_sdk_s3.types.redirect_all_requests_to.deserialize_xml(
                child_redirect_all_requests_to
            )
        )
    child_index_document = el.find("IndexDocument")
    if child_index_document is not None:
        import aws_sdk_s3.types.index_document

        out["index_document"] = aws_sdk_s3.types.index_document.deserialize_xml(
            child_index_document
        )
    child_error_document = el.find("ErrorDocument")
    if child_error_document is not None:
        import aws_sdk_s3.types.error_document

        out["error_document"] = aws_sdk_s3.types.error_document.deserialize_xml(
            child_error_document
        )
    child_routing_rules = el.find("RoutingRules")
    if child_routing_rules is not None:
        import aws_sdk_s3.types.routing_rules

        out["routing_rules"] = aws_sdk_s3.types.routing_rules.deserialize_xml(
            child_routing_rules
        )
    return out
