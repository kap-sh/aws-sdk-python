"""Generated from Smithy shape ``com.amazonaws.ivs#ListRecordingConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.max_recording_configuration_results
    import capo_ivs.types.pagination_token


class ListRecordingConfigurationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>The first recording configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "capo_ivs.types.max_recording_configuration_results.MaxRecordingConfigurationResults"
    ]
    """<p>Maximum number of recording configurations to return. Default: your service quota or 100, whichever is smaller. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecordingConfigurationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListRecordingConfigurationsRequest:
    out: ListRecordingConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
