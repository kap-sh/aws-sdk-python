"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListIngestConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.ingest_configuration_state
    import capo_ivs_realtime.types.max_ingest_configuration_results
    import capo_ivs_realtime.types.pagination_token
    import capo_ivs_realtime.types.stage_arn


class ListIngestConfigurationsRequest(TypedDict, closed=True):
    filter_by_stage_arn: NotRequired["capo_ivs_realtime.types.stage_arn.StageArn"]
    """<p>Filters the response list to match the specified stage ARN. Only one filter (by stage ARN or by state) can be used at a time.</p>"""
    filter_by_state: NotRequired[
        "capo_ivs_realtime.types.ingest_configuration_state.IngestConfigurationState"
    ]
    """<p>Filters the response list to match the specified state. Only one filter (by stage ARN or by state) can be used at a time.</p>"""
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>The first IngestConfiguration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "capo_ivs_realtime.types.max_ingest_configuration_results.MaxIngestConfigurationResults"
    ]
    """<p>Maximum number of results to return. Default: 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIngestConfigurationsRequest) -> dict:
    out: dict = {}
    if "filter_by_stage_arn" in value:
        out["filterByStageArn"] = value["filter_by_stage_arn"]
    if "filter_by_state" in value:
        out["filterByState"] = value["filter_by_state"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListIngestConfigurationsRequest:
    out: ListIngestConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "filterByStageArn" in data:
        out["filter_by_stage_arn"] = data["filterByStageArn"]
    if "filterByState" in data:
        out["filter_by_state"] = data["filterByState"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
