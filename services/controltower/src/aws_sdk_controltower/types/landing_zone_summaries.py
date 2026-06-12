"""Generated from Smithy shape ``com.amazonaws.controltower#LandingZoneSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.landing_zone_summary

LandingZoneSummaries: TypeAlias = list[
    "aws_sdk_controltower.types.landing_zone_summary.LandingZoneSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LandingZoneSummaries) -> list:
    import aws_sdk_controltower.types.landing_zone_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_controltower.types.landing_zone_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LandingZoneSummaries:
    import aws_sdk_controltower.types.landing_zone_summary

    out: LandingZoneSummaries = []
    for item in data:
        out.append(
            aws_sdk_controltower.types.landing_zone_summary.deserialize_json(item)
        )
    return out
