"""Generated from Smithy shape ``com.amazonaws.iot#DeleteMitigationActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.mitigation_action_name


class DeleteMitigationActionRequest(TypedDict, closed=True):
    action_name: "capo_iot.types.mitigation_action_name.MitigationActionName"
    """<p>The name of the mitigation action that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMitigationActionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMitigationActionRequest:
    out: DeleteMitigationActionRequest = {}  # type: ignore[typeddict-item]
    return out
