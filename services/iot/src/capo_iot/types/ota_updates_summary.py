"""Generated from Smithy shape ``com.amazonaws.iot#OTAUpdatesSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.ota_update_summary

OTAUpdatesSummary: TypeAlias = list[
    "capo_iot.types.ota_update_summary.OTAUpdateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OTAUpdatesSummary) -> list:
    import capo_iot.types.ota_update_summary

    out: list = []
    for item in value:
        out.append(capo_iot.types.ota_update_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> OTAUpdatesSummary:
    import capo_iot.types.ota_update_summary

    out: OTAUpdatesSummary = []
    for item in data:
        out.append(capo_iot.types.ota_update_summary.deserialize_json(item))
    return out
