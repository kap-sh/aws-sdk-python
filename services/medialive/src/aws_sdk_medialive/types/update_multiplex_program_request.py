"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateMultiplexProgramRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.multiplex_program_settings


class UpdateMultiplexProgramRequest(TypedDict, closed=True):
    multiplex_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the multiplex of the program to update."""
    multiplex_program_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_program_settings.MultiplexProgramSettings"
    ]
    """The new settings for a multiplex program."""
    program_name: "aws_sdk_medialive.types.__string.__string"
    """The name of the program to update."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMultiplexProgramRequest) -> dict:
    out: dict = {}
    if "multiplex_program_settings" in value:
        import aws_sdk_medialive.types.multiplex_program_settings

        out["multiplexProgramSettings"] = (
            aws_sdk_medialive.types.multiplex_program_settings.serialize_json(
                value["multiplex_program_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMultiplexProgramRequest:
    out: UpdateMultiplexProgramRequest = {}  # type: ignore[typeddict-item]
    if "multiplexProgramSettings" in data:
        import aws_sdk_medialive.types.multiplex_program_settings

        out["multiplex_program_settings"] = (
            aws_sdk_medialive.types.multiplex_program_settings.deserialize_json(
                data["multiplexProgramSettings"]
            )
        )
    return out
