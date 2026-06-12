"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMultiplexProgramSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multiplex_program_summary

__listOfMultiplexProgramSummary: TypeAlias = list[
    "aws_sdk_medialive.types.multiplex_program_summary.MultiplexProgramSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMultiplexProgramSummary) -> list:
    import aws_sdk_medialive.types.multiplex_program_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.multiplex_program_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfMultiplexProgramSummary:
    import aws_sdk_medialive.types.multiplex_program_summary

    out: __listOfMultiplexProgramSummary = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.multiplex_program_summary.deserialize_json(item)
        )
    return out
