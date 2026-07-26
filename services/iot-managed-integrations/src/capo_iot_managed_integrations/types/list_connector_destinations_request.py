"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListConnectorDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.cloud_connector_id
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token


class ListConnectorDestinationsRequest(TypedDict, closed=True):
    cloud_connector_id: NotRequired[
        "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    ]
    """<p>The identifier of the cloud connector to filter connector destinations by.</p>"""
    next_token: NotRequired["capo_iot_managed_integrations.types.next_token.NextToken"]
    """<p>A token used for pagination of results.</p>"""
    max_results: NotRequired[
        "capo_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of connector destinations to return in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorDestinationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectorDestinationsRequest:
    out: ListConnectorDestinationsRequest = {}  # type: ignore[typeddict-item]
    return out
