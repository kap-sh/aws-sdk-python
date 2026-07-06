"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDomainConflictsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.domain_conflicts_list
    import aws_sdk_cloudfront.types.string


class ListDomainConflictsResult(TypedDict, closed=True):
    domain_conflicts: NotRequired[
        "aws_sdk_cloudfront.types.domain_conflicts_list.DomainConflictsList"
    ]
    """<p>Contains details about the domain conflicts.</p>"""
    next_marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListDomainConflictsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "domain_conflicts" in value:
        import aws_sdk_cloudfront.types.domain_conflicts_list

        aws_sdk_cloudfront.types.domain_conflicts_list.serialize_xml(
            value["domain_conflicts"], el, "DomainConflicts"
        )
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])


def deserialize_xml(el: Element) -> ListDomainConflictsResult:
    out: ListDomainConflictsResult = {}  # type: ignore[typeddict-item]
    child_domain_conflicts = el.find("DomainConflicts")
    if child_domain_conflicts is not None:
        import aws_sdk_cloudfront.types.domain_conflicts_list

        out["domain_conflicts"] = (
            aws_sdk_cloudfront.types.domain_conflicts_list.deserialize_xml(
                child_domain_conflicts
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
