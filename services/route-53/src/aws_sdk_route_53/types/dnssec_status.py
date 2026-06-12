"""Generated from Smithy shape ``com.amazonaws.route53#DNSSECStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.serve_signature
    import aws_sdk_route_53.types.signing_key_status_message


class DNSSECStatus(TypedDict):
    serve_signature: NotRequired[
        "aws_sdk_route_53.types.serve_signature.ServeSignature"
    ]
    """<p>A string that represents the current hosted zone signing status.</p> <p>Status can have one of the following values:</p> <dl> <dt>SIGNING</dt> <dd> <p>DNSSEC signing is enabled for the hosted zone.</p> </dd> <dt>NOT_SIGNING</dt> <dd> <p>DNSSEC signing is not enabled for the hosted zone.</p> </dd> <dt>DELETING</dt> <dd> <p>DNSSEC signing is in the process of being removed for the hosted zone.</p> </dd> <dt>ACTION_NEEDED</dt> <dd> <p>There is a problem with signing in the hosted zone that requires you to take action to resolve. For example, the customer managed key might have been deleted, or the permissions for the customer managed key might have been changed.</p> </dd> <dt>INTERNAL_FAILURE</dt> <dd> <p>There was an error during a request. Before you can continue to work with DNSSEC signing, including with key-signing keys (KSKs), you must correct the problem by enabling or disabling DNSSEC signing for the hosted zone.</p> </dd> </dl>"""
    status_message: NotRequired[
        "aws_sdk_route_53.types.signing_key_status_message.SigningKeyStatusMessage"
    ]
    """<p>The status message provided for the following DNSSEC signing status: <code>INTERNAL_FAILURE</code>. The status message includes information about what the problem might be and steps that you can take to correct the issue.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DNSSECStatus, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "serve_signature" in value:
        SubElement(el, "ServeSignature").text = str(value["serve_signature"])
    if "status_message" in value:
        SubElement(el, "StatusMessage").text = str(value["status_message"])


def deserialize_xml(el: Element) -> DNSSECStatus:
    out: DNSSECStatus = {}  # type: ignore[typeddict-item]
    child_serve_signature = el.find("ServeSignature")
    if child_serve_signature is not None:
        out["serve_signature"] = str(child_serve_signature.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    return out
