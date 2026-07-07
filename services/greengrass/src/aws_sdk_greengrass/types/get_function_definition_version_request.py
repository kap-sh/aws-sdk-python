"""Generated from Smithy shape ``com.amazonaws.greengrass#GetFunctionDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetFunctionDefinitionVersionRequest(TypedDict, closed=True):
    function_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Lambda function definition."""
    function_definition_version_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the function definition version. This value maps to the ''Version'' property of the corresponding ''VersionInformation'' object, which is returned by ''ListFunctionDefinitionVersions'' requests. If the version is the last one that was associated with a function definition, the value also maps to the ''LatestVersion'' property of the corresponding ''DefinitionInformation'' object."""
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionDefinitionVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFunctionDefinitionVersionRequest:
    out: GetFunctionDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    return out
