"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.replica_region


class CreateBotReplicaRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The request for the unique bot ID of the source bot to be replicated in the secondary region.</p>"""
    replica_region: "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    """<p>The request for the secondary region that will be used in the replication of the source bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotReplicaRequest) -> dict:
    out: dict = {}
    out["replicaRegion"] = value["replica_region"]
    return out


def deserialize_json(data: dict) -> CreateBotReplicaRequest:
    out: CreateBotReplicaRequest = {}  # type: ignore[typeddict-item]
    if "replicaRegion" in data:
        out["replica_region"] = data["replicaRegion"]
    else:
        raise DeserializationError("CreateBotReplicaRequest.replica_region required")
    return out
