"""Generated from Smithy shape ``com.amazonaws.securityhub#IndicatorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.indicator

IndicatorsList: TypeAlias = list["aws_sdk_securityhub.types.indicator.Indicator"]


# --- restJson1 ser/de ---
def serialize_json(value: IndicatorsList) -> list:
    import aws_sdk_securityhub.types.indicator

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.indicator.serialize_json(item))
    return out


def deserialize_json(data: list) -> IndicatorsList:
    import aws_sdk_securityhub.types.indicator

    out: IndicatorsList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.indicator.deserialize_json(item))
    return out
