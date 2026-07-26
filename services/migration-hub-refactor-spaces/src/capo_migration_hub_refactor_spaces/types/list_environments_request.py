"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.max_results
    import capo_migration_hub_refactor_spaces.types.next_token


class ListEnvironmentsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired[
        "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnvironmentsRequest:
    out: ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    return out
