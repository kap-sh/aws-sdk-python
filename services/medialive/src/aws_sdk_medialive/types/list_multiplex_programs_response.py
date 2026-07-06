"""Generated from Smithy shape ``com.amazonaws.medialive#ListMultiplexProgramsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_multiplex_program_summary
    import aws_sdk_medialive.types.__string


class ListMultiplexProgramsResponse(TypedDict, closed=True):
    multiplex_programs: NotRequired[
        "aws_sdk_medialive.types.__list_of_multiplex_program_summary.__listOfMultiplexProgramSummary"
    ]
    """List of multiplex programs."""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Token for the next ListMultiplexProgram request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultiplexProgramsResponse) -> dict:
    out: dict = {}
    if "multiplex_programs" in value:
        import aws_sdk_medialive.types.__list_of_multiplex_program_summary

        out["multiplexPrograms"] = (
            aws_sdk_medialive.types.__list_of_multiplex_program_summary.serialize_json(
                value["multiplex_programs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMultiplexProgramsResponse:
    out: ListMultiplexProgramsResponse = {}  # type: ignore[typeddict-item]
    if "multiplexPrograms" in data:
        import aws_sdk_medialive.types.__list_of_multiplex_program_summary

        out["multiplex_programs"] = (
            aws_sdk_medialive.types.__list_of_multiplex_program_summary.deserialize_json(
                data["multiplexPrograms"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
