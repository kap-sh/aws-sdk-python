"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.simple_rule


class AlarmRule(TypedDict, closed=True):
    simple_rule: NotRequired["capo_iot_events.types.simple_rule.SimpleRule"]
    """<p>A rule that compares an input property value to a threshold value with a comparison operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmRule) -> dict:
    out: dict = {}
    if "simple_rule" in value:
        import capo_iot_events.types.simple_rule

        out["simpleRule"] = capo_iot_events.types.simple_rule.serialize_json(
            value["simple_rule"]
        )
    return out


def deserialize_json(data: dict) -> AlarmRule:
    out: AlarmRule = {}  # type: ignore[typeddict-item]
    if "simpleRule" in data:
        import capo_iot_events.types.simple_rule

        out["simple_rule"] = capo_iot_events.types.simple_rule.deserialize_json(
            data["simpleRule"]
        )
    return out
