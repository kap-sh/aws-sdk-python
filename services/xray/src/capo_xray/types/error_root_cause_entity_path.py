"""Generated from Smithy shape ``com.amazonaws.xray#ErrorRootCauseEntityPath``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.error_root_cause_entity

ErrorRootCauseEntityPath: TypeAlias = list[
    "capo_xray.types.error_root_cause_entity.ErrorRootCauseEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorRootCauseEntityPath) -> list:
    import capo_xray.types.error_root_cause_entity

    out: list = []
    for item in value:
        out.append(capo_xray.types.error_root_cause_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> ErrorRootCauseEntityPath:
    import capo_xray.types.error_root_cause_entity

    out: ErrorRootCauseEntityPath = []
    for item in data:
        out.append(capo_xray.types.error_root_cause_entity.deserialize_json(item))
    return out
