"""Generated from Smithy shape ``com.amazonaws.qapps#GetQAppSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class GetQAppSessionInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    session_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App session to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQAppSessionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQAppSessionInput:
    out: GetQAppSessionInput = {}  # type: ignore[typeddict-item]
    return out
