"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsIntentNodeSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_node_count
    import aws_sdk_lex_models_v2.types.analytics_node_level
    import aws_sdk_lex_models_v2.types.analytics_node_type
    import aws_sdk_lex_models_v2.types.analytics_path
    import aws_sdk_lex_models_v2.types.name


class AnalyticsIntentNodeSummary(TypedDict):
    intent_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of the intent at the end of the requested path.</p>"""
    intent_path: NotRequired["aws_sdk_lex_models_v2.types.analytics_path.AnalyticsPath"]
    """<p>The path.</p>"""
    intent_count: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_node_count.AnalyticsNodeCount"
    ]
    """<p>The total number of sessions that follow the given path to the given intent.</p>"""
    intent_level: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_node_level.AnalyticsNodeLevel"
    ]
    """<p>The number of intents up to and including the requested path.</p>"""
    node_type: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_node_type.AnalyticsNodeType"
    ]
    """<p>Specifies whether the node is the end of a path (<code>Exit</code>) or not (<code>Inner</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsIntentNodeSummary) -> dict:
    out: dict = {}
    if "intent_name" in value:
        out["intentName"] = value["intent_name"]
    if "intent_path" in value:
        out["intentPath"] = value["intent_path"]
    if "intent_count" in value:
        out["intentCount"] = value["intent_count"]
    if "intent_level" in value:
        out["intentLevel"] = value["intent_level"]
    if "node_type" in value:
        import aws_sdk_lex_models_v2.types.analytics_node_type

        out["nodeType"] = (
            aws_sdk_lex_models_v2.types.analytics_node_type.serialize_json(
                value["node_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalyticsIntentNodeSummary:
    out: AnalyticsIntentNodeSummary = {}  # type: ignore[typeddict-item]
    if "intentName" in data:
        out["intent_name"] = data["intentName"]
    if "intentPath" in data:
        out["intent_path"] = data["intentPath"]
    if "intentCount" in data:
        out["intent_count"] = data["intentCount"]
    if "intentLevel" in data:
        out["intent_level"] = data["intentLevel"]
    if "nodeType" in data:
        import aws_sdk_lex_models_v2.types.analytics_node_type

        out["node_type"] = (
            aws_sdk_lex_models_v2.types.analytics_node_type.deserialize_json(
                data["nodeType"]
            )
        )
    return out
