"""Generated from Smithy shape ``com.amazonaws.s3#RedirectAllRequestsTo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.host_name
    import aws_sdk_s3.types.protocol


class RedirectAllRequestsTo(TypedDict, closed=True):
    host_name: "aws_sdk_s3.types.host_name.HostName"
    """<p>Name of the host where requests are redirected.</p>"""
    protocol: NotRequired["aws_sdk_s3.types.protocol.Protocol"]
    """<p>Protocol to use when redirecting requests. The default is the protocol that is used in the original request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RedirectAllRequestsTo, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HostName").text = str(value["host_name"])
    if "protocol" in value:
        import aws_sdk_s3.types.protocol

        aws_sdk_s3.types.protocol.serialize_xml(value["protocol"], el, "Protocol")


def deserialize_xml(el: Element) -> RedirectAllRequestsTo:
    out: RedirectAllRequestsTo = {}  # type: ignore[typeddict-item]
    child_host_name = el.find("HostName")
    if child_host_name is not None:
        out["host_name"] = str(child_host_name.text or "")
    else:
        raise DeserializationError("RedirectAllRequestsTo.host_name required")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import aws_sdk_s3.types.protocol

        out["protocol"] = aws_sdk_s3.types.protocol.deserialize_xml(child_protocol)
    return out
