"""Generated from Smithy shape ``com.amazonaws.iot#OTAUpdateFiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.ota_update_file

OTAUpdateFiles: TypeAlias = list["capo_iot.types.ota_update_file.OTAUpdateFile"]


# --- restJson1 ser/de ---
def serialize_json(value: OTAUpdateFiles) -> list:
    import capo_iot.types.ota_update_file

    out: list = []
    for item in value:
        out.append(capo_iot.types.ota_update_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> OTAUpdateFiles:
    import capo_iot.types.ota_update_file

    out: OTAUpdateFiles = []
    for item in data:
        out.append(capo_iot.types.ota_update_file.deserialize_json(item))
    return out
