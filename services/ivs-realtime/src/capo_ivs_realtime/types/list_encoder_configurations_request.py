"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListEncoderConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.max_encoder_configuration_results
    import capo_ivs_realtime.types.pagination_token


class ListEncoderConfigurationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>The first encoder configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "capo_ivs_realtime.types.max_encoder_configuration_results.MaxEncoderConfigurationResults"
    ]
    """<p>Maximum number of results to return. Default: 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEncoderConfigurationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListEncoderConfigurationsRequest:
    out: ListEncoderConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
