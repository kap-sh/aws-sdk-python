"""Generated from Smithy shape ``com.amazonaws.medialive#ArchiveContainerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.m2ts_settings
    import aws_sdk_medialive.types.raw_settings


class ArchiveContainerSettings(TypedDict, closed=True):
    m2ts_settings: NotRequired["aws_sdk_medialive.types.m2ts_settings.M2tsSettings"]
    raw_settings: NotRequired["aws_sdk_medialive.types.raw_settings.RawSettings"]


# --- restJson1 ser/de ---
def serialize_json(value: ArchiveContainerSettings) -> dict:
    out: dict = {}
    if "m2ts_settings" in value:
        import aws_sdk_medialive.types.m2ts_settings

        out["m2tsSettings"] = aws_sdk_medialive.types.m2ts_settings.serialize_json(
            value["m2ts_settings"]
        )
    if "raw_settings" in value:
        import aws_sdk_medialive.types.raw_settings

        out["rawSettings"] = aws_sdk_medialive.types.raw_settings.serialize_json(
            value["raw_settings"]
        )
    return out


def deserialize_json(data: dict) -> ArchiveContainerSettings:
    out: ArchiveContainerSettings = {}  # type: ignore[typeddict-item]
    if "m2tsSettings" in data:
        import aws_sdk_medialive.types.m2ts_settings

        out["m2ts_settings"] = aws_sdk_medialive.types.m2ts_settings.deserialize_json(
            data["m2tsSettings"]
        )
    if "rawSettings" in data:
        import aws_sdk_medialive.types.raw_settings

        out["raw_settings"] = aws_sdk_medialive.types.raw_settings.deserialize_json(
            data["rawSettings"]
        )
    return out
