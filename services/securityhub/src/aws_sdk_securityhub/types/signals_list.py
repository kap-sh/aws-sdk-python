"""Generated from Smithy shape ``com.amazonaws.securityhub#SignalsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.signal

SignalsList: TypeAlias = list["aws_sdk_securityhub.types.signal.Signal"]


# --- restJson1 ser/de ---
def serialize_json(value: SignalsList) -> list:
    import aws_sdk_securityhub.types.signal

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.signal.serialize_json(item))
    return out


def deserialize_json(data: list) -> SignalsList:
    import aws_sdk_securityhub.types.signal

    out: SignalsList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.signal.deserialize_json(item))
    return out
