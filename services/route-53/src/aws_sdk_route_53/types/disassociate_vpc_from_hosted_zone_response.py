"""Generated from Smithy shape ``com.amazonaws.route53#DisassociateVPCFromHostedZoneResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.change_info


class DisassociateVPCFromHostedZoneResponse(TypedDict, closed=True):
    change_info: "aws_sdk_route_53.types.change_info.ChangeInfo"
    """<p>A complex type that describes the changes made to the specified private hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DisassociateVPCFromHostedZoneResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.change_info

    aws_sdk_route_53.types.change_info.serialize_xml(
        value["change_info"], el, "ChangeInfo"
    )


def deserialize_xml(el: Element) -> DisassociateVPCFromHostedZoneResponse:
    out: DisassociateVPCFromHostedZoneResponse = {}  # type: ignore[typeddict-item]
    child_change_info = el.find("ChangeInfo")
    if child_change_info is not None:
        import aws_sdk_route_53.types.change_info

        out["change_info"] = aws_sdk_route_53.types.change_info.deserialize_xml(
            child_change_info
        )
    else:
        raise DeserializationError(
            "DisassociateVPCFromHostedZoneResponse.change_info required"
        )
    return out
