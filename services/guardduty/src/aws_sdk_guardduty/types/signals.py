"""Generated from Smithy shape ``com.amazonaws.guardduty#Signals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.signal

Signals: TypeAlias = list["aws_sdk_guardduty.types.signal.Signal"]


# --- restJson1 ser/de ---
def serialize_json(value: Signals) -> list:
    import aws_sdk_guardduty.types.signal

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.signal.serialize_json(item))
    return out


def deserialize_json(data: list) -> Signals:
    import aws_sdk_guardduty.types.signal

    out: Signals = []
    for item in data:
        out.append(aws_sdk_guardduty.types.signal.deserialize_json(item))
    return out
