"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetConnectionGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.connection_group
    import aws_sdk_cloudfront.types.string


class GetConnectionGroupResult(TypedDict, closed=True):
    connection_group: NotRequired[
        "aws_sdk_cloudfront.types.connection_group.ConnectionGroup"
    ]
    """<p>The connection group that you retrieved.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the connection group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetConnectionGroupResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "connection_group" in value:
        import aws_sdk_cloudfront.types.connection_group

        aws_sdk_cloudfront.types.connection_group.serialize_xml(
            value["connection_group"], el, "ConnectionGroup"
        )


def deserialize_xml(el: Element) -> GetConnectionGroupResult:
    out: GetConnectionGroupResult = {}  # type: ignore[typeddict-item]
    child_connection_group = el.find("ConnectionGroup")
    if child_connection_group is not None:
        import aws_sdk_cloudfront.types.connection_group

        out["connection_group"] = (
            aws_sdk_cloudfront.types.connection_group.deserialize_xml(
                child_connection_group
            )
        )
    return out
