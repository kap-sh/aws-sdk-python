"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListProfileSharesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.list_profile_shares_max_results
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.profile_arn
    import capo_wellarchitected.types.share_status
    import capo_wellarchitected.types.shared_with_prefix


class ListProfileSharesInput(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.profile_arn.ProfileArn"
    """<p>The profile ARN.</p>"""
    shared_with_prefix: NotRequired[
        "capo_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
    ]
    """<p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the profile is shared.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "capo_wellarchitected.types.list_profile_shares_max_results.ListProfileSharesMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""
    status: NotRequired["capo_wellarchitected.types.share_status.ShareStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileSharesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfileSharesInput:
    out: ListProfileSharesInput = {}  # type: ignore[typeddict-item]
    return out
