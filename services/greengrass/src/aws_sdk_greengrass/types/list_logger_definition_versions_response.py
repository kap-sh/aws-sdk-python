"""Generated from Smithy shape ``com.amazonaws.greengrass#ListLoggerDefinitionVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_version_information
    import aws_sdk_greengrass.types.__string


class ListLoggerDefinitionVersionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""
    versions: NotRequired[
        "aws_sdk_greengrass.types.__list_of_version_information.__listOfVersionInformation"
    ]
    """Information about a version."""


# --- restJson1 ser/de ---
def serialize_json(value: ListLoggerDefinitionVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "versions" in value:
        import aws_sdk_greengrass.types.__list_of_version_information

        out["Versions"] = (
            aws_sdk_greengrass.types.__list_of_version_information.serialize_json(
                value["versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListLoggerDefinitionVersionsResponse:
    out: ListLoggerDefinitionVersionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Versions" in data:
        import aws_sdk_greengrass.types.__list_of_version_information

        out["versions"] = (
            aws_sdk_greengrass.types.__list_of_version_information.deserialize_json(
                data["Versions"]
            )
        )
    return out
