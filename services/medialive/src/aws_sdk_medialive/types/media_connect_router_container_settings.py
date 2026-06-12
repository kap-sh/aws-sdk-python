"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectRouterContainerSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.m2ts_settings


class MediaConnectRouterContainerSettings(TypedDict):
    m2ts_settings: NotRequired["aws_sdk_medialive.types.m2ts_settings.M2tsSettings"]


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectRouterContainerSettings) -> dict:
    out: dict = {}
    if "m2ts_settings" in value:
        import aws_sdk_medialive.types.m2ts_settings

        out["m2tsSettings"] = aws_sdk_medialive.types.m2ts_settings.serialize_json(
            value["m2ts_settings"]
        )
    return out


def deserialize_json(data: dict) -> MediaConnectRouterContainerSettings:
    out: MediaConnectRouterContainerSettings = {}  # type: ignore[typeddict-item]
    if "m2tsSettings" in data:
        import aws_sdk_medialive.types.m2ts_settings

        out["m2ts_settings"] = aws_sdk_medialive.types.m2ts_settings.deserialize_json(
            data["m2tsSettings"]
        )
    return out
