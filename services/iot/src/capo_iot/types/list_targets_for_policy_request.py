"""Generated from Smithy shape ``com.amazonaws.iot#ListTargetsForPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.marker
    import capo_iot.types.page_size
    import capo_iot.types.policy_name


class ListTargetsForPolicyRequest(TypedDict, closed=True):
    policy_name: "capo_iot.types.policy_name.PolicyName"
    """<p>The policy name.</p>"""
    marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>A marker used to get the next set of results.</p>"""
    page_size: NotRequired["capo_iot.types.page_size.PageSize"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsForPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTargetsForPolicyRequest:
    out: ListTargetsForPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
