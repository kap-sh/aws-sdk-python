"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyReservedInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ModifyReservedInstancesResult(TypedDict, closed=True):
    reserved_instances_modification_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID for the modification.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyReservedInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reserved_instances_modification_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedInstancesModificationId",
                str(value["reserved_instances_modification_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ModifyReservedInstancesResult:
    out: ModifyReservedInstancesResult = {}  # type: ignore[typeddict-item]
    child_reserved_instances_modification_id = el.find(
        "ReservedInstancesModificationId"
    )
    if child_reserved_instances_modification_id is not None:
        out["reserved_instances_modification_id"] = str(
            child_reserved_instances_modification_id.text or ""
        )
    return out
