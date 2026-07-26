"""Generated from Smithy shape ``com.amazonaws.supplychain#GetInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.uuid


class GetInstanceRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInstanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInstanceRequest:
    out: GetInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
