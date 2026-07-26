"""Generated from Smithy shape ``com.amazonaws.greengrass#ListGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_group_information
    import capo_greengrass.types.__string


class ListGroupsResponse(TypedDict, closed=True):
    groups: NotRequired[
        "capo_greengrass.types.__list_of_group_information.__listOfGroupInformation"
    ]
    """Information about a group."""
    next_token: NotRequired["capo_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsResponse) -> dict:
    out: dict = {}
    if "groups" in value:
        import capo_greengrass.types.__list_of_group_information

        out["Groups"] = (
            capo_greengrass.types.__list_of_group_information.serialize_json(
                value["groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupsResponse:
    out: ListGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import capo_greengrass.types.__list_of_group_information

        out["groups"] = (
            capo_greengrass.types.__list_of_group_information.deserialize_json(
                data["Groups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
