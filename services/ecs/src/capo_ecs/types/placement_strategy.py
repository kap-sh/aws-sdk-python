"""Generated from Smithy shape ``com.amazonaws.ecs#PlacementStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.placement_strategy_type
    import capo_ecs.types.string


class PlacementStrategy(TypedDict, closed=True):
    type: NotRequired["capo_ecs.types.placement_strategy_type.PlacementStrategyType"]
    """<p>The type of placement strategy. The <code>random</code> placement strategy randomly places tasks on available candidates. The <code>spread</code> placement strategy spreads placement across available candidates evenly based on the <code>field</code> parameter. The <code>binpack</code> strategy places tasks on available candidates that have the least available amount of the resource that's specified with the <code>field</code> parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory but still enough to run the task.</p>"""
    field: NotRequired["capo_ecs.types.string.String"]
    """<p>The field to apply the placement strategy against. For the <code>spread</code> placement strategy, valid values are <code>instanceId</code> (or <code>host</code>, which has the same effect), or any platform or custom attribute that's applied to a container instance, such as <code>attribute:ecs.availability-zone</code>. For the <code>binpack</code> placement strategy, valid values are <code>cpu</code> and <code>memory</code>. For the <code>random</code> placement strategy, this field is not used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementStrategy) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_ecs.types.placement_strategy_type

        out["type"] = capo_ecs.types.placement_strategy_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "field" in value:
        out["field"] = value["field"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacementStrategy:
    out: PlacementStrategy = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_ecs.types.placement_strategy_type

        out["type"] = capo_ecs.types.placement_strategy_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if data.get("field") is not None:
        out["field"] = data["field"]
    return out
