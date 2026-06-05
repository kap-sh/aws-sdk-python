"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseScheduledInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.purchased_scheduled_instance_set


class PurchaseScheduledInstancesResult(TypedDict):
    scheduled_instance_set: NotRequired[
        "aws_sdk_ec2.types.purchased_scheduled_instance_set.PurchasedScheduledInstanceSet"
    ]
    """<p>Information about the Scheduled Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseScheduledInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "scheduled_instance_set" in value:
        import aws_sdk_ec2.types.purchased_scheduled_instance_set

        aws_sdk_ec2.types.purchased_scheduled_instance_set.serialize_ec2_query(
            value["scheduled_instance_set"], pairs, f"{prefix}.ScheduledInstanceSet"
        )


def deserialize_ec2_query(el: Element) -> PurchaseScheduledInstancesResult:
    out: PurchaseScheduledInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("ScheduledInstanceSet") is not None:
        import aws_sdk_ec2.types.purchased_scheduled_instance_set

        out["scheduled_instance_set"] = (
            aws_sdk_ec2.types.purchased_scheduled_instance_set.deserialize_ec2_query(
                el, "ScheduledInstanceSet"
            )
        )
    return out
