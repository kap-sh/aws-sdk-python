"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateMultiplexProgramResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multiplex_program


class UpdateMultiplexProgramResponse(TypedDict, closed=True):
    multiplex_program: NotRequired[
        "aws_sdk_medialive.types.multiplex_program.MultiplexProgram"
    ]
    """The updated multiplex program."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMultiplexProgramResponse) -> dict:
    out: dict = {}
    if "multiplex_program" in value:
        import aws_sdk_medialive.types.multiplex_program

        out["multiplexProgram"] = (
            aws_sdk_medialive.types.multiplex_program.serialize_json(
                value["multiplex_program"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMultiplexProgramResponse:
    out: UpdateMultiplexProgramResponse = {}  # type: ignore[typeddict-item]
    if "multiplexProgram" in data:
        import aws_sdk_medialive.types.multiplex_program

        out["multiplex_program"] = (
            aws_sdk_medialive.types.multiplex_program.deserialize_json(
                data["multiplexProgram"]
            )
        )
    return out
