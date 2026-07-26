"""Generated from Smithy shape ``com.amazonaws.xray#TraceUsers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.trace_user

TraceUsers: TypeAlias = list["capo_xray.types.trace_user.TraceUser"]


# --- restJson1 ser/de ---
def serialize_json(value: TraceUsers) -> list:
    import capo_xray.types.trace_user

    out: list = []
    for item in value:
        out.append(capo_xray.types.trace_user.serialize_json(item))
    return out


def deserialize_json(data: list) -> TraceUsers:
    import capo_xray.types.trace_user

    out: TraceUsers = []
    for item in data:
        out.append(capo_xray.types.trace_user.deserialize_json(item))
    return out
