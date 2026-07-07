"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_tnb.types.pagination_token


class ListSolFunctionInstancesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to include in the response.</p>"""
    next_token: NotRequired["aws_sdk_tnb.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionInstancesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSolFunctionInstancesInput:
    out: ListSolFunctionInstancesInput = {}  # type: ignore[typeddict-item]
    return out
