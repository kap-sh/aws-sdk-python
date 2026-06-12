"""Generated from Smithy shape ``com.amazonaws.route53#DeleteQueryLoggingConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.query_logging_config_id


class DeleteQueryLoggingConfigRequest(TypedDict):
    id: "aws_sdk_route_53.types.query_logging_config_id.QueryLoggingConfigId"
    """<p>The ID of the configuration that you want to delete. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteQueryLoggingConfigRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteQueryLoggingConfigRequest:
    out: DeleteQueryLoggingConfigRequest = {}  # type: ignore[typeddict-item]
    return out
