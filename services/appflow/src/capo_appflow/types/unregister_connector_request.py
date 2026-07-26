"""Generated from Smithy shape ``com.amazonaws.appflow#UnregisterConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.connector_label


class UnregisterConnectorRequest(TypedDict, closed=True):
    connector_label: "capo_appflow.types.connector_label.ConnectorLabel"
    """<p>The label of the connector. The label is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account.</p>"""
    force_delete: "capo_appflow.types.boolean.Boolean"
    """<p>Indicates whether Amazon AppFlow should unregister the connector, even if it is currently in use in one or more connector profiles. The default value is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnregisterConnectorRequest) -> dict:
    out: dict = {}
    out["connectorLabel"] = value["connector_label"]
    out["forceDelete"] = value.get("force_delete", False)
    return out


def deserialize_json(data: dict) -> UnregisterConnectorRequest:
    out: UnregisterConnectorRequest = {}  # type: ignore[typeddict-item]
    if "connectorLabel" in data:
        out["connector_label"] = data["connectorLabel"]
    else:
        raise DeserializationError(
            "UnregisterConnectorRequest.connector_label required"
        )
    if "forceDelete" in data:
        out["force_delete"] = data["forceDelete"]
    else:
        out["force_delete"] = False
    return out
