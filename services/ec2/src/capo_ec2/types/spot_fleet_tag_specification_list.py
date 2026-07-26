"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetTagSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.spot_fleet_tag_specification

SpotFleetTagSpecificationList: TypeAlias = list[
    "capo_ec2.types.spot_fleet_tag_specification.SpotFleetTagSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotFleetTagSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.spot_fleet_tag_specification

        capo_ec2.types.spot_fleet_tag_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SpotFleetTagSpecificationList:
    import capo_ec2.types.spot_fleet_tag_specification

    out: SpotFleetTagSpecificationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.spot_fleet_tag_specification.deserialize_ec2_query(child)
        )
    return out
