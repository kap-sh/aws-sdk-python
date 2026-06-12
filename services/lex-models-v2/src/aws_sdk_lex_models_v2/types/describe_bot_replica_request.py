"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotReplicaRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.replica_region


class DescribeBotReplicaRequest(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The request for the unique bot ID of the replicated bot being monitored.</p>"""
    replica_region: "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    """<p>The request for the region of the replicated bot being monitored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotReplicaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBotReplicaRequest:
    out: DescribeBotReplicaRequest = {}  # type: ignore[typeddict-item]
    return out
