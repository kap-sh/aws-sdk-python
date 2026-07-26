"""Generated from Smithy shape ``com.amazonaws.medialive#CreateMultiplexProgramRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.multiplex_program_settings


class CreateMultiplexProgramRequest(TypedDict, closed=True):
    multiplex_id: "capo_medialive.types.__string.__string"
    """ID of the multiplex where the program is to be created."""
    multiplex_program_settings: NotRequired[
        "capo_medialive.types.multiplex_program_settings.MultiplexProgramSettings"
    ]
    """The settings for this multiplex program."""
    program_name: NotRequired["capo_medialive.types.__string.__string"]
    """Name of multiplex program."""
    request_id: NotRequired["capo_medialive.types.__string.__string"]
    """Unique request ID. This prevents retries from creating multiple resources."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultiplexProgramRequest) -> dict:
    out: dict = {}
    if "multiplex_program_settings" in value:
        import capo_medialive.types.multiplex_program_settings

        out["multiplexProgramSettings"] = (
            capo_medialive.types.multiplex_program_settings.serialize_json(
                value["multiplex_program_settings"]
            )
        )
    if "program_name" in value:
        out["programName"] = value["program_name"]
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateMultiplexProgramRequest:
    out: CreateMultiplexProgramRequest = {}  # type: ignore[typeddict-item]
    if "multiplexProgramSettings" in data:
        import capo_medialive.types.multiplex_program_settings

        out["multiplex_program_settings"] = (
            capo_medialive.types.multiplex_program_settings.deserialize_json(
                data["multiplexProgramSettings"]
            )
        )
    if "programName" in data:
        out["program_name"] = data["programName"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    return out
