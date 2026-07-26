"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InvalidSignals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.invalid_signal

InvalidSignals: TypeAlias = list["capo_iotfleetwise.types.invalid_signal.InvalidSignal"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidSignals) -> list:
    import capo_iotfleetwise.types.invalid_signal

    out: list = []
    for item in value:
        out.append(capo_iotfleetwise.types.invalid_signal.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> InvalidSignals:
    import capo_iotfleetwise.types.invalid_signal

    out: InvalidSignals = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.invalid_signal.deserialize_aws_json_1_0(item)
        )
    return out
