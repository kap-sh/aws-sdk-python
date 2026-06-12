"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexOutputSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multiplex_container_settings
    import aws_sdk_medialive.types.output_location_ref


class MultiplexOutputSettings(TypedDict):
    destination: NotRequired[
        "aws_sdk_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """Destination is a Multiplex."""
    container_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_container_settings.MultiplexContainerSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexOutputSettings) -> dict:
    out: dict = {}
    if "destination" in value:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = aws_sdk_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "container_settings" in value:
        import aws_sdk_medialive.types.multiplex_container_settings

        out["containerSettings"] = (
            aws_sdk_medialive.types.multiplex_container_settings.serialize_json(
                value["container_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiplexOutputSettings:
    out: MultiplexOutputSettings = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = (
            aws_sdk_medialive.types.output_location_ref.deserialize_json(
                data["destination"]
            )
        )
    if "containerSettings" in data:
        import aws_sdk_medialive.types.multiplex_container_settings

        out["container_settings"] = (
            aws_sdk_medialive.types.multiplex_container_settings.deserialize_json(
                data["containerSettings"]
            )
        )
    return out
