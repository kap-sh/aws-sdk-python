"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#ListPluginsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.max_results
    import aws_sdk_migrationhuborchestrator.types.next_token


class ListPluginsRequest(TypedDict):
    max_results: "aws_sdk_migrationhuborchestrator.types.max_results.MaxResults"
    """<p>The maximum number of plugins that can be returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_migrationhuborchestrator.types.next_token.NextToken"
    ]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPluginsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPluginsRequest:
    out: ListPluginsRequest = {}  # type: ignore[typeddict-item]
    return out
