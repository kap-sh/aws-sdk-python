"""Generated from Smithy shape ``com.amazonaws.rds#ScalingConfigurationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class ScalingConfigurationInfo(TypedDict, closed=True):
    min_capacity: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The minimum capacity for an Aurora DB cluster in <code>serverless</code> DB engine mode.</p>"""
    max_capacity: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum capacity for an Aurora DB cluster in <code>serverless</code> DB engine mode.</p>"""
    auto_pause: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether automatic pause is allowed for the Aurora DB cluster in <code>serverless</code> DB engine mode.</p> <p>When the value is set to false for an Aurora Serverless v1 DB cluster, the DB cluster automatically resumes.</p>"""
    seconds_until_auto_pause: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The remaining amount of time, in seconds, before the Aurora DB cluster in <code>serverless</code> mode is paused. A DB cluster can be paused only when it's idle (it has no connections).</p>"""
    timeout_action: NotRequired["capo_rds.types.string.String"]
    """<p>The action that occurs when Aurora times out while attempting to change the capacity of an Aurora Serverless v1 cluster. The value is either <code>ForceApplyCapacityChange</code> or <code>RollbackCapacityChange</code>.</p> <p> <code>ForceApplyCapacityChange</code>, the default, sets the capacity to the specified value as soon as possible.</p> <p> <code>RollbackCapacityChange</code> ignores the capacity change if a scaling point isn't found in the timeout period.</p>"""
    seconds_before_timeout: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of seconds before scaling times out. What happens when an attempted scaling action times out is determined by the <code>TimeoutAction</code> setting.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScalingConfigurationInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min_capacity" in value:
        pairs.append((f"{prefix}.MinCapacity", str(value["min_capacity"])))
    if "max_capacity" in value:
        pairs.append((f"{prefix}.MaxCapacity", str(value["max_capacity"])))
    if "auto_pause" in value:
        pairs.append(
            (f"{prefix}.AutoPause", "true" if value["auto_pause"] else "false")
        )
    if "seconds_until_auto_pause" in value:
        pairs.append(
            (f"{prefix}.SecondsUntilAutoPause", str(value["seconds_until_auto_pause"]))
        )
    if "timeout_action" in value:
        pairs.append((f"{prefix}.TimeoutAction", str(value["timeout_action"])))
    if "seconds_before_timeout" in value:
        pairs.append(
            (f"{prefix}.SecondsBeforeTimeout", str(value["seconds_before_timeout"]))
        )


def deserialize_query(el: Element) -> ScalingConfigurationInfo:
    out: ScalingConfigurationInfo = {}  # type: ignore[typeddict-item]
    child_min_capacity = el.find("MinCapacity")
    if child_min_capacity is not None:
        out["min_capacity"] = int(child_min_capacity.text or "")
    child_max_capacity = el.find("MaxCapacity")
    if child_max_capacity is not None:
        out["max_capacity"] = int(child_max_capacity.text or "")
    child_auto_pause = el.find("AutoPause")
    if child_auto_pause is not None:
        out["auto_pause"] = (child_auto_pause.text or "").lower() == "true"
    child_seconds_until_auto_pause = el.find("SecondsUntilAutoPause")
    if child_seconds_until_auto_pause is not None:
        out["seconds_until_auto_pause"] = int(child_seconds_until_auto_pause.text or "")
    child_timeout_action = el.find("TimeoutAction")
    if child_timeout_action is not None:
        out["timeout_action"] = str(child_timeout_action.text or "")
    child_seconds_before_timeout = el.find("SecondsBeforeTimeout")
    if child_seconds_before_timeout is not None:
        out["seconds_before_timeout"] = int(child_seconds_before_timeout.text or "")
    return out
