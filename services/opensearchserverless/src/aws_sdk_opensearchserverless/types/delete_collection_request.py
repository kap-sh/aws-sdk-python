"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.collection_id


class DeleteCollectionRequest(TypedDict, closed=True):
    id: "aws_sdk_opensearchserverless.types.collection_id.CollectionId"
    r"""<p>The unique identifier of the collection. For example, <code>1iu5usc406kd</code>. The ID is part of the collection endpoint. You can also retrieve it using the <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html\">ListCollections</a> API.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCollectionRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCollectionRequest:
    out: DeleteCollectionRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteCollectionRequest.id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
