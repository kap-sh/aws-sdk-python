"""Generated from Smithy shape ``com.amazonaws.greengrass#ListResourceDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_definition_information
    import aws_sdk_greengrass.types.__string


class ListResourceDefinitionsResponse(TypedDict):
    definitions: NotRequired[
        "aws_sdk_greengrass.types.__list_of_definition_information.__listOfDefinitionInformation"
    ]
    """Information about a definition."""
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceDefinitionsResponse) -> dict:
    out: dict = {}
    if "definitions" in value:
        import aws_sdk_greengrass.types.__list_of_definition_information

        out["Definitions"] = (
            aws_sdk_greengrass.types.__list_of_definition_information.serialize_json(
                value["definitions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceDefinitionsResponse:
    out: ListResourceDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "Definitions" in data:
        import aws_sdk_greengrass.types.__list_of_definition_information

        out["definitions"] = (
            aws_sdk_greengrass.types.__list_of_definition_information.deserialize_json(
                data["Definitions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
