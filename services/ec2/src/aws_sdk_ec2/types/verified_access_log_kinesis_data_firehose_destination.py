"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessLogKinesisDataFirehoseDestination``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_log_delivery_status


class VerifiedAccessLogKinesisDataFirehoseDestination(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    delivery_status: NotRequired[
        "aws_sdk_ec2.types.verified_access_log_delivery_status.VerifiedAccessLogDeliveryStatus"
    ]
    """<p>The delivery status.</p>"""
    delivery_stream: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the delivery stream.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessLogKinesisDataFirehoseDestination,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))
    if "delivery_status" in value:
        import aws_sdk_ec2.types.verified_access_log_delivery_status

        aws_sdk_ec2.types.verified_access_log_delivery_status.serialize_ec2_query(
            value["delivery_status"], pairs, f"{prefix}.DeliveryStatus"
        )
    if "delivery_stream" in value:
        pairs.append((f"{prefix}.DeliveryStream", str(value["delivery_stream"])))


def deserialize_ec2_query(
    el: Element,
) -> VerifiedAccessLogKinesisDataFirehoseDestination:
    out: VerifiedAccessLogKinesisDataFirehoseDestination = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    child_delivery_status = el.find("DeliveryStatus")
    if child_delivery_status is not None:
        import aws_sdk_ec2.types.verified_access_log_delivery_status

        out["delivery_status"] = (
            aws_sdk_ec2.types.verified_access_log_delivery_status.deserialize_ec2_query(
                child_delivery_status
            )
        )
    child_delivery_stream = el.find("DeliveryStream")
    if child_delivery_stream is not None:
        out["delivery_stream"] = str(child_delivery_stream.text or "")
    return out
