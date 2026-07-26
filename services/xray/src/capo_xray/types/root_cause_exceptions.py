"""Generated from Smithy shape ``com.amazonaws.xray#RootCauseExceptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.root_cause_exception

RootCauseExceptions: TypeAlias = list[
    "capo_xray.types.root_cause_exception.RootCauseException"
]


# --- restJson1 ser/de ---
def serialize_json(value: RootCauseExceptions) -> list:
    import capo_xray.types.root_cause_exception

    out: list = []
    for item in value:
        out.append(capo_xray.types.root_cause_exception.serialize_json(item))
    return out


def deserialize_json(data: list) -> RootCauseExceptions:
    import capo_xray.types.root_cause_exception

    out: RootCauseExceptions = []
    for item in data:
        out.append(capo_xray.types.root_cause_exception.deserialize_json(item))
    return out
