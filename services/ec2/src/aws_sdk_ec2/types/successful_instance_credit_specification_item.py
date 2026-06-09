"""Generated from Smithy shape ``com.amazonaws.ec2#SuccessfulInstanceCreditSpecificationItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SuccessfulInstanceCreditSpecificationItem(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SuccessfulInstanceCreditSpecificationItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))


def deserialize_ec2_query(el: Element) -> SuccessfulInstanceCreditSpecificationItem:
    out: SuccessfulInstanceCreditSpecificationItem = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    return out
