"""Generated from Smithy shape ``com.amazonaws.greengrass#ListFunctionDefinitionVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class ListFunctionDefinitionVersionsRequest(TypedDict, closed=True):
    function_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Lambda function definition."""
    max_results: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The maximum number of results to be returned per request."""
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionDefinitionVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionDefinitionVersionsRequest:
    out: ListFunctionDefinitionVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
