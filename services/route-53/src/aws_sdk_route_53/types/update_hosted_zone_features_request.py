"""Generated from Smithy shape ``com.amazonaws.route53#UpdateHostedZoneFeaturesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.accelerated_recovery_enabled
    import aws_sdk_route_53.types.resource_id


class UpdateHostedZoneFeaturesRequest(TypedDict):
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone for which you want to update features. This is the unique identifier for your hosted zone.</p>"""
    enable_accelerated_recovery: NotRequired[
        "aws_sdk_route_53.types.accelerated_recovery_enabled.AcceleratedRecoveryEnabled"
    ]
    """<p>Specifies whether to enable accelerated recovery for the hosted zone. Set to <code>true</code> to enable accelerated recovery, or <code>false</code> to disable it.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateHostedZoneFeaturesRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "enable_accelerated_recovery" in value:
        SubElement(el, "EnableAcceleratedRecovery").text = (
            "true" if value["enable_accelerated_recovery"] else "false"
        )


def deserialize_xml(el: Element) -> UpdateHostedZoneFeaturesRequest:
    out: UpdateHostedZoneFeaturesRequest = {}  # type: ignore[typeddict-item]
    child_enable_accelerated_recovery = el.find("EnableAcceleratedRecovery")
    if child_enable_accelerated_recovery is not None:
        out["enable_accelerated_recovery"] = (
            child_enable_accelerated_recovery.text or ""
        ).lower() == "true"
    return out
