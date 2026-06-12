"""Generated from Smithy shape ``com.amazonaws.finspace#KxCommandLineArguments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_command_line_argument

KxCommandLineArguments: TypeAlias = list[
    "aws_sdk_finspace.types.kx_command_line_argument.KxCommandLineArgument"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxCommandLineArguments) -> list:
    import aws_sdk_finspace.types.kx_command_line_argument

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace.types.kx_command_line_argument.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxCommandLineArguments:
    import aws_sdk_finspace.types.kx_command_line_argument

    out: KxCommandLineArguments = []
    for item in data:
        out.append(
            aws_sdk_finspace.types.kx_command_line_argument.deserialize_json(item)
        )
    return out
