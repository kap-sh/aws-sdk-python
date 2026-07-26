"""Generated from Smithy shape ``com.amazonaws.securityhub#IndicatorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.indicator

IndicatorsList: TypeAlias = list["capo_securityhub.types.indicator.Indicator"]


# --- restJson1 ser/de ---
def serialize_json(value: IndicatorsList) -> list:
    import capo_securityhub.types.indicator

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.indicator.serialize_json(item))
    return out


def deserialize_json(data: list) -> IndicatorsList:
    import capo_securityhub.types.indicator

    out: IndicatorsList = []
    for item in data:
        out.append(capo_securityhub.types.indicator.deserialize_json(item))
    return out
