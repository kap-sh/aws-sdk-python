"""Generated from Smithy shape ``com.amazonaws.route53#EnableHostedZoneDNSSECResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.change_info


class EnableHostedZoneDNSSECResponse(TypedDict, closed=True):
    change_info: "aws_sdk_route_53.types.change_info.ChangeInfo"


# --- restXml ser/de ---
def serialize_xml(
    value: EnableHostedZoneDNSSECResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.change_info

    aws_sdk_route_53.types.change_info.serialize_xml(
        value["change_info"], el, "ChangeInfo"
    )


def deserialize_xml(el: Element) -> EnableHostedZoneDNSSECResponse:
    out: EnableHostedZoneDNSSECResponse = {}  # type: ignore[typeddict-item]
    child_change_info = el.find("ChangeInfo")
    if child_change_info is not None:
        import aws_sdk_route_53.types.change_info

        out["change_info"] = aws_sdk_route_53.types.change_info.deserialize_xml(
            child_change_info
        )
    else:
        raise DeserializationError(
            "EnableHostedZoneDNSSECResponse.change_info required"
        )
    return out
