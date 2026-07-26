"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListProfilesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.profile_summaries


class ListProfilesOutput(TypedDict, closed=True):
    profile_summaries: NotRequired[
        "capo_wellarchitected.types.profile_summaries.ProfileSummaries"
    ]
    """<p>Profile summaries.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListProfilesOutput) -> dict:
    out: dict = {}
    if "profile_summaries" in value:
        import capo_wellarchitected.types.profile_summaries

        out["ProfileSummaries"] = (
            capo_wellarchitected.types.profile_summaries.serialize_json(
                value["profile_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfilesOutput:
    out: ListProfilesOutput = {}  # type: ignore[typeddict-item]
    if "ProfileSummaries" in data:
        import capo_wellarchitected.types.profile_summaries

        out["profile_summaries"] = (
            capo_wellarchitected.types.profile_summaries.deserialize_json(
                data["ProfileSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
