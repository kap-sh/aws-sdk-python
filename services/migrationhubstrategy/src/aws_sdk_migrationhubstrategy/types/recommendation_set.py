"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#RecommendationSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.strategy
    import aws_sdk_migrationhubstrategy.types.target_destination
    import aws_sdk_migrationhubstrategy.types.transformation_tool


class RecommendationSet(TypedDict):
    transformation_tool: NotRequired[
        "aws_sdk_migrationhubstrategy.types.transformation_tool.TransformationTool"
    ]
    """<p> The target destination for the recommendation set. </p>"""
    target_destination: NotRequired[
        "aws_sdk_migrationhubstrategy.types.target_destination.TargetDestination"
    ]
    """<p> The recommended target destination. </p>"""
    strategy: NotRequired["aws_sdk_migrationhubstrategy.types.strategy.Strategy"]
    """<p> The recommended strategy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationSet) -> dict:
    out: dict = {}
    if "transformation_tool" in value:
        import aws_sdk_migrationhubstrategy.types.transformation_tool

        out["transformationTool"] = (
            aws_sdk_migrationhubstrategy.types.transformation_tool.serialize_json(
                value["transformation_tool"]
            )
        )
    if "target_destination" in value:
        out["targetDestination"] = value["target_destination"]
    if "strategy" in value:
        out["strategy"] = value["strategy"]
    return out


def deserialize_json(data: dict) -> RecommendationSet:
    out: RecommendationSet = {}  # type: ignore[typeddict-item]
    if "transformationTool" in data:
        import aws_sdk_migrationhubstrategy.types.transformation_tool

        out["transformation_tool"] = (
            aws_sdk_migrationhubstrategy.types.transformation_tool.deserialize_json(
                data["transformationTool"]
            )
        )
    if "targetDestination" in data:
        out["target_destination"] = data["targetDestination"]
    if "strategy" in data:
        out["strategy"] = data["strategy"]
    return out
