"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Goal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.attainment_goal
    import capo_application_signals.types.interval
    import capo_application_signals.types.warning_threshold


class Goal(TypedDict, closed=True):
    interval: NotRequired["capo_application_signals.types.interval.Interval"]
    """<p>The time period used to evaluate the SLO. It can be either a calendar interval or rolling interval.</p> <p>If you omit this parameter, a rolling interval of 7 days is used.</p>"""
    attainment_goal: NotRequired[
        "capo_application_signals.types.attainment_goal.AttainmentGoal"
    ]
    """<p>The threshold that determines if the goal is being met.</p> <p>If this is a period-based SLO, the attainment goal is the percentage of good periods that meet the threshold requirements to the total periods within the interval. For example, an attainment goal of 99.9% means that within your interval, you are targeting 99.9% of the periods to be in healthy state.</p> <p>If this is a request-based SLO, the attainment goal is the percentage of requests that must be successful to meet the attainment goal.</p> <p>If you omit this parameter, 99 is used to represent 99% as the attainment goal.</p>"""
    warning_threshold: NotRequired[
        "capo_application_signals.types.warning_threshold.WarningThreshold"
    ]
    """<p>The percentage of remaining budget over total budget that you want to get warnings for. If you omit this parameter, the default of 50.0 is used. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Goal) -> dict:
    out: dict = {}
    if "interval" in value:
        import capo_application_signals.types.interval

        out["Interval"] = capo_application_signals.types.interval.serialize_json(
            value["interval"]
        )
    if "attainment_goal" in value:
        out["AttainmentGoal"] = value["attainment_goal"]
    if "warning_threshold" in value:
        out["WarningThreshold"] = value["warning_threshold"]
    return out


def deserialize_json(data: dict) -> Goal:
    out: Goal = {}  # type: ignore[typeddict-item]
    if "Interval" in data:
        import capo_application_signals.types.interval

        out["interval"] = capo_application_signals.types.interval.deserialize_json(
            data["Interval"]
        )
    if "AttainmentGoal" in data:
        out["attainment_goal"] = data["AttainmentGoal"]
    if "WarningThreshold" in data:
        out["warning_threshold"] = data["WarningThreshold"]
    return out
