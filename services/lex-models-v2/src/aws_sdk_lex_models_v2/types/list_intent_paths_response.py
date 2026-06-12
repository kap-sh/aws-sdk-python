"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListIntentPathsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_intent_node_summaries


class ListIntentPathsResponse(TypedDict):
    node_summaries: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_intent_node_summaries.AnalyticsIntentNodeSummaries"
    ]
    """<p>A list of objects, each of which contains information about a node in the intent path for which you requested metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntentPathsResponse) -> dict:
    out: dict = {}
    if "node_summaries" in value:
        import aws_sdk_lex_models_v2.types.analytics_intent_node_summaries

        out["nodeSummaries"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_node_summaries.serialize_json(
                value["node_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListIntentPathsResponse:
    out: ListIntentPathsResponse = {}  # type: ignore[typeddict-item]
    if "nodeSummaries" in data:
        import aws_sdk_lex_models_v2.types.analytics_intent_node_summaries

        out["node_summaries"] = (
            aws_sdk_lex_models_v2.types.analytics_intent_node_summaries.deserialize_json(
                data["nodeSummaries"]
            )
        )
    return out
