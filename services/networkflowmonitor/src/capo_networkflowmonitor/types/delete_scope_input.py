"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#DeleteScopeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.scope_id


class DeleteScopeInput(TypedDict, closed=True):
    scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId"
    """<p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScopeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScopeInput:
    out: DeleteScopeInput = {}  # type: ignore[typeddict-item]
    return out
