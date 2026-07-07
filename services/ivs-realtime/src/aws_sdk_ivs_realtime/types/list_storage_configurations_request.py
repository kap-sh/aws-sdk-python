"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListStorageConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.max_storage_configuration_results
    import aws_sdk_ivs_realtime.types.pagination_token


class ListStorageConfigurationsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>The first storage configuration to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "aws_sdk_ivs_realtime.types.max_storage_configuration_results.MaxStorageConfigurationResults"
    ]
    """<p>Maximum number of storage configurations to return. Default: your service quota or 100, whichever is smaller.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStorageConfigurationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListStorageConfigurationsRequest:
    out: ListStorageConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
