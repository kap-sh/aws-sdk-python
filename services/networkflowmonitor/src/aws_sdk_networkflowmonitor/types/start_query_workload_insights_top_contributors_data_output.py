"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StartQueryWorkloadInsightsTopContributorsDataOutput``."""

from typing_extensions import TypedDict

from aws_sdk_networkflowmonitor.errors import DeserializationError


class StartQueryWorkloadInsightsTopContributorsDataOutput(TypedDict, closed=True):
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryWorkloadInsightsTopContributorsDataOutput) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> StartQueryWorkloadInsightsTopContributorsDataOutput:
    out: StartQueryWorkloadInsightsTopContributorsDataOutput = {}  # type: ignore[typeddict-item]
    if "queryId" in data:
        out["query_id"] = data["queryId"]
    else:
        raise DeserializationError(
            "StartQueryWorkloadInsightsTopContributorsDataOutput.query_id required"
        )
    return out
