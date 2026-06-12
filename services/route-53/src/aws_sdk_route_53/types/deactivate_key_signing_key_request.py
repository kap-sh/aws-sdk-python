"""Generated from Smithy shape ``com.amazonaws.route53#DeactivateKeySigningKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_id
    import aws_sdk_route_53.types.signing_key_name


class DeactivateKeySigningKeyRequest(TypedDict):
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>A unique string used to identify a hosted zone.</p>"""
    name: "aws_sdk_route_53.types.signing_key_name.SigningKeyName"
    """<p>A string used to identify a key-signing key (KSK).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeactivateKeySigningKeyRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeactivateKeySigningKeyRequest:
    out: DeactivateKeySigningKeyRequest = {}  # type: ignore[typeddict-item]
    return out
