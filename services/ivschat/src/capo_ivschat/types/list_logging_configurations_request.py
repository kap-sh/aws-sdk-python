"""Generated from Smithy shape ``com.amazonaws.ivschat#ListLoggingConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.max_logging_configuration_results
    import capo_ivschat.types.pagination_token


class ListLoggingConfigurationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ivschat.types.pagination_token.PaginationToken"]
    """<p>The first logging configurations to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "capo_ivschat.types.max_logging_configuration_results.MaxLoggingConfigurationResults"
    ]
    """<p>Maximum number of logging configurations to return. Default: 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLoggingConfigurationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListLoggingConfigurationsRequest:
    out: ListLoggingConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
