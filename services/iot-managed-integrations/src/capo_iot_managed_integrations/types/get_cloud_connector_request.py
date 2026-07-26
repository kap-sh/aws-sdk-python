"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetCloudConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.cloud_connector_id


class GetCloudConnectorRequest(TypedDict, closed=True):
    identifier: (
        "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    )
    """<p>The identifier of the C2C connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCloudConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCloudConnectorRequest:
    out: GetCloudConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
