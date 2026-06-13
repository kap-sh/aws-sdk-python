"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#GetConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.connector_arn


class GetConnectorRequest(TypedDict):
    connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectorRequest:
    out: GetConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
