"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogCloudWatchLogsDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.verified_access_log_delivery_status


class VerifiedAccessLogCloudWatchLogsDestination(TypedDict, closed=True):
    enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    delivery_status: NotRequired[
        "capo_ec2.types.verified_access_log_delivery_status.VerifiedAccessLogDeliveryStatus"
    ]
    """<p>The delivery status for access logs.</p>"""
    log_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the CloudWatch Logs log group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessLogCloudWatchLogsDestination,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))
    if "delivery_status" in value:
        import capo_ec2.types.verified_access_log_delivery_status

        capo_ec2.types.verified_access_log_delivery_status.serialize_ec2_query(
            value["delivery_status"], pairs, f"{prefix}.DeliveryStatus"
        )
    if "log_group" in value:
        pairs.append((f"{prefix}.LogGroup", str(value["log_group"])))


def deserialize_ec2_query(el: Element) -> VerifiedAccessLogCloudWatchLogsDestination:
    out: VerifiedAccessLogCloudWatchLogsDestination = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_delivery_status = el.find("DeliveryStatus")
    if child_delivery_status is not None:
        import capo_ec2.types.verified_access_log_delivery_status

        out["delivery_status"] = (
            capo_ec2.types.verified_access_log_delivery_status.deserialize_ec2_query(
                child_delivery_status
            )
        )
    child_log_group = el.find("LogGroup")
    if child_log_group is not None:
        out["log_group"] = str(child_log_group.text or "")
    return out
