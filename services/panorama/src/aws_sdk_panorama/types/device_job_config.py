"""Generated from Smithy shape ``com.amazonaws.panorama#DeviceJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.ota_job_config


class DeviceJobConfig(TypedDict, closed=True):
    ota_job_config: NotRequired["aws_sdk_panorama.types.ota_job_config.OTAJobConfig"]
    """<p>A configuration for an over-the-air (OTA) upgrade. Required for OTA jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceJobConfig) -> dict:
    out: dict = {}
    if "ota_job_config" in value:
        import aws_sdk_panorama.types.ota_job_config

        out["OTAJobConfig"] = aws_sdk_panorama.types.ota_job_config.serialize_json(
            value["ota_job_config"]
        )
    return out


def deserialize_json(data: dict) -> DeviceJobConfig:
    out: DeviceJobConfig = {}  # type: ignore[typeddict-item]
    if "OTAJobConfig" in data:
        import aws_sdk_panorama.types.ota_job_config

        out["ota_job_config"] = aws_sdk_panorama.types.ota_job_config.deserialize_json(
            data["OTAJobConfig"]
        )
    return out
