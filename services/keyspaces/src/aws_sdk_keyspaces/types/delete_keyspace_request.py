"""Generated from Smithy shape ``com.amazonaws.keyspaces#DeleteKeyspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.keyspace_name


class DeleteKeyspaceRequest(TypedDict, closed=True):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteKeyspaceRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteKeyspaceRequest:
    out: DeleteKeyspaceRequest = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("DeleteKeyspaceRequest.keyspace_name required")
    return out
