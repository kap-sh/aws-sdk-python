"""Generated from Smithy shape ``com.amazonaws.medialive#CreateMultiplexProgramResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multiplex_program


class CreateMultiplexProgramResponse(TypedDict):
    multiplex_program: NotRequired[
        "aws_sdk_medialive.types.multiplex_program.MultiplexProgram"
    ]
    """The newly created multiplex program."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMultiplexProgramResponse) -> dict:
    out: dict = {}
    if "multiplex_program" in value:
        import aws_sdk_medialive.types.multiplex_program

        out["multiplexProgram"] = (
            aws_sdk_medialive.types.multiplex_program.serialize_json(
                value["multiplex_program"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMultiplexProgramResponse:
    out: CreateMultiplexProgramResponse = {}  # type: ignore[typeddict-item]
    if "multiplexProgram" in data:
        import aws_sdk_medialive.types.multiplex_program

        out["multiplex_program"] = (
            aws_sdk_medialive.types.multiplex_program.deserialize_json(
                data["multiplexProgram"]
            )
        )
    return out
