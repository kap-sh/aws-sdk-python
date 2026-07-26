"""Generated from Smithy shape ``com.amazonaws.route53#CreateKeySigningKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.change_info
    import capo_route_53.types.key_signing_key
    import capo_route_53.types.resource_uri


class CreateKeySigningKeyResponse(TypedDict, closed=True):
    change_info: "capo_route_53.types.change_info.ChangeInfo"
    key_signing_key: "capo_route_53.types.key_signing_key.KeySigningKey"
    """<p>The key-signing key (KSK) that the request creates.</p>"""
    location: "capo_route_53.types.resource_uri.ResourceURI"
    """<p>The unique URL representing the new key-signing key (KSK).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateKeySigningKeyResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.change_info

    capo_route_53.types.change_info.serialize_xml(
        value["change_info"], el, "ChangeInfo"
    )
    import capo_route_53.types.key_signing_key

    capo_route_53.types.key_signing_key.serialize_xml(
        value["key_signing_key"], el, "KeySigningKey"
    )


def deserialize_xml(el: Element) -> CreateKeySigningKeyResponse:
    out: CreateKeySigningKeyResponse = {}  # type: ignore[typeddict-item]
    child_change_info = el.find("ChangeInfo")
    if child_change_info is not None:
        import capo_route_53.types.change_info

        out["change_info"] = capo_route_53.types.change_info.deserialize_xml(
            child_change_info
        )
    else:
        raise DeserializationError("CreateKeySigningKeyResponse.change_info required")
    child_key_signing_key = el.find("KeySigningKey")
    if child_key_signing_key is not None:
        import capo_route_53.types.key_signing_key

        out["key_signing_key"] = capo_route_53.types.key_signing_key.deserialize_xml(
            child_key_signing_key
        )
    else:
        raise DeserializationError(
            "CreateKeySigningKeyResponse.key_signing_key required"
        )
    return out
