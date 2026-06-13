"""Generated from Smithy shape ``com.amazonaws.mwaa#ListEnvironmentsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.next_token


class ListEnvironmentsInput(TypedDict):
    next_token: NotRequired["aws_sdk_mwaa.types.next_token.NextToken"]
    """<p>Retrieves the next page of the results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve per page. For example, <code>5</code> environments per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnvironmentsInput:
    out: ListEnvironmentsInput = {}  # type: ignore[typeddict-item]
    return out
