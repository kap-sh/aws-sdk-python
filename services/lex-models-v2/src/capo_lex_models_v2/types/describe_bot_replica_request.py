"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotReplicaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.replica_region


class DescribeBotReplicaRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The request for the unique bot ID of the replicated bot being monitored.</p>"""
    replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion"
    """<p>The request for the region of the replicated bot being monitored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotReplicaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBotReplicaRequest:
    out: DescribeBotReplicaRequest = {}  # type: ignore[typeddict-item]
    return out
