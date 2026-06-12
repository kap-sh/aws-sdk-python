"""Generated from Smithy shape ``com.amazonaws.iot#ListTargetsForPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.page_size
    import aws_sdk_iot.types.policy_name


class ListTargetsForPolicyRequest(TypedDict):
    policy_name: "aws_sdk_iot.types.policy_name.PolicyName"
    """<p>The policy name.</p>"""
    marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>A marker used to get the next set of results.</p>"""
    page_size: NotRequired["aws_sdk_iot.types.page_size.PageSize"]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsForPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTargetsForPolicyRequest:
    out: ListTargetsForPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
