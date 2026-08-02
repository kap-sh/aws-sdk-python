"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePlacementGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.placement_group_list


class DescribePlacementGroupsResult(TypedDict, closed=True):
    placement_groups: NotRequired[
        "capo_ec2.types.placement_group_list.PlacementGroupList"
    ]
    """<p>Information about the placement groups.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribePlacementGroupsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "placement_groups" in value:
        import capo_ec2.types.placement_group_list

        capo_ec2.types.placement_group_list.serialize_ec2_query(
            value["placement_groups"], pairs, f"{key_prefix}PlacementGroupSet"
        )


def deserialize_ec2_query(el: Element) -> DescribePlacementGroupsResult:
    out: DescribePlacementGroupsResult = {}  # type: ignore[typeddict-item]
    if el.find("PlacementGroupSet") is not None:
        import capo_ec2.types.placement_group_list

        out["placement_groups"] = (
            capo_ec2.types.placement_group_list.deserialize_ec2_query(
                el, "PlacementGroupSet"
            )
        )
    return out
