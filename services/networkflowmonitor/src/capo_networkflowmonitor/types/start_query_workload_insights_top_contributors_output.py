"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StartQueryWorkloadInsightsTopContributorsOutput``."""

from typing_extensions import TypedDict

from capo_networkflowmonitor.errors import DeserializationError


class StartQueryWorkloadInsightsTopContributorsOutput(TypedDict, closed=True):
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryWorkloadInsightsTopContributorsOutput) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> StartQueryWorkloadInsightsTopContributorsOutput:
    out: StartQueryWorkloadInsightsTopContributorsOutput = {}  # type: ignore[typeddict-item]
    if "queryId" in data:
        out["query_id"] = data["queryId"]
    else:
        raise DeserializationError(
            "StartQueryWorkloadInsightsTopContributorsOutput.query_id required"
        )
    return out
