"""Generated from Smithy shape ``com.amazonaws.xray#ResponseTimeRootCauseServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.response_time_root_cause_service

ResponseTimeRootCauseServices: TypeAlias = list[
    "capo_xray.types.response_time_root_cause_service.ResponseTimeRootCauseService"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseTimeRootCauseServices) -> list:
    import capo_xray.types.response_time_root_cause_service

    out: list = []
    for item in value:
        out.append(
            capo_xray.types.response_time_root_cause_service.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResponseTimeRootCauseServices:
    import capo_xray.types.response_time_root_cause_service

    out: ResponseTimeRootCauseServices = []
    for item in data:
        out.append(
            capo_xray.types.response_time_root_cause_service.deserialize_json(item)
        )
    return out
