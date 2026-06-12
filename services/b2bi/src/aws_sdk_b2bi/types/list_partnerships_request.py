"""Generated from Smithy shape ``com.amazonaws.b2bi#ListPartnershipsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.max_results
    import aws_sdk_b2bi.types.page_token
    import aws_sdk_b2bi.types.profile_id


class ListPartnershipsRequest(TypedDict):
    profile_id: NotRequired["aws_sdk_b2bi.types.profile_id.ProfileId"]
    """<p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>"""
    next_token: NotRequired["aws_sdk_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""
    max_results: NotRequired["aws_sdk_b2bi.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of capabilities to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPartnershipsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPartnershipsRequest:
    out: ListPartnershipsRequest = {}  # type: ignore[typeddict-item]
    return out
