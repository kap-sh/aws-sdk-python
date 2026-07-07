"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#StopQueryWorkloadInsightsTopContributorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.scope_id


class StopQueryWorkloadInsightsTopContributorsInput(TypedDict, closed=True):
    scope_id: "aws_sdk_networkflowmonitor.types.scope_id.ScopeId"
    """<p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>"""
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopQueryWorkloadInsightsTopContributorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopQueryWorkloadInsightsTopContributorsInput:
    out: StopQueryWorkloadInsightsTopContributorsInput = {}  # type: ignore[typeddict-item]
    return out
