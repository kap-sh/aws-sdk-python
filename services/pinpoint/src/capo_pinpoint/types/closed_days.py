"""Generated from Smithy shape ``com.amazonaws.pinpoint#ClosedDays``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.list_of_closed_days_rules


class ClosedDays(TypedDict, closed=True):
    email: NotRequired[
        "capo_pinpoint.types.list_of_closed_days_rules.ListOfClosedDaysRules"
    ]
    """<p>Rules for the Email channel.</p>"""
    sms: NotRequired[
        "capo_pinpoint.types.list_of_closed_days_rules.ListOfClosedDaysRules"
    ]
    """<p>Rules for the SMS channel.</p>"""
    push: NotRequired[
        "capo_pinpoint.types.list_of_closed_days_rules.ListOfClosedDaysRules"
    ]
    """<p>Rules for the Push channel.</p>"""
    voice: NotRequired[
        "capo_pinpoint.types.list_of_closed_days_rules.ListOfClosedDaysRules"
    ]
    """<p>Rules for the Voice channel.</p>"""
    custom: NotRequired[
        "capo_pinpoint.types.list_of_closed_days_rules.ListOfClosedDaysRules"
    ]
    """<p>Rules for the Custom channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClosedDays) -> dict:
    out: dict = {}
    if "email" in value:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["EMAIL"] = capo_pinpoint.types.list_of_closed_days_rules.serialize_json(
            value["email"]
        )
    if "sms" in value:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["SMS"] = capo_pinpoint.types.list_of_closed_days_rules.serialize_json(
            value["sms"]
        )
    if "push" in value:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["PUSH"] = capo_pinpoint.types.list_of_closed_days_rules.serialize_json(
            value["push"]
        )
    if "voice" in value:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["VOICE"] = capo_pinpoint.types.list_of_closed_days_rules.serialize_json(
            value["voice"]
        )
    if "custom" in value:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["CUSTOM"] = capo_pinpoint.types.list_of_closed_days_rules.serialize_json(
            value["custom"]
        )
    return out


def deserialize_json(data: dict) -> ClosedDays:
    out: ClosedDays = {}  # type: ignore[typeddict-item]
    if "EMAIL" in data:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["email"] = capo_pinpoint.types.list_of_closed_days_rules.deserialize_json(
            data["EMAIL"]
        )
    if "SMS" in data:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["sms"] = capo_pinpoint.types.list_of_closed_days_rules.deserialize_json(
            data["SMS"]
        )
    if "PUSH" in data:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["push"] = capo_pinpoint.types.list_of_closed_days_rules.deserialize_json(
            data["PUSH"]
        )
    if "VOICE" in data:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["voice"] = capo_pinpoint.types.list_of_closed_days_rules.deserialize_json(
            data["VOICE"]
        )
    if "CUSTOM" in data:
        import capo_pinpoint.types.list_of_closed_days_rules

        out["custom"] = capo_pinpoint.types.list_of_closed_days_rules.deserialize_json(
            data["CUSTOM"]
        )
    return out
