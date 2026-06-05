"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulInstanceCreditSpecificationItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item_error


class UnsuccessfulInstanceCreditSpecificationItem(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    error: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item_error.UnsuccessfulInstanceCreditSpecificationItemError"
    ]
    """<p>The applicable error for the burstable performance instance whose credit option for CPU usage was not modified.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnsuccessfulInstanceCreditSpecificationItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "error" in value:
        import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item_error

        aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item_error.serialize_ec2_query(
            value["error"], pairs, f"{prefix}.Error"
        )


def deserialize_ec2_query(el: Element) -> UnsuccessfulInstanceCreditSpecificationItem:
    out: UnsuccessfulInstanceCreditSpecificationItem = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_error = el.find("Error")
    if child_error is not None:
        import aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item_error

        out["error"] = (
            aws_sdk_ec2.types.unsuccessful_instance_credit_specification_item_error.deserialize_ec2_query(
                child_error
            )
        )
    return out
