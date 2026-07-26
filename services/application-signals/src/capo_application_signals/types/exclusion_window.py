"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ExclusionWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.exclusion_reason
    import capo_application_signals.types.recurrence_rule
    import capo_application_signals.types.window


class ExclusionWindow(TypedDict, closed=True):
    window: "capo_application_signals.types.window.Window"
    """<p>The SLO time window exclusion .</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The start of the SLO time window exclusion. Defaults to current time if not specified.</p>"""
    recurrence_rule: NotRequired[
        "capo_application_signals.types.recurrence_rule.RecurrenceRule"
    ]
    """<p>The recurrence rule for the SLO time window exclusion. Supports both cron and rate expressions.</p>"""
    reason: NotRequired[
        "capo_application_signals.types.exclusion_reason.ExclusionReason"
    ]
    """<p>A description explaining why this time period should be excluded from SLO calculations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExclusionWindow) -> dict:
    out: dict = {}
    import capo_application_signals.types.window

    out["Window"] = capo_application_signals.types.window.serialize_json(
        value["window"]
    )
    if "start_time" in value:
        import capo_application_signals.types._prelude.timestamp

        out["StartTime"] = (
            capo_application_signals.types._prelude.timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "recurrence_rule" in value:
        import capo_application_signals.types.recurrence_rule

        out["RecurrenceRule"] = (
            capo_application_signals.types.recurrence_rule.serialize_json(
                value["recurrence_rule"]
            )
        )
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ExclusionWindow:
    out: ExclusionWindow = {}  # type: ignore[typeddict-item]
    if "Window" in data:
        import capo_application_signals.types.window

        out["window"] = capo_application_signals.types.window.deserialize_json(
            data["Window"]
        )
    else:
        raise DeserializationError("ExclusionWindow.window required")
    if "StartTime" in data:
        import capo_application_signals.types._prelude.timestamp

        out["start_time"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if "RecurrenceRule" in data:
        import capo_application_signals.types.recurrence_rule

        out["recurrence_rule"] = (
            capo_application_signals.types.recurrence_rule.deserialize_json(
                data["RecurrenceRule"]
            )
        )
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
