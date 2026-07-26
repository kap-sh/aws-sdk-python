"""Generated from Smithy shape ``com.amazonaws.medialive#UdpContainerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.m2ts_settings


class UdpContainerSettings(TypedDict, closed=True):
    m2ts_settings: NotRequired["capo_medialive.types.m2ts_settings.M2tsSettings"]


# --- restJson1 ser/de ---
def serialize_json(value: UdpContainerSettings) -> dict:
    out: dict = {}
    if "m2ts_settings" in value:
        import capo_medialive.types.m2ts_settings

        out["m2tsSettings"] = capo_medialive.types.m2ts_settings.serialize_json(
            value["m2ts_settings"]
        )
    return out


def deserialize_json(data: dict) -> UdpContainerSettings:
    out: UdpContainerSettings = {}  # type: ignore[typeddict-item]
    if "m2tsSettings" in data:
        import capo_medialive.types.m2ts_settings

        out["m2ts_settings"] = capo_medialive.types.m2ts_settings.deserialize_json(
            data["m2tsSettings"]
        )
    return out
