"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListIdMappingWorkflowsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.next_token


class ListIdMappingWorkflowsInput(TypedDict):
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of objects returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdMappingWorkflowsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdMappingWorkflowsInput:
    out: ListIdMappingWorkflowsInput = {}  # type: ignore[typeddict-item]
    return out
