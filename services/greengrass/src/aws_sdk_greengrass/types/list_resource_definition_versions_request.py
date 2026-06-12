"""Generated from Smithy shape ``com.amazonaws.greengrass#ListResourceDefinitionVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class ListResourceDefinitionVersionsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The maximum number of results to be returned per request."""
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""
    resource_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the resource definition."""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceDefinitionVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListResourceDefinitionVersionsRequest:
    out: ListResourceDefinitionVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
