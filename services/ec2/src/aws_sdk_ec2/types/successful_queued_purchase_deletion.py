"""Generated from Smithy shape ``com.amazonaws.ec2#SuccessfulQueuedPurchaseDeletion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SuccessfulQueuedPurchaseDeletion(TypedDict):
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SuccessfulQueuedPurchaseDeletion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{prefix}.ReservedInstancesId", str(value["reserved_instances_id"]))
        )


def deserialize_ec2_query(el: Element) -> SuccessfulQueuedPurchaseDeletion:
    out: SuccessfulQueuedPurchaseDeletion = {}  # type: ignore[typeddict-item]
    child_reserved_instances_id = el.find("ReservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    return out
