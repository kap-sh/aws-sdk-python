"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#GetConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.connector


class GetConnectorResponse(TypedDict):
    connector: NotRequired["aws_sdk_pca_connector_scep.types.connector.Connector"]
    """<p>The properties of the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorResponse) -> dict:
    out: dict = {}
    if "connector" in value:
        import aws_sdk_pca_connector_scep.types.connector

        out["Connector"] = aws_sdk_pca_connector_scep.types.connector.serialize_json(
            value["connector"]
        )
    return out


def deserialize_json(data: dict) -> GetConnectorResponse:
    out: GetConnectorResponse = {}  # type: ignore[typeddict-item]
    if "Connector" in data:
        import aws_sdk_pca_connector_scep.types.connector

        out["connector"] = aws_sdk_pca_connector_scep.types.connector.deserialize_json(
            data["Connector"]
        )
    return out
