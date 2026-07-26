"""Generated from Smithy shape ``com.amazonaws.route53#DeactivateKeySigningKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.change_info


class DeactivateKeySigningKeyResponse(TypedDict, closed=True):
    change_info: "capo_route_53.types.change_info.ChangeInfo"


# --- restXml ser/de ---
def serialize_xml(
    value: DeactivateKeySigningKeyResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.change_info

    capo_route_53.types.change_info.serialize_xml(
        value["change_info"], el, "ChangeInfo"
    )


def deserialize_xml(el: Element) -> DeactivateKeySigningKeyResponse:
    out: DeactivateKeySigningKeyResponse = {}  # type: ignore[typeddict-item]
    child_change_info = el.find("ChangeInfo")
    if child_change_info is not None:
        import capo_route_53.types.change_info

        out["change_info"] = capo_route_53.types.change_info.deserialize_xml(
            child_change_info
        )
    else:
        raise DeserializationError(
            "DeactivateKeySigningKeyResponse.change_info required"
        )
    return out
