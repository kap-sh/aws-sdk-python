"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListIntentPathsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_intent_node_summaries


class ListIntentPathsResponse(TypedDict, closed=True):
    node_summaries: NotRequired[
        "capo_lex_models_v2.types.analytics_intent_node_summaries.AnalyticsIntentNodeSummaries"
    ]
    """<p>A list of objects, each of which contains information about a node in the intent path for which you requested metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntentPathsResponse) -> dict:
    out: dict = {}
    if "node_summaries" in value:
        import capo_lex_models_v2.types.analytics_intent_node_summaries

        out["nodeSummaries"] = (
            capo_lex_models_v2.types.analytics_intent_node_summaries.serialize_json(
                value["node_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListIntentPathsResponse:
    out: ListIntentPathsResponse = {}  # type: ignore[typeddict-item]
    if "nodeSummaries" in data:
        import capo_lex_models_v2.types.analytics_intent_node_summaries

        out["node_summaries"] = (
            capo_lex_models_v2.types.analytics_intent_node_summaries.deserialize_json(
                data["nodeSummaries"]
            )
        )
    return out
