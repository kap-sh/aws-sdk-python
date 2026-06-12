"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneFeatures``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.accelerated_recovery_status
    import aws_sdk_route_53.types.hosted_zone_failure_reasons


class HostedZoneFeatures(TypedDict):
    accelerated_recovery_status: NotRequired[
        "aws_sdk_route_53.types.accelerated_recovery_status.AcceleratedRecoveryStatus"
    ]
    """<p>The current status of accelerated recovery for the hosted zone.</p>"""
    failure_reasons: NotRequired[
        "aws_sdk_route_53.types.hosted_zone_failure_reasons.HostedZoneFailureReasons"
    ]
    """<p>Information about any failures that occurred when attempting to enable or configure features for the hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HostedZoneFeatures, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "accelerated_recovery_status" in value:
        import aws_sdk_route_53.types.accelerated_recovery_status

        aws_sdk_route_53.types.accelerated_recovery_status.serialize_xml(
            value["accelerated_recovery_status"], el, "AcceleratedRecoveryStatus"
        )
    if "failure_reasons" in value:
        import aws_sdk_route_53.types.hosted_zone_failure_reasons

        aws_sdk_route_53.types.hosted_zone_failure_reasons.serialize_xml(
            value["failure_reasons"], el, "FailureReasons"
        )


def deserialize_xml(el: Element) -> HostedZoneFeatures:
    out: HostedZoneFeatures = {}  # type: ignore[typeddict-item]
    child_accelerated_recovery_status = el.find("AcceleratedRecoveryStatus")
    if child_accelerated_recovery_status is not None:
        import aws_sdk_route_53.types.accelerated_recovery_status

        out["accelerated_recovery_status"] = (
            aws_sdk_route_53.types.accelerated_recovery_status.deserialize_xml(
                child_accelerated_recovery_status
            )
        )
    child_failure_reasons = el.find("FailureReasons")
    if child_failure_reasons is not None:
        import aws_sdk_route_53.types.hosted_zone_failure_reasons

        out["failure_reasons"] = (
            aws_sdk_route_53.types.hosted_zone_failure_reasons.deserialize_xml(
                child_failure_reasons
            )
        )
    return out
