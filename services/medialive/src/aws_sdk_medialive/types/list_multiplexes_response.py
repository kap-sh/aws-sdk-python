"""Generated from Smithy shape ``com.amazonaws.medialive#ListMultiplexesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_multiplex_summary
    import aws_sdk_medialive.types.__string


class ListMultiplexesResponse(TypedDict, closed=True):
    multiplexes: NotRequired[
        "aws_sdk_medialive.types.__list_of_multiplex_summary.__listOfMultiplexSummary"
    ]
    """List of multiplexes."""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Token for the next ListMultiplexes request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultiplexesResponse) -> dict:
    out: dict = {}
    if "multiplexes" in value:
        import aws_sdk_medialive.types.__list_of_multiplex_summary

        out["multiplexes"] = (
            aws_sdk_medialive.types.__list_of_multiplex_summary.serialize_json(
                value["multiplexes"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMultiplexesResponse:
    out: ListMultiplexesResponse = {}  # type: ignore[typeddict-item]
    if "multiplexes" in data:
        import aws_sdk_medialive.types.__list_of_multiplex_summary

        out["multiplexes"] = (
            aws_sdk_medialive.types.__list_of_multiplex_summary.deserialize_json(
                data["multiplexes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
