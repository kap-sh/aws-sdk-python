"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_summary

LandingZoneSummaries: TypeAlias = list[
    "capo_controltower.types.landing_zone_summary.LandingZoneSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneSummaries) -> list:
    import capo_controltower.types.landing_zone_summary

    out: list = []
    for item in value:
        out.append(capo_controltower.types.landing_zone_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LandingZoneSummaries:
    import capo_controltower.types.landing_zone_summary

    out: LandingZoneSummaries = []
    for item in data:
        out.append(capo_controltower.types.landing_zone_summary.deserialize_json(item))
    return out
