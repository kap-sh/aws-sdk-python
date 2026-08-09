"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrunkInterfaceAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.trunk_interface_association_list


class DescribeTrunkInterfaceAssociationsResult(TypedDict, closed=True):
    interface_associations: NotRequired[
        "capo_ec2.types.trunk_interface_association_list.TrunkInterfaceAssociationList"
    ]
    """<p>Information about the trunk associations.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrunkInterfaceAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "interface_associations" in value:
        import capo_ec2.types.trunk_interface_association_list

        capo_ec2.types.trunk_interface_association_list.serialize_ec2_query(
            value["interface_associations"],
            pairs,
            f"{key_prefix}InterfaceAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTrunkInterfaceAssociationsResult:
    out: DescribeTrunkInterfaceAssociationsResult = {}  # type: ignore[typeddict-item]
    child_interface_associations = el.find("interfaceAssociationSet")
    if child_interface_associations is not None:
        import capo_ec2.types.trunk_interface_association_list

        out["interface_associations"] = (
            capo_ec2.types.trunk_interface_association_list.deserialize_ec2_query(
                child_interface_associations
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
