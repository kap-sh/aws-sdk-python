"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrunkInterfaceAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.trunk_interface_association_list


class DescribeTrunkInterfaceAssociationsResult(TypedDict):
    interface_associations: NotRequired[
        "aws_sdk_ec2.types.trunk_interface_association_list.TrunkInterfaceAssociationList"
    ]
    """<p>Information about the trunk associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrunkInterfaceAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "interface_associations" in value:
        import aws_sdk_ec2.types.trunk_interface_association_list

        aws_sdk_ec2.types.trunk_interface_association_list.serialize_ec2_query(
            value["interface_associations"], pairs, f"{prefix}.InterfaceAssociationSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTrunkInterfaceAssociationsResult:
    out: DescribeTrunkInterfaceAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("InterfaceAssociationSet") is not None:
        import aws_sdk_ec2.types.trunk_interface_association_list

        out["interface_associations"] = (
            aws_sdk_ec2.types.trunk_interface_association_list.deserialize_ec2_query(
                el, "InterfaceAssociationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
