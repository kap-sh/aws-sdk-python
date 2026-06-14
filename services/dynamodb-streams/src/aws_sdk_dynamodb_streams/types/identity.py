"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#Identity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb_streams.types.string


class Identity(TypedDict):
    principal_id: NotRequired["aws_sdk_dynamodb_streams.types.string.String"]
    r"""<p>A unique identifier for the entity that made the call. For Time To Live, the principalId is \"dynamodb.amazonaws.com\".</p>"""
    type: NotRequired["aws_sdk_dynamodb_streams.types.string.String"]
    r"""<p>The type of the identity. For Time To Live, the type is \"Service\".</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Identity) -> dict:
    out: dict = {}
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Identity:
    out: Identity = {}  # type: ignore[typeddict-item]
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
