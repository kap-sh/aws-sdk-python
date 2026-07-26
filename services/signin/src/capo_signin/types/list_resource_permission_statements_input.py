"""Generated from Smithy shape ``com.amazonaws.signin#ListResourcePermissionStatementsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.console_permission_max_results
    import capo_signin.types.next_token


class ListResourcePermissionStatementsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_signin.types.console_permission_max_results.ConsolePermissionMaxResults"
    ]
    """Maximum number of results to return"""
    next_token: NotRequired["capo_signin.types.next_token.NextToken"]
    """Token for pagination"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcePermissionStatementsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcePermissionStatementsInput:
    out: ListResourcePermissionStatementsInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
