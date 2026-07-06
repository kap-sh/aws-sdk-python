"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListMatchingWorkflowsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.next_token


class ListMatchingWorkflowsInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of objects returned per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMatchingWorkflowsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMatchingWorkflowsInput:
    out: ListMatchingWorkflowsInput = {}  # type: ignore[typeddict-item]
    return out
