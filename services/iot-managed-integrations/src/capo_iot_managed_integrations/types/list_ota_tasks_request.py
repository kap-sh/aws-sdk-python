"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListOtaTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.ota_next_token


class ListOtaTasksRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_iot_managed_integrations.types.ota_next_token.OtaNextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""
    max_results: NotRequired[
        "capo_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOtaTasksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOtaTasksRequest:
    out: ListOtaTasksRequest = {}  # type: ignore[typeddict-item]
    return out
