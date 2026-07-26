"""Generated from Smithy shape ``com.amazonaws.s3#WebsiteConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.error_document
    import capo_s3.types.index_document
    import capo_s3.types.redirect_all_requests_to
    import capo_s3.types.routing_rules


class WebsiteConfiguration(TypedDict, closed=True):
    error_document: NotRequired["capo_s3.types.error_document.ErrorDocument"]
    """<p>The name of the error document for the website.</p>"""
    index_document: NotRequired["capo_s3.types.index_document.IndexDocument"]
    """<p>The name of the index document for the website.</p>"""
    redirect_all_requests_to: NotRequired[
        "capo_s3.types.redirect_all_requests_to.RedirectAllRequestsTo"
    ]
    """<p>The redirect behavior for every request to this bucket's website endpoint.</p> <important> <p>If you specify this property, you can't specify any other property.</p> </important>"""
    routing_rules: NotRequired["capo_s3.types.routing_rules.RoutingRules"]
    """<p>Rules that define when a redirect is applied and the redirect behavior.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: WebsiteConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "error_document" in value:
        import capo_s3.types.error_document

        capo_s3.types.error_document.serialize_xml(
            value["error_document"], el, "ErrorDocument"
        )
    if "index_document" in value:
        import capo_s3.types.index_document

        capo_s3.types.index_document.serialize_xml(
            value["index_document"], el, "IndexDocument"
        )
    if "redirect_all_requests_to" in value:
        import capo_s3.types.redirect_all_requests_to

        capo_s3.types.redirect_all_requests_to.serialize_xml(
            value["redirect_all_requests_to"], el, "RedirectAllRequestsTo"
        )
    if "routing_rules" in value:
        import capo_s3.types.routing_rules

        capo_s3.types.routing_rules.serialize_xml(
            value["routing_rules"], el, "RoutingRules"
        )


def deserialize_xml(el: Element) -> WebsiteConfiguration:
    out: WebsiteConfiguration = {}  # type: ignore[typeddict-item]
    child_error_document = el.find("ErrorDocument")
    if child_error_document is not None:
        import capo_s3.types.error_document

        out["error_document"] = capo_s3.types.error_document.deserialize_xml(
            child_error_document
        )
    child_index_document = el.find("IndexDocument")
    if child_index_document is not None:
        import capo_s3.types.index_document

        out["index_document"] = capo_s3.types.index_document.deserialize_xml(
            child_index_document
        )
    child_redirect_all_requests_to = el.find("RedirectAllRequestsTo")
    if child_redirect_all_requests_to is not None:
        import capo_s3.types.redirect_all_requests_to

        out["redirect_all_requests_to"] = (
            capo_s3.types.redirect_all_requests_to.deserialize_xml(
                child_redirect_all_requests_to
            )
        )
    child_routing_rules = el.find("RoutingRules")
    if child_routing_rules is not None:
        import capo_s3.types.routing_rules

        out["routing_rules"] = capo_s3.types.routing_rules.deserialize_xml(
            child_routing_rules
        )
    return out
