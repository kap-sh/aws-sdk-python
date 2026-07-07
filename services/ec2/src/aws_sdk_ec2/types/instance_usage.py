"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class InstanceUsage(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that is making use of the Capacity Reservation.</p>"""
    used_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances the Amazon Web Services account currently has in the Capacity Reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceUsage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "account_id" in value:
        pairs.append((f"{prefix}.AccountId", str(value["account_id"])))
    if "used_instance_count" in value:
        pairs.append((f"{prefix}.UsedInstanceCount", str(value["used_instance_count"])))


def deserialize_ec2_query(el: Element) -> InstanceUsage:
    out: InstanceUsage = {}  # type: ignore[typeddict-item]
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_used_instance_count = el.find("UsedInstanceCount")
    if child_used_instance_count is not None:
        out["used_instance_count"] = int(child_used_instance_count.text or "")
    return out
