"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#ListSimulationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.optional_string
    import aws_sdk_simspaceweaver.types.positive_integer


class ListSimulationsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_simspaceweaver.types.positive_integer.PositiveInteger"
    ]
    """<p>The maximum number of simulations to list.</p>"""
    next_token: NotRequired[
        "aws_sdk_simspaceweaver.types.optional_string.OptionalString"
    ]
    """<p>If SimSpace Weaver returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an <i>HTTP 400 ValidationException</i> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSimulationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSimulationsInput:
    out: ListSimulationsInput = {}  # type: ignore[typeddict-item]
    return out
