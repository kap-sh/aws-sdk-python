"""Generated from Smithy shape ``com.amazonaws.fis#GetActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fis.types.action_id


class GetActionRequest(TypedDict, closed=True):
    id: "capo_fis.types.action_id.ActionId"
    """<p>The ID of the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetActionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetActionRequest:
    out: GetActionRequest = {}  # type: ignore[typeddict-item]
    return out
