"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileShareSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_share_summary

ProfileShareSummaries: TypeAlias = list[
    "capo_wellarchitected.types.profile_share_summary.ProfileShareSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileShareSummaries) -> list:
    import capo_wellarchitected.types.profile_share_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.profile_share_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProfileShareSummaries:
    import capo_wellarchitected.types.profile_share_summary

    out: ProfileShareSummaries = []
    for item in data:
        out.append(
            capo_wellarchitected.types.profile_share_summary.deserialize_json(item)
        )
    return out
