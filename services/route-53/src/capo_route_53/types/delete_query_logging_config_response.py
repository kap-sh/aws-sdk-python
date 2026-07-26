"""Generated from Smithy shape ``com.amazonaws.route53#DeleteQueryLoggingConfigResponse``."""

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement


class DeleteQueryLoggingConfigResponse(TypedDict, closed=True):
    pass


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteQueryLoggingConfigResponse, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteQueryLoggingConfigResponse:
    out: DeleteQueryLoggingConfigResponse = {}  # type: ignore[typeddict-item]
    return out
