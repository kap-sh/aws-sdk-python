"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ListConnectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.connector_list
    import capo_pca_connector_scep.types.next_token


class ListConnectorsResponse(TypedDict, closed=True):
    connectors: NotRequired[
        "capo_pca_connector_scep.types.connector_list.ConnectorList"
    ]
    """<p>The connectors belonging to your Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_pca_connector_scep.types.next_token.NextToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsResponse) -> dict:
    out: dict = {}
    if "connectors" in value:
        import capo_pca_connector_scep.types.connector_list

        out["Connectors"] = capo_pca_connector_scep.types.connector_list.serialize_json(
            value["connectors"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorsResponse:
    out: ListConnectorsResponse = {}  # type: ignore[typeddict-item]
    if "Connectors" in data:
        import capo_pca_connector_scep.types.connector_list

        out["connectors"] = (
            capo_pca_connector_scep.types.connector_list.deserialize_json(
                data["Connectors"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
