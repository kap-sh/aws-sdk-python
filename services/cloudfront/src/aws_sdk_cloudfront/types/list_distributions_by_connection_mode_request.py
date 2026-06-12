"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListDistributionsByConnectionModeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.connection_mode
    import aws_sdk_cloudfront.types.integer
    import aws_sdk_cloudfront.types.string


class ListDistributionsByConnectionModeRequest(TypedDict):
    marker: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p> The marker for the next set of distributions to retrieve.</p>"""
    max_items: NotRequired["aws_sdk_cloudfront.types.integer.integer"]
    """<p>The maximum number of distributions to return.</p>"""
    connection_mode: "aws_sdk_cloudfront.types.connection_mode.ConnectionMode"
    """<p>This field specifies whether the connection mode is through a standard distribution (direct) or a multi-tenant distribution with distribution tenants (tenant-only).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDistributionsByConnectionModeRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListDistributionsByConnectionModeRequest:
    out: ListDistributionsByConnectionModeRequest = {}  # type: ignore[typeddict-item]
    return out
