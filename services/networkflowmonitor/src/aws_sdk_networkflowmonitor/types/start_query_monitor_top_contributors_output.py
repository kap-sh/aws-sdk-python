"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StartQueryMonitorTopContributorsOutput``."""

from typing import TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError


class StartQueryMonitorTopContributorsOutput(TypedDict):
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryMonitorTopContributorsOutput) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> StartQueryMonitorTopContributorsOutput:
    out: StartQueryMonitorTopContributorsOutput = {}  # type: ignore[typeddict-item]
    if "queryId" in data:
        out["query_id"] = data["queryId"]
    else:
        raise DeserializationError(
            "StartQueryMonitorTopContributorsOutput.query_id required"
        )
    return out
