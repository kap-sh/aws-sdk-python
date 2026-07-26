"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateCloudConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.cloud_connector_description
    import capo_iot_managed_integrations.types.cloud_connector_id
    import capo_iot_managed_integrations.types.display_name


class UpdateCloudConnectorRequest(TypedDict, closed=True):
    identifier: (
        "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    )
    """<p>The unique identifier of the cloud connector to update.</p>"""
    name: NotRequired["capo_iot_managed_integrations.types.display_name.DisplayName"]
    """<p>The new display name to assign to the cloud connector.</p>"""
    description: NotRequired[
        "capo_iot_managed_integrations.types.cloud_connector_description.CloudConnectorDescription"
    ]
    """<p>The new description to assign to the cloud connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCloudConnectorRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateCloudConnectorRequest:
    out: UpdateCloudConnectorRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
