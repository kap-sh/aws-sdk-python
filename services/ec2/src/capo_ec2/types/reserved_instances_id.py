"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class ReservedInstancesId(TypedDict, closed=True):
    reserved_instances_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesId, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{key_prefix}ReservedInstancesId", str(value["reserved_instances_id"]))
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesId:
    out: ReservedInstancesId = {}  # type: ignore[typeddict-item]
    child_reserved_instances_id = el.find("ReservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    return out
