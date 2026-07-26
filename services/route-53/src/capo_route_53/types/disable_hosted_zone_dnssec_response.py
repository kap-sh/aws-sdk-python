"""Generated from Smithy shape ``com.amazonaws.route53#DisableHostedZoneDNSSECResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.change_info


class DisableHostedZoneDNSSECResponse(TypedDict, closed=True):
    change_info: "capo_route_53.types.change_info.ChangeInfo"


# --- restXml ser/de ---
def serialize_xml(
    value: DisableHostedZoneDNSSECResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.change_info

    capo_route_53.types.change_info.serialize_xml(
        value["change_info"], el, "ChangeInfo"
    )


def deserialize_xml(el: Element) -> DisableHostedZoneDNSSECResponse:
    out: DisableHostedZoneDNSSECResponse = {}  # type: ignore[typeddict-item]
    child_change_info = el.find("ChangeInfo")
    if child_change_info is not None:
        import capo_route_53.types.change_info

        out["change_info"] = capo_route_53.types.change_info.deserialize_xml(
            child_change_info
        )
    else:
        raise DeserializationError(
            "DisableHostedZoneDNSSECResponse.change_info required"
        )
    return out
