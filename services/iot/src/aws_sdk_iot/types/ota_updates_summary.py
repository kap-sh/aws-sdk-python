"""Generated from Smithy shape ``com.amazonaws.iot#OTAUpdatesSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.ota_update_summary

OTAUpdatesSummary: TypeAlias = list[
    "aws_sdk_iot.types.ota_update_summary.OTAUpdateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OTAUpdatesSummary) -> list:
    import aws_sdk_iot.types.ota_update_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.ota_update_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> OTAUpdatesSummary:
    import aws_sdk_iot.types.ota_update_summary

    out: OTAUpdatesSummary = []
    for item in data:
        out.append(aws_sdk_iot.types.ota_update_summary.deserialize_json(item))
    return out
