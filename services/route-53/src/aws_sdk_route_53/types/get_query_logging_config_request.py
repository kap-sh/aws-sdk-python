"""Generated from Smithy shape ``com.amazonaws.route53#GetQueryLoggingConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.query_logging_config_id


class GetQueryLoggingConfigRequest(TypedDict):
    id: "aws_sdk_route_53.types.query_logging_config_id.QueryLoggingConfigId"
    """<p>The ID of the configuration for DNS query logging that you want to get information about.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetQueryLoggingConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetQueryLoggingConfigRequest:
    out: GetQueryLoggingConfigRequest = {}  # type: ignore[typeddict-item]
    return out
