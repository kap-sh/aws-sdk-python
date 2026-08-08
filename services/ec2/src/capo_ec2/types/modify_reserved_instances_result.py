"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyReservedInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class ModifyReservedInstancesResult(TypedDict, closed=True):
    reserved_instances_modification_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID for the modification.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyReservedInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_instances_modification_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedInstancesModificationId",
                str(value["reserved_instances_modification_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ModifyReservedInstancesResult:
    out: ModifyReservedInstancesResult = {}  # type: ignore[typeddict-item]
    child_reserved_instances_modification_id = el.find(
        "reservedInstancesModificationId"
    )
    if child_reserved_instances_modification_id is not None:
        out["reserved_instances_modification_id"] = str(
            child_reserved_instances_modification_id.text or ""
        )
    return out
