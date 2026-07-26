"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_summary

ProfileSummaries: TypeAlias = list[
    "capo_wellarchitected.types.profile_summary.ProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileSummaries) -> list:
    import capo_wellarchitected.types.profile_summary

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.profile_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileSummaries:
    import capo_wellarchitected.types.profile_summary

    out: ProfileSummaries = []
    for item in data:
        out.append(capo_wellarchitected.types.profile_summary.deserialize_json(item))
    return out
