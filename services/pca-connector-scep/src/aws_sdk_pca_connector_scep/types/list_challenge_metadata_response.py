"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ListChallengeMetadataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.challenge_metadata_list
    import aws_sdk_pca_connector_scep.types.next_token


class ListChallengeMetadataResponse(TypedDict):
    challenges: NotRequired[
        "aws_sdk_pca_connector_scep.types.challenge_metadata_list.ChallengeMetadataList"
    ]
    """<p>The challenge metadata for the challenges belonging to your Amazon Web Services account.</p>"""
    next_token: NotRequired["aws_sdk_pca_connector_scep.types.next_token.NextToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChallengeMetadataResponse) -> dict:
    out: dict = {}
    if "challenges" in value:
        import aws_sdk_pca_connector_scep.types.challenge_metadata_list

        out["Challenges"] = (
            aws_sdk_pca_connector_scep.types.challenge_metadata_list.serialize_json(
                value["challenges"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChallengeMetadataResponse:
    out: ListChallengeMetadataResponse = {}  # type: ignore[typeddict-item]
    if "Challenges" in data:
        import aws_sdk_pca_connector_scep.types.challenge_metadata_list

        out["challenges"] = (
            aws_sdk_pca_connector_scep.types.challenge_metadata_list.deserialize_json(
                data["Challenges"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
