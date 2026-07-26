"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.conditions
    import capo_observabilityadmin.types.filter_behavior
    import capo_observabilityadmin.types.filter_requirement


class Filter(TypedDict, closed=True):
    behavior: NotRequired[
        "capo_observabilityadmin.types.filter_behavior.FilterBehavior"
    ]
    """<p> The action to take for log records matching this filter (KEEP or DROP). </p>"""
    requirement: NotRequired[
        "capo_observabilityadmin.types.filter_requirement.FilterRequirement"
    ]
    """<p> Whether the log record must meet all conditions (MEETS_ALL) or any condition (MEETS_ANY) to match this filter. </p>"""
    conditions: NotRequired["capo_observabilityadmin.types.conditions.Conditions"]
    """<p> The list of conditions that determine if a log record matches this filter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "behavior" in value:
        import capo_observabilityadmin.types.filter_behavior

        out["Behavior"] = capo_observabilityadmin.types.filter_behavior.serialize_json(
            value["behavior"]
        )
    if "requirement" in value:
        import capo_observabilityadmin.types.filter_requirement

        out["Requirement"] = (
            capo_observabilityadmin.types.filter_requirement.serialize_json(
                value["requirement"]
            )
        )
    if "conditions" in value:
        import capo_observabilityadmin.types.conditions

        out["Conditions"] = capo_observabilityadmin.types.conditions.serialize_json(
            value["conditions"]
        )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Behavior" in data:
        import capo_observabilityadmin.types.filter_behavior

        out["behavior"] = (
            capo_observabilityadmin.types.filter_behavior.deserialize_json(
                data["Behavior"]
            )
        )
    if "Requirement" in data:
        import capo_observabilityadmin.types.filter_requirement

        out["requirement"] = (
            capo_observabilityadmin.types.filter_requirement.deserialize_json(
                data["Requirement"]
            )
        )
    if "Conditions" in data:
        import capo_observabilityadmin.types.conditions

        out["conditions"] = capo_observabilityadmin.types.conditions.deserialize_json(
            data["Conditions"]
        )
    return out
