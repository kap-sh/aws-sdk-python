"""Generated from Smithy shape ``com.amazonaws.route53#GetDNSSECResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.dnssec_status
    import aws_sdk_route_53.types.key_signing_keys


class GetDNSSECResponse(TypedDict, closed=True):
    status: "aws_sdk_route_53.types.dnssec_status.DNSSECStatus"
    """<p>A string representing the status of DNSSEC.</p>"""
    key_signing_keys: "aws_sdk_route_53.types.key_signing_keys.KeySigningKeys"
    """<p>The key-signing keys (KSKs) in your account.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetDNSSECResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.dnssec_status

    aws_sdk_route_53.types.dnssec_status.serialize_xml(value["status"], el, "Status")
    import aws_sdk_route_53.types.key_signing_keys

    aws_sdk_route_53.types.key_signing_keys.serialize_xml(
        value["key_signing_keys"], el, "KeySigningKeys"
    )


def deserialize_xml(el: Element) -> GetDNSSECResponse:
    out: GetDNSSECResponse = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_route_53.types.dnssec_status

        out["status"] = aws_sdk_route_53.types.dnssec_status.deserialize_xml(
            child_status
        )
    else:
        raise DeserializationError("GetDNSSECResponse.status required")
    child_key_signing_keys = el.find("KeySigningKeys")
    if child_key_signing_keys is not None:
        import aws_sdk_route_53.types.key_signing_keys

        out["key_signing_keys"] = (
            aws_sdk_route_53.types.key_signing_keys.deserialize_xml(
                child_key_signing_keys
            )
        )
    else:
        raise DeserializationError("GetDNSSECResponse.key_signing_keys required")
    return out
