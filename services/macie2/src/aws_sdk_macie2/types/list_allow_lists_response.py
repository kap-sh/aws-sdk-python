"""Generated from Smithy shape ``com.amazonaws.macie2#ListAllowListsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_allow_list_summary
    import aws_sdk_macie2.types.__string


class ListAllowListsResponse(TypedDict, closed=True):
    allow_lists: NotRequired[
        "aws_sdk_macie2.types.__list_of_allow_list_summary.__listOfAllowListSummary"
    ]
    """<p>An array of objects, one for each allow list.</p>"""
    next_token: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAllowListsResponse) -> dict:
    out: dict = {}
    if "allow_lists" in value:
        import aws_sdk_macie2.types.__list_of_allow_list_summary

        out["allowLists"] = (
            aws_sdk_macie2.types.__list_of_allow_list_summary.serialize_json(
                value["allow_lists"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAllowListsResponse:
    out: ListAllowListsResponse = {}  # type: ignore[typeddict-item]
    if "allowLists" in data:
        import aws_sdk_macie2.types.__list_of_allow_list_summary

        out["allow_lists"] = (
            aws_sdk_macie2.types.__list_of_allow_list_summary.deserialize_json(
                data["allowLists"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
