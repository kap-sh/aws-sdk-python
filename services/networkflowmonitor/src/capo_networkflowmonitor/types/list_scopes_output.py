"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ListScopesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkflowmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.scope_summary_list


class ListScopesOutput(TypedDict, closed=True):
    scopes: "capo_networkflowmonitor.types.scope_summary_list.ScopeSummaryList"
    """<p>The scopes returned by the call.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScopesOutput) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.scope_summary_list

    out["scopes"] = capo_networkflowmonitor.types.scope_summary_list.serialize_json(
        value["scopes"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListScopesOutput:
    out: ListScopesOutput = {}  # type: ignore[typeddict-item]
    if "scopes" in data:
        import capo_networkflowmonitor.types.scope_summary_list

        out["scopes"] = (
            capo_networkflowmonitor.types.scope_summary_list.deserialize_json(
                data["scopes"]
            )
        )
    else:
        raise DeserializationError("ListScopesOutput.scopes required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
