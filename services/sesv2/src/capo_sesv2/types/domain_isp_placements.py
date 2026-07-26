"""Generated from Smithy shape ``com.amazonaws.sesv2#DomainIspPlacements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.domain_isp_placement

DomainIspPlacements: TypeAlias = list[
    "capo_sesv2.types.domain_isp_placement.DomainIspPlacement"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainIspPlacements) -> list:
    import capo_sesv2.types.domain_isp_placement

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.domain_isp_placement.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainIspPlacements:
    import capo_sesv2.types.domain_isp_placement

    out: DomainIspPlacements = []
    for item in data:
        out.append(capo_sesv2.types.domain_isp_placement.deserialize_json(item))
    return out
