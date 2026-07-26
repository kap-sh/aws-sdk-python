"""Generated from Smithy shape ``com.amazonaws.qapps#ListQAppSessionDataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.uuid


class ListQAppSessionDataInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    session_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App data collection session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQAppSessionDataInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQAppSessionDataInput:
    out: ListQAppSessionDataInput = {}  # type: ignore[typeddict-item]
    return out
