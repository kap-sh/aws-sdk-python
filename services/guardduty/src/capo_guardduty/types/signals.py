"""Generated from Smithy shape ``com.amazonaws.guardduty#Signals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.signal

Signals: TypeAlias = list["capo_guardduty.types.signal.Signal"]


# --- restJson1 ser/de ---
def serialize_json(value: Signals) -> list:
    import capo_guardduty.types.signal

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.signal.serialize_json(item))
    return out


def deserialize_json(data: list) -> Signals:
    import capo_guardduty.types.signal

    out: Signals = []
    for item in data:
        out.append(capo_guardduty.types.signal.deserialize_json(item))
    return out
