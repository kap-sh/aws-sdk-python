"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesModificationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_modification_list
    import capo_ec2.types.string


class DescribeReservedInstancesModificationsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    reserved_instances_modifications: NotRequired[
        "capo_ec2.types.reserved_instances_modification_list.ReservedInstancesModificationList"
    ]
    """<p>The Reserved Instance modification information.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReservedInstancesModificationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "reserved_instances_modifications" in value:
        import capo_ec2.types.reserved_instances_modification_list

        capo_ec2.types.reserved_instances_modification_list.serialize_ec2_query(
            value["reserved_instances_modifications"],
            pairs,
            f"{key_prefix}ReservedInstancesModificationsSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeReservedInstancesModificationsResult:
    out: DescribeReservedInstancesModificationsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("reservedInstancesModificationsSet") is not None:
        import capo_ec2.types.reserved_instances_modification_list

        out["reserved_instances_modifications"] = (
            capo_ec2.types.reserved_instances_modification_list.deserialize_ec2_query(
                el, "reservedInstancesModificationsSet"
            )
        )
    return out
