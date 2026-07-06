"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GetConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.connector


class GetConnectorResponse(TypedDict, closed=True):
    connector: NotRequired["aws_sdk_pca_connector_ad.types.connector.Connector"]
    """<p>A structure that contains information about your connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorResponse) -> dict:
    out: dict = {}
    if "connector" in value:
        import aws_sdk_pca_connector_ad.types.connector

        out["Connector"] = aws_sdk_pca_connector_ad.types.connector.serialize_json(
            value["connector"]
        )
    return out


def deserialize_json(data: dict) -> GetConnectorResponse:
    out: GetConnectorResponse = {}  # type: ignore[typeddict-item]
    if "Connector" in data:
        import aws_sdk_pca_connector_ad.types.connector

        out["connector"] = aws_sdk_pca_connector_ad.types.connector.deserialize_json(
            data["Connector"]
        )
    return out
