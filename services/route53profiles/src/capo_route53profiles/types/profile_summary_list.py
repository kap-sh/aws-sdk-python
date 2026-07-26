"""Generated from Smithy shape ``com.amazonaws.route53profiles#ProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53profiles.types.profile_summary

ProfileSummaryList: TypeAlias = list[
    "capo_route53profiles.types.profile_summary.ProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileSummaryList) -> list:
    import capo_route53profiles.types.profile_summary

    out: list = []
    for item in value:
        out.append(capo_route53profiles.types.profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileSummaryList:
    import capo_route53profiles.types.profile_summary

    out: ProfileSummaryList = []
    for item in data:
        out.append(capo_route53profiles.types.profile_summary.deserialize_json(item))
    return out
