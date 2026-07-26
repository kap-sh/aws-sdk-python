"""Generated from Smithy shape ``com.amazonaws.eventbridge#PlacementStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.placement_strategy_field
    import capo_eventbridge.types.placement_strategy_type


class PlacementStrategy(TypedDict, closed=True):
    type: NotRequired[
        "capo_eventbridge.types.placement_strategy_type.PlacementStrategyType"
    ]
    """<p>The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task). </p>"""
    field: NotRequired[
        "capo_eventbridge.types.placement_strategy_field.PlacementStrategyField"
    ]
    """<p>The field to apply the placement strategy against. For the spread placement strategy, valid values are instanceId (or host, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as attribute:ecs.availability-zone. For the binpack placement strategy, valid values are cpu and memory. For the random placement strategy, this field is not used. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementStrategy) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_eventbridge.types.placement_strategy_type

        out["type"] = (
            capo_eventbridge.types.placement_strategy_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "field" in value:
        out["field"] = value["field"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacementStrategy:
    out: PlacementStrategy = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_eventbridge.types.placement_strategy_type

        out["type"] = (
            capo_eventbridge.types.placement_strategy_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "field" in data:
        out["field"] = data["field"]
    return out
