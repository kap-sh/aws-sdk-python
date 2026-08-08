"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulInstanceCreditSpecificationItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.unsuccessful_instance_credit_specification_item_error


class UnsuccessfulInstanceCreditSpecificationItem(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    error: NotRequired[
        "capo_ec2.types.unsuccessful_instance_credit_specification_item_error.UnsuccessfulInstanceCreditSpecificationItemError"
    ]
    """<p>The applicable error for the burstable performance instance whose credit option for CPU usage was not modified.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnsuccessfulInstanceCreditSpecificationItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "error" in value:
        import capo_ec2.types.unsuccessful_instance_credit_specification_item_error

        capo_ec2.types.unsuccessful_instance_credit_specification_item_error.serialize_ec2_query(
            value["error"], pairs, f"{key_prefix}Error"
        )


def deserialize_ec2_query(el: Element) -> UnsuccessfulInstanceCreditSpecificationItem:
    out: UnsuccessfulInstanceCreditSpecificationItem = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_error = el.find("error")
    if child_error is not None:
        import capo_ec2.types.unsuccessful_instance_credit_specification_item_error

        out["error"] = (
            capo_ec2.types.unsuccessful_instance_credit_specification_item_error.deserialize_ec2_query(
                child_error
            )
        )
    return out
