"""Generated from Smithy shape ``com.amazonaws.xray#ErrorRootCauseServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.error_root_cause_service

ErrorRootCauseServices: TypeAlias = list[
    "capo_xray.types.error_root_cause_service.ErrorRootCauseService"
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorRootCauseServices) -> list:
    import capo_xray.types.error_root_cause_service

    out: list = []
    for item in value:
        out.append(capo_xray.types.error_root_cause_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> ErrorRootCauseServices:
    import capo_xray.types.error_root_cause_service

    out: ErrorRootCauseServices = []
    for item in data:
        out.append(capo_xray.types.error_root_cause_service.deserialize_json(item))
    return out
