"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#StrategyOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.boolean
    import aws_sdk_migrationhubstrategy.types.strategy
    import aws_sdk_migrationhubstrategy.types.target_destination
    import aws_sdk_migrationhubstrategy.types.transformation_tool_name


class StrategyOption(TypedDict):
    strategy: NotRequired["aws_sdk_migrationhubstrategy.types.strategy.Strategy"]
    """<p> Type of transformation. For example, Rehost, Replatform, and so on. </p>"""
    tool_name: NotRequired[
        "aws_sdk_migrationhubstrategy.types.transformation_tool_name.TransformationToolName"
    ]
    """<p> The name of the tool that can be used to transform an application component using this strategy. </p>"""
    target_destination: NotRequired[
        "aws_sdk_migrationhubstrategy.types.target_destination.TargetDestination"
    ]
    """<p> Destination information about where the application component can migrate to. For example, <code>EC2</code>, <code>ECS</code>, and so on. </p>"""
    is_preferred: NotRequired["aws_sdk_migrationhubstrategy.types.boolean.Boolean"]
    """<p> Indicates if a specific strategy is preferred for the application component. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StrategyOption) -> dict:
    out: dict = {}
    if "strategy" in value:
        out["strategy"] = value["strategy"]
    if "tool_name" in value:
        out["toolName"] = value["tool_name"]
    if "target_destination" in value:
        out["targetDestination"] = value["target_destination"]
    if "is_preferred" in value:
        out["isPreferred"] = value["is_preferred"]
    return out


def deserialize_json(data: dict) -> StrategyOption:
    out: StrategyOption = {}  # type: ignore[typeddict-item]
    if "strategy" in data:
        out["strategy"] = data["strategy"]
    if "toolName" in data:
        out["tool_name"] = data["toolName"]
    if "targetDestination" in data:
        out["target_destination"] = data["targetDestination"]
    if "isPreferred" in data:
        out["is_preferred"] = data["isPreferred"]
    return out
