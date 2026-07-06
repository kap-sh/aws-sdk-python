"""Generated from Smithy shape ``com.amazonaws.mediatailor#GetChannelScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_schedule_entry
    import aws_sdk_mediatailor.types.__string


class GetChannelScheduleResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_schedule_entry.__listOfScheduleEntry"
    ]
    """<p>A list of schedule entries for the channel.</p>"""
    next_token: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelScheduleResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mediatailor.types.__list_of_schedule_entry

        out["Items"] = (
            aws_sdk_mediatailor.types.__list_of_schedule_entry.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetChannelScheduleResponse:
    out: GetChannelScheduleResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_mediatailor.types.__list_of_schedule_entry

        out["items"] = (
            aws_sdk_mediatailor.types.__list_of_schedule_entry.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
