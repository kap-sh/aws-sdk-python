"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListConflictingAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.alias_string
    import capo_cloudfront.types.distribution_id_string
    import capo_cloudfront.types.list_conflicting_aliases_max_items_integer
    import capo_cloudfront.types.string


class ListConflictingAliasesRequest(TypedDict, closed=True):
    distribution_id: "capo_cloudfront.types.distribution_id_string.distributionIdString"
    """<p>The ID of a standard distribution in your account that has an attached TLS certificate that includes the provided alias.</p>"""
    alias: "capo_cloudfront.types.alias_string.aliasString"
    """<p>The alias (also called a CNAME) to search for conflicting aliases.</p>"""
    marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>Use this field when paginating results to indicate where to begin in the list of conflicting aliases. The response includes conflicting aliases in the list that occur after the marker. To get the next page of the list, set this field's value to the value of <code>NextMarker</code> from the current page's response.</p>"""
    max_items: NotRequired[
        "capo_cloudfront.types.list_conflicting_aliases_max_items_integer.listConflictingAliasesMaxItemsInteger"
    ]
    """<p>The maximum number of conflicting aliases that you want in the response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListConflictingAliasesRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListConflictingAliasesRequest:
    out: ListConflictingAliasesRequest = {}  # type: ignore[typeddict-item]
    return out
