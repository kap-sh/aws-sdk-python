"""Generated from Smithy shape ``com.amazonaws.pinpoint#MultiConditionalBranch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.simple_condition


class MultiConditionalBranch(TypedDict, closed=True):
    condition: NotRequired["capo_pinpoint.types.simple_condition.SimpleCondition"]
    """<p>The condition to evaluate for the activity path.</p>"""
    next_activity: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the next activity to perform, after completing the activity for the path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiConditionalBranch) -> dict:
    out: dict = {}
    if "condition" in value:
        import capo_pinpoint.types.simple_condition

        out["Condition"] = capo_pinpoint.types.simple_condition.serialize_json(
            value["condition"]
        )
    if "next_activity" in value:
        out["NextActivity"] = value["next_activity"]
    return out


def deserialize_json(data: dict) -> MultiConditionalBranch:
    out: MultiConditionalBranch = {}  # type: ignore[typeddict-item]
    if "Condition" in data:
        import capo_pinpoint.types.simple_condition

        out["condition"] = capo_pinpoint.types.simple_condition.deserialize_json(
            data["Condition"]
        )
    if "NextActivity" in data:
        out["next_activity"] = data["NextActivity"]
    return out
