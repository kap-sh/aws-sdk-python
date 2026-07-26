"""Generated from Smithy shape ``com.amazonaws.xray#ResponseTimeRootCauseEntityPath``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.response_time_root_cause_entity

ResponseTimeRootCauseEntityPath: TypeAlias = list[
    "capo_xray.types.response_time_root_cause_entity.ResponseTimeRootCauseEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTimeRootCauseEntityPath) -> list:
    import capo_xray.types.response_time_root_cause_entity

    out: list = []
    for item in value:
        out.append(capo_xray.types.response_time_root_cause_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResponseTimeRootCauseEntityPath:
    import capo_xray.types.response_time_root_cause_entity

    out: ResponseTimeRootCauseEntityPath = []
    for item in data:
        out.append(
            capo_xray.types.response_time_root_cause_entity.deserialize_json(item)
        )
    return out
