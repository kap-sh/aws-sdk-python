"""Generated from Smithy shape ``com.amazonaws.finspace#KxCommandLineArguments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_command_line_argument

KxCommandLineArguments: TypeAlias = list[
    "capo_finspace.types.kx_command_line_argument.KxCommandLineArgument"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxCommandLineArguments) -> list:
    import capo_finspace.types.kx_command_line_argument

    out: list = []
    for item in value:
        out.append(capo_finspace.types.kx_command_line_argument.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxCommandLineArguments:
    import capo_finspace.types.kx_command_line_argument

    out: KxCommandLineArguments = []
    for item in data:
        out.append(capo_finspace.types.kx_command_line_argument.deserialize_json(item))
    return out
