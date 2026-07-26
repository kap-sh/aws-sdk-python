"""Generated from Smithy shape ``com.amazonaws.supplychain#DeleteInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.uuid


class DeleteInstanceRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInstanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInstanceRequest:
    out: DeleteInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
