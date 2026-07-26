"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateConnectionGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.connection_group
    import capo_cloudfront.types.string


class UpdateConnectionGroupResult(TypedDict, closed=True):
    connection_group: NotRequired[
        "capo_cloudfront.types.connection_group.ConnectionGroup"
    ]
    """<p>The connection group that you updated.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the connection group.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateConnectionGroupResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "connection_group" in value:
        import capo_cloudfront.types.connection_group

        capo_cloudfront.types.connection_group.serialize_xml(
            value["connection_group"], el, "ConnectionGroup"
        )


def deserialize_xml(el: Element) -> UpdateConnectionGroupResult:
    out: UpdateConnectionGroupResult = {}  # type: ignore[typeddict-item]
    child_connection_group = el.find("ConnectionGroup")
    if child_connection_group is not None:
        import capo_cloudfront.types.connection_group

        out["connection_group"] = (
            capo_cloudfront.types.connection_group.deserialize_xml(
                child_connection_group
            )
        )
    return out
