"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeleteCloudConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.cloud_connector_id


class DeleteCloudConnectorRequest(TypedDict, closed=True):
    identifier: (
        "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    )
    """<p>The identifier of the cloud connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCloudConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCloudConnectorRequest:
    out: DeleteCloudConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
