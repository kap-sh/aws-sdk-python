"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryStatusWorkloadInsightsTopContributorsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_networkflowmonitor.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.query_status

class GetQueryStatusWorkloadInsightsTopContributorsOutput(TypedDict):
    status: "aws_sdk_networkflowmonitor.types.query_status.QueryStatus"
    """<p>When you run a query, use this call to check the status of the query to make sure that the query has <code>SUCCEEDED</code> before you review the results.</p> <ul> <li> <p> <code>QUEUED</code>: The query is scheduled to run.</p> </li> <li> <p> <code>RUNNING</code>: The query is in progress but not complete.</p> </li> <li> <p> <code>SUCCEEDED</code>: The query completed sucessfully.</p> </li> <li> <p> <code>FAILED</code>: The query failed due to an error.</p> </li> <li> <p> <code>CANCELED</code>: The query was canceled.</p> </li> </ul>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStatusWorkloadInsightsTopContributorsOutput) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.query_status
    out["status"] = aws_sdk_networkflowmonitor.types.query_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> GetQueryStatusWorkloadInsightsTopContributorsOutput:
    out: GetQueryStatusWorkloadInsightsTopContributorsOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_networkflowmonitor.types.query_status
        out["status"] = aws_sdk_networkflowmonitor.types.query_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("GetQueryStatusWorkloadInsightsTopContributorsOutput.status required")
    return out