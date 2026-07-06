"""Generated from Smithy shape ``com.amazonaws.route53#DeleteKeySigningKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_id
    import aws_sdk_route_53.types.signing_key_name


class DeleteKeySigningKeyRequest(TypedDict, closed=True):
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>A unique string used to identify a hosted zone.</p>"""
    name: "aws_sdk_route_53.types.signing_key_name.SigningKeyName"
    """<p>A string used to identify a key-signing key (KSK).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteKeySigningKeyRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteKeySigningKeyRequest:
    out: DeleteKeySigningKeyRequest = {}  # type: ignore[typeddict-item]
    return out
