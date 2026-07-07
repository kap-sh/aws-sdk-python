"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryStatusWorkloadInsightsTopContributorsDataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.query_status


class GetQueryStatusWorkloadInsightsTopContributorsDataOutput(TypedDict, closed=True):
    status: "aws_sdk_networkflowmonitor.types.query_status.QueryStatus"
    """<p>The status of a query for top contributors data.</p> <ul> <li> <p> <code>QUEUED</code>: The query is scheduled to run.</p> </li> <li> <p> <code>RUNNING</code>: The query is in progress but not complete.</p> </li> <li> <p> <code>SUCCEEDED</code>: The query completed sucessfully.</p> </li> <li> <p> <code>FAILED</code>: The query failed due to an error.</p> </li> <li> <p> <code>CANCELED</code>: The query was canceled.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetQueryStatusWorkloadInsightsTopContributorsDataOutput,
) -> dict:
    out: dict = {}
    import aws_sdk_networkflowmonitor.types.query_status

    out["status"] = aws_sdk_networkflowmonitor.types.query_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(
    data: dict,
) -> GetQueryStatusWorkloadInsightsTopContributorsDataOutput:
    out: GetQueryStatusWorkloadInsightsTopContributorsDataOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_networkflowmonitor.types.query_status

        out["status"] = aws_sdk_networkflowmonitor.types.query_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError(
            "GetQueryStatusWorkloadInsightsTopContributorsDataOutput.status required"
        )
    return out
