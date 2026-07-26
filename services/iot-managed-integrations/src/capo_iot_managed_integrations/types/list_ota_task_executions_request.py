"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListOtaTaskExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.ota_next_token
    import capo_iot_managed_integrations.types.ota_task_id


class ListOtaTaskExecutionsRequest(TypedDict, closed=True):
    identifier: "capo_iot_managed_integrations.types.ota_task_id.OtaTaskId"
    """<p>The over-the-air (OTA) task id.</p>"""
    next_token: NotRequired[
        "capo_iot_managed_integrations.types.ota_next_token.OtaNextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""
    max_results: NotRequired[
        "capo_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOtaTaskExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOtaTaskExecutionsRequest:
    out: ListOtaTaskExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
