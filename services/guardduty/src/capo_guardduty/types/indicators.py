"""Generated from Smithy shape ``com.amazonaws.guardduty#Indicators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.indicator

Indicators: TypeAlias = list["capo_guardduty.types.indicator.Indicator"]


# --- restJson1 ser/de ---
def serialize_json(value: Indicators) -> list:
    import capo_guardduty.types.indicator

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.indicator.serialize_json(item))
    return out


def deserialize_json(data: list) -> Indicators:
    import capo_guardduty.types.indicator

    out: Indicators = []
    for item in data:
        out.append(capo_guardduty.types.indicator.deserialize_json(item))
    return out
