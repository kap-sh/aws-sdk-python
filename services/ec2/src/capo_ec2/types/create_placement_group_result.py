"""Generated from Smithy shape ``com.amazonaws.ec2#CreatePlacementGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.placement_group


class CreatePlacementGroupResult(TypedDict, closed=True):
    placement_group: NotRequired["capo_ec2.types.placement_group.PlacementGroup"]
    """<p>Information about the placement group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreatePlacementGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "placement_group" in value:
        import capo_ec2.types.placement_group

        capo_ec2.types.placement_group.serialize_ec2_query(
            value["placement_group"], pairs, f"{prefix}.PlacementGroup"
        )


def deserialize_ec2_query(el: Element) -> CreatePlacementGroupResult:
    out: CreatePlacementGroupResult = {}  # type: ignore[typeddict-item]
    child_placement_group = el.find("PlacementGroup")
    if child_placement_group is not None:
        import capo_ec2.types.placement_group

        out["placement_group"] = capo_ec2.types.placement_group.deserialize_ec2_query(
            child_placement_group
        )
    return out
