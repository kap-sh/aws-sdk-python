"""Generated from Smithy shape ``com.amazonaws.ec2#FailedQueuedPurchaseDeletion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.delete_queued_reserved_instances_error
    import capo_ec2.types.string


class FailedQueuedPurchaseDeletion(TypedDict, closed=True):
    error: NotRequired[
        "capo_ec2.types.delete_queued_reserved_instances_error.DeleteQueuedReservedInstancesError"
    ]
    """<p>The error.</p>"""
    reserved_instances_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FailedQueuedPurchaseDeletion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "error" in value:
        import capo_ec2.types.delete_queued_reserved_instances_error

        capo_ec2.types.delete_queued_reserved_instances_error.serialize_ec2_query(
            value["error"], pairs, f"{key_prefix}Error"
        )
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{key_prefix}ReservedInstancesId", str(value["reserved_instances_id"]))
        )


def deserialize_ec2_query(el: Element) -> FailedQueuedPurchaseDeletion:
    out: FailedQueuedPurchaseDeletion = {}  # type: ignore[typeddict-item]
    child_error = el.find("error")
    if child_error is not None:
        import capo_ec2.types.delete_queued_reserved_instances_error

        out["error"] = (
            capo_ec2.types.delete_queued_reserved_instances_error.deserialize_ec2_query(
                child_error
            )
        )
    child_reserved_instances_id = el.find("reservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    return out
