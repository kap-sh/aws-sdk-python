"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListSourceLocationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_source_location
    import aws_sdk_mediatailor.types.__string


class ListSourceLocationsResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_mediatailor.types.__list_of_source_location.__listOfSourceLocation"
    ]
    """<p>A list of source locations.</p>"""
    next_token: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceLocationsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mediatailor.types.__list_of_source_location

        out["Items"] = (
            aws_sdk_mediatailor.types.__list_of_source_location.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSourceLocationsResponse:
    out: ListSourceLocationsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_mediatailor.types.__list_of_source_location

        out["items"] = (
            aws_sdk_mediatailor.types.__list_of_source_location.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
