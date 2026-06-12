"""Generated from Smithy shape ``com.amazonaws.iot#OTAUpdateFiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.ota_update_file

OTAUpdateFiles: TypeAlias = list["aws_sdk_iot.types.ota_update_file.OTAUpdateFile"]


# --- restJson1 ser/de ---
def serialize_json(value: OTAUpdateFiles) -> list:
    import aws_sdk_iot.types.ota_update_file

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.ota_update_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> OTAUpdateFiles:
    import aws_sdk_iot.types.ota_update_file

    out: OTAUpdateFiles = []
    for item in data:
        out.append(aws_sdk_iot.types.ota_update_file.deserialize_json(item))
    return out
