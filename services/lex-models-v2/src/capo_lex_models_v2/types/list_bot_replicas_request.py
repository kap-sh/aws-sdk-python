"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotReplicasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id


class ListBotReplicasRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The request for the unique bot IDs in the list of replicated bots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotReplicasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBotReplicasRequest:
    out: ListBotReplicasRequest = {}  # type: ignore[typeddict-item]
    return out
