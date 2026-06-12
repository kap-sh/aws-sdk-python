"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListBotVersionReplicasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_version_replica_sort_by
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.max_results
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.replica_region


class ListBotVersionReplicasRequest(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The request for the unique ID in the list of replicated bots.</p>"""
    replica_region: "aws_sdk_lex_models_v2.types.replica_region.ReplicaRegion"
    """<p>The request for the region used in the list of replicated bots.</p>"""
    max_results: NotRequired["aws_sdk_lex_models_v2.types.max_results.MaxResults"]
    """<p>The maximum results given in the list of replicated bots.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>The next token given in the list of replicated bots.</p>"""
    sort_by: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_version_replica_sort_by.BotVersionReplicaSortBy"
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
        import aws_sdk_lex_models_v2.types.bot_version_replica_sort_by

        out["sortBy"] = (
            aws_sdk_lex_models_v2.types.bot_version_replica_sort_by.serialize_json(
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
        import aws_sdk_lex_models_v2.types.bot_version_replica_sort_by

        out["sort_by"] = (
            aws_sdk_lex_models_v2.types.bot_version_replica_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    return out
