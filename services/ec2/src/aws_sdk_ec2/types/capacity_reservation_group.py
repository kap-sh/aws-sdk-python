"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CapacityReservationGroup(TypedDict):
    group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the resource group.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the resource group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group_arn" in value:
        pairs.append((f"{prefix}.GroupArn", str(value["group_arn"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))


def deserialize_ec2_query(el: Element) -> CapacityReservationGroup:
    out: CapacityReservationGroup = {}  # type: ignore[typeddict-item]
    child_group_arn = el.find("GroupArn")
    if child_group_arn is not None:
        out["group_arn"] = str(child_group_arn.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    return out
