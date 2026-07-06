"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#CreateChallengeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pca_connector_scep.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.client_token
    import aws_sdk_pca_connector_scep.types.connector_arn
    import aws_sdk_pca_connector_scep.types.tags


class CreateChallengeRequest(TypedDict, closed=True):
    connector_arn: "aws_sdk_pca_connector_scep.types.connector_arn.ConnectorArn"
    """<p>The Amazon Resource Name (ARN) of the connector that you want to create a challenge for.</p>"""
    client_token: NotRequired[
        "aws_sdk_pca_connector_scep.types.client_token.ClientToken"
    ]
    r"""<p>Custom string that can be used to distinguish between calls to the <a href=\"https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html\">CreateChallenge</a> action. Client tokens for <code>CreateChallenge</code> time out after five minutes. Therefore, if you call <code>CreateChallenge</code> multiple times with the same client token within five minutes, Connector for SCEP recognizes that you are requesting only one challenge and will only respond with one. If you change the client token for each call, Connector for SCEP recognizes that you are requesting multiple challenge passwords.</p>"""
    tags: NotRequired["aws_sdk_pca_connector_scep.types.tags.Tags"]
    """<p>The key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChallengeRequest) -> dict:
    out: dict = {}
    out["ConnectorArn"] = value["connector_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_pca_connector_scep.types.tags

        out["Tags"] = aws_sdk_pca_connector_scep.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateChallengeRequest:
    out: CreateChallengeRequest = {}  # type: ignore[typeddict-item]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    else:
        raise DeserializationError("CreateChallengeRequest.connector_arn required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_pca_connector_scep.types.tags

        out["tags"] = aws_sdk_pca_connector_scep.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
