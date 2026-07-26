"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.multiplex_container_settings
    import capo_medialive.types.output_location_ref


class MultiplexOutputSettings(TypedDict, closed=True):
    destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """Destination is a Multiplex."""
    container_settings: NotRequired[
        "capo_medialive.types.multiplex_container_settings.MultiplexContainerSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexOutputSettings) -> dict:
    out: dict = {}
    if "destination" in value:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "container_settings" in value:
        import capo_medialive.types.multiplex_container_settings

        out["containerSettings"] = (
            capo_medialive.types.multiplex_container_settings.serialize_json(
                value["container_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiplexOutputSettings:
    out: MultiplexOutputSettings = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.deserialize_json(
            data["destination"]
        )
    if "containerSettings" in data:
        import capo_medialive.types.multiplex_container_settings

        out["container_settings"] = (
            capo_medialive.types.multiplex_container_settings.deserialize_json(
                data["containerSettings"]
            )
        )
    return out
