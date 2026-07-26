"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#GetConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.connector


class GetConnectorResponse(TypedDict, closed=True):
    connector: NotRequired["capo_pca_connector_scep.types.connector.Connector"]
    """<p>The properties of the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorResponse) -> dict:
    out: dict = {}
    if "connector" in value:
        import capo_pca_connector_scep.types.connector

        out["Connector"] = capo_pca_connector_scep.types.connector.serialize_json(
            value["connector"]
        )
    return out


def deserialize_json(data: dict) -> GetConnectorResponse:
    out: GetConnectorResponse = {}  # type: ignore[typeddict-item]
    if "Connector" in data:
        import capo_pca_connector_scep.types.connector

        out["connector"] = capo_pca_connector_scep.types.connector.deserialize_json(
            data["Connector"]
        )
    return out
