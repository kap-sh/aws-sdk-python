"""Generated from Smithy shape ``com.amazonaws.deadline#ListSessionsForWorkerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.max_results
    import aws_sdk_deadline.types.next_token
    import aws_sdk_deadline.types.worker_id


class ListSessionsForWorkerRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the session.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID for the session.</p>"""
    worker_id: "aws_sdk_deadline.types.worker_id.WorkerId"
    """<p>The worker ID for the session.</p>"""
    next_token: NotRequired["aws_sdk_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: "aws_sdk_deadline.types.max_results.MaxResults"
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsForWorkerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSessionsForWorkerRequest:
    out: ListSessionsForWorkerRequest = {}  # type: ignore[typeddict-item]
    return out
