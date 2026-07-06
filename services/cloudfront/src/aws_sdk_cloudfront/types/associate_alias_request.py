"""Generated from Smithy shape ``com.amazonaws.cloudfront#AssociateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string


class AssociateAliasRequest(TypedDict, closed=True):
    target_distribution_id: "aws_sdk_cloudfront.types.string.string"
    """<p>The ID of the standard distribution that you're associating the alias with.</p>"""
    alias: "aws_sdk_cloudfront.types.string.string"
    """<p>The alias (also known as a CNAME) to add to the target standard distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AssociateAliasRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> AssociateAliasRequest:
    out: AssociateAliasRequest = {}  # type: ignore[typeddict-item]
    return out
