"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_list


class DescribeReservedInstancesResult(TypedDict, closed=True):
    reserved_instances: NotRequired[
        "capo_ec2.types.reserved_instances_list.ReservedInstancesList"
    ]
    """<p>A list of Reserved Instances.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReservedInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_instances" in value:
        import capo_ec2.types.reserved_instances_list

        capo_ec2.types.reserved_instances_list.serialize_ec2_query(
            value["reserved_instances"], pairs, f"{key_prefix}ReservedInstancesSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeReservedInstancesResult:
    out: DescribeReservedInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("ReservedInstancesSet") is not None:
        import capo_ec2.types.reserved_instances_list

        out["reserved_instances"] = (
            capo_ec2.types.reserved_instances_list.deserialize_ec2_query(
                el, "ReservedInstancesSet"
            )
        )
    return out
