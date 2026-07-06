"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GetConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.connector_arn


class GetConnectorRequest(TypedDict, closed=True):
    connector_arn: "aws_sdk_pca_connector_ad.types.connector_arn.ConnectorArn"
    r"""<p> The Amazon Resource Name (ARN) that was returned when you called <a href=\"https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html\">CreateConnector</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectorRequest:
    out: GetConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
