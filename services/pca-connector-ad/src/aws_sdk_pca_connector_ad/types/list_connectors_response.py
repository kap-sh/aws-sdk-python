"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ListConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.connector_list
    import aws_sdk_pca_connector_ad.types.next_token


class ListConnectorsResponse(TypedDict, closed=True):
    connectors: NotRequired[
        "aws_sdk_pca_connector_ad.types.connector_list.ConnectorList"
    ]
    """<p>Summary information about each connector you have created.</p>"""
    next_token: NotRequired["aws_sdk_pca_connector_ad.types.next_token.NextToken"]
    """<p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the NextToken parameter from the response you just received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsResponse) -> dict:
    out: dict = {}
    if "connectors" in value:
        import aws_sdk_pca_connector_ad.types.connector_list

        out["Connectors"] = (
            aws_sdk_pca_connector_ad.types.connector_list.serialize_json(
                value["connectors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorsResponse:
    out: ListConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "Connectors" in data:
        import aws_sdk_pca_connector_ad.types.connector_list

        out["connectors"] = (
            aws_sdk_pca_connector_ad.types.connector_list.deserialize_json(
                data["Connectors"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
