"""Generated from Smithy shape ``com.amazonaws.greengrass#ListConnectorDefinitionVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_version_information
    import capo_greengrass.types.__string


class ListConnectorDefinitionVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""
    versions: NotRequired[
        "capo_greengrass.types.__list_of_version_information.__listOfVersionInformation"
    ]
    """Information about a version."""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorDefinitionVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "versions" in value:
        import capo_greengrass.types.__list_of_version_information

        out["Versions"] = (
            capo_greengrass.types.__list_of_version_information.serialize_json(
                value["versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListConnectorDefinitionVersionsResponse:
    out: ListConnectorDefinitionVersionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Versions" in data:
        import capo_greengrass.types.__list_of_version_information

        out["versions"] = (
            capo_greengrass.types.__list_of_version_information.deserialize_json(
                data["Versions"]
            )
        )
    return out
