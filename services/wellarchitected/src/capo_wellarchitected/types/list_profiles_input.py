"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListProfilesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.profile_name_prefix
    import capo_wellarchitected.types.profile_owner_type


class ListProfilesInput(TypedDict, closed=True):
    profile_name_prefix: NotRequired[
        "capo_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
    ]
    """<p>An optional string added to the beginning of each profile name returned in the results.</p>"""
    profile_owner_type: NotRequired[
        "capo_wellarchitected.types.profile_owner_type.ProfileOwnerType"
    ]
    """<p>Profile owner type.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]


# --- restJson1 ser/de ---
def serialize_json(value: ListProfilesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfilesInput:
    out: ListProfilesInput = {}  # type: ignore[typeddict-item]
    return out
