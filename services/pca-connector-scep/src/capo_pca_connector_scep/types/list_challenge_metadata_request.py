"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ListChallengeMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.connector_arn
    import capo_pca_connector_scep.types.max_results
    import capo_pca_connector_scep.types.next_token


class ListChallengeMetadataRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_pca_connector_scep.types.max_results.MaxResults"]
    """<p>The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    next_token: NotRequired["capo_pca_connector_scep.types.next_token.NextToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    connector_arn: "capo_pca_connector_scep.types.connector_arn.ConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChallengeMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChallengeMetadataRequest:
    out: ListChallengeMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
