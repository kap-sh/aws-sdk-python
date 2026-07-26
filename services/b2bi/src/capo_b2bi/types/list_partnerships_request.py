"""Generated from Smithy shape ``com.amazonaws.b2bi#ListPartnershipsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.max_results
    import capo_b2bi.types.page_token
    import capo_b2bi.types.profile_id


class ListPartnershipsRequest(TypedDict, closed=True):
    profile_id: NotRequired["capo_b2bi.types.profile_id.ProfileId"]
    """<p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>"""
    next_token: NotRequired["capo_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""
    max_results: NotRequired["capo_b2bi.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of capabilities to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPartnershipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPartnershipsRequest:
    out: ListPartnershipsRequest = {}  # type: ignore[typeddict-item]
    return out
