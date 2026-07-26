"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexContainerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.multiplex_m2ts_settings


class MultiplexContainerSettings(TypedDict, closed=True):
    multiplex_m2ts_settings: NotRequired[
        "capo_medialive.types.multiplex_m2ts_settings.MultiplexM2tsSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexContainerSettings) -> dict:
    out: dict = {}
    if "multiplex_m2ts_settings" in value:
        import capo_medialive.types.multiplex_m2ts_settings

        out["multiplexM2tsSettings"] = (
            capo_medialive.types.multiplex_m2ts_settings.serialize_json(
                value["multiplex_m2ts_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiplexContainerSettings:
    out: MultiplexContainerSettings = {}  # type: ignore[typeddict-item]
    if "multiplexM2tsSettings" in data:
        import capo_medialive.types.multiplex_m2ts_settings

        out["multiplex_m2ts_settings"] = (
            capo_medialive.types.multiplex_m2ts_settings.deserialize_json(
                data["multiplexM2tsSettings"]
            )
        )
    return out
