"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetQueryStatusWorkloadInsightsTopContributorsDataInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.scope_id


class GetQueryStatusWorkloadInsightsTopContributorsDataInput(TypedDict):
    scope_id: "aws_sdk_networkflowmonitor.types.scope_id.ScopeId"
    """<p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account. A scope ID is returned from a <code>CreateScope</code> API call.</p>"""
    query_id: "str"
    """<p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetQueryStatusWorkloadInsightsTopContributorsDataInput,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> GetQueryStatusWorkloadInsightsTopContributorsDataInput:
    out: GetQueryStatusWorkloadInsightsTopContributorsDataInput = {}  # type: ignore[typeddict-item]
    return out
