"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListTargetGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.target_group_type
    import capo_vpc_lattice.types.vpc_id


class ListTargetGroupsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""
    vpc_identifier: NotRequired["capo_vpc_lattice.types.vpc_id.VpcId"]
    """<p>The ID or ARN of the VPC.</p>"""
    target_group_type: NotRequired[
        "capo_vpc_lattice.types.target_group_type.TargetGroupType"
    ]
    """<p>The target group type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTargetGroupsRequest:
    out: ListTargetGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
