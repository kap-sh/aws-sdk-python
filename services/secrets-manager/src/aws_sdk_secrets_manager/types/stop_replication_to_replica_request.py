"""Generated from Smithy shape ``com.amazonaws.secretsmanager#StopReplicationToReplicaRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_id_type


class StopReplicationToReplicaRequest(TypedDict):
    secret_id: "aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The name of the secret or the replica ARN. The replica ARN is the same as the original primary secret ARN expect the Region is changed to the replica Region. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopReplicationToReplicaRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopReplicationToReplicaRequest:
    out: StopReplicationToReplicaRequest = {}  # type: ignore[typeddict-item]
    if "SecretId" in data:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("StopReplicationToReplicaRequest.secret_id required")
    return out
