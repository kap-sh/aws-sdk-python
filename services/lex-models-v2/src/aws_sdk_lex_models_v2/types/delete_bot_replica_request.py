"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DeleteBotReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.replica_region


class DeleteBotReplicaRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique ID of the replicated bot to be deleted from the secondary region</p>"""
    replica_region: "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    """<p>The secondary region of the replicated bot that will be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBotReplicaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBotReplicaRequest:
    out: DeleteBotReplicaRequest = {}  # type: ignore[typeddict-item]
    return out
