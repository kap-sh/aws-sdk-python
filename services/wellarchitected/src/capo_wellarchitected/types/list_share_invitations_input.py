"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListShareInvitationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_name_prefix
    import capo_wellarchitected.types.list_share_invitations_max_results
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.profile_name_prefix
    import capo_wellarchitected.types.share_resource_type
    import capo_wellarchitected.types.template_name_prefix
    import capo_wellarchitected.types.workload_name_prefix


class ListShareInvitationsInput(TypedDict, closed=True):
    workload_name_prefix: NotRequired[
        "capo_wellarchitected.types.workload_name_prefix.WorkloadNamePrefix"
    ]
    lens_name_prefix: NotRequired[
        "capo_wellarchitected.types.lens_name_prefix.LensNamePrefix"
    ]
    """<p>An optional string added to the beginning of each lens name returned in the results.</p>"""
    share_resource_type: NotRequired[
        "capo_wellarchitected.types.share_resource_type.ShareResourceType"
    ]
    """<p>The type of share invitations to be returned.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "capo_wellarchitected.types.list_share_invitations_max_results.ListShareInvitationsMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""
    profile_name_prefix: NotRequired[
        "capo_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
    ]
    """<p>An optional string added to the beginning of each profile name returned in the results.</p>"""
    template_name_prefix: NotRequired[
        "capo_wellarchitected.types.template_name_prefix.TemplateNamePrefix"
    ]
    """<p>An optional string added to the beginning of each review template name returned in the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListShareInvitationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListShareInvitationsInput:
    out: ListShareInvitationsInput = {}  # type: ignore[typeddict-item]
    return out
