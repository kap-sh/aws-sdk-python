"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneFailureReasons``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.failure_reason


class HostedZoneFailureReasons(TypedDict, closed=True):
    accelerated_recovery: NotRequired[
        "capo_route_53.types.failure_reason.FailureReason"
    ]
    """<p>The reason why accelerated recovery failed to be enabled or disabled for the hosted zone, if applicable.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HostedZoneFailureReasons, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "accelerated_recovery" in value:
        SubElement(el, "AcceleratedRecovery").text = str(value["accelerated_recovery"])


def deserialize_xml(el: Element) -> HostedZoneFailureReasons:
    out: HostedZoneFailureReasons = {}  # type: ignore[typeddict-item]
    child_accelerated_recovery = el.find("AcceleratedRecovery")
    if child_accelerated_recovery is not None:
        out["accelerated_recovery"] = str(child_accelerated_recovery.text or "")
    return out
