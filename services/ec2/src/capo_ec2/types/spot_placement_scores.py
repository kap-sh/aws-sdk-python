"""Generated from Smithy shape ``com.amazonaws.ec2#SpotPlacementScores``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_placement_score

SpotPlacementScores: TypeAlias = list[
    "capo_ec2.types.spot_placement_score.SpotPlacementScore"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotPlacementScores, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.spot_placement_score

        capo_ec2.types.spot_placement_score.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SpotPlacementScores:
    import capo_ec2.types.spot_placement_score

    out: SpotPlacementScores = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.spot_placement_score.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SpotPlacementScores:
    import capo_ec2.types.spot_placement_score

    out: SpotPlacementScores = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.spot_placement_score.deserialize_ec2_query(child))
    return out
