"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotVersionReplicasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version_replica_sort_by
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.replica_region


class ListBotVersionReplicasRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The request for the unique ID in the list of replicated bots.</p>"""
    replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion"
    """<p>The request for the region used in the list of replicated bots.</p>"""
    max_results: NotRequired["capo_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum results given in the list of replicated bots.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>The next token given in the list of replicated bots.</p>"""
    sort_by: NotRequired[
        "capo_lex_models_v2.types.bot_version_replica_sort_by.BotVersionReplicaSortBy"
    ]
    """<p>The requested sort category for the list of replicated bots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotVersionReplicasRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_by" in value:
        import capo_lex_models_v2.types.bot_version_replica_sort_by

        out["sortBy"] = (
            capo_lex_models_v2.types.bot_version_replica_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListBotVersionReplicasRequest:
    out: ListBotVersionReplicasRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortBy" in data:
        import capo_lex_models_v2.types.bot_version_replica_sort_by

        out["sort_by"] = (
            capo_lex_models_v2.types.bot_version_replica_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    return out
