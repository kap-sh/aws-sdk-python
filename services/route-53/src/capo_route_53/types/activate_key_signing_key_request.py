"""Generated from Smithy shape ``com.amazonaws.route53#ActivateKeySigningKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_id
    import capo_route_53.types.signing_key_name


class ActivateKeySigningKeyRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>A unique string used to identify a hosted zone.</p>"""
    name: "capo_route_53.types.signing_key_name.SigningKeyName"
    """<p>A string used to identify a key-signing key (KSK). <code>Name</code> can include numbers, letters, and underscores (_). <code>Name</code> must be unique for each key-signing key in the same hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ActivateKeySigningKeyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ActivateKeySigningKeyRequest:
    out: ActivateKeySigningKeyRequest = {}  # type: ignore[typeddict-item]
    return out
