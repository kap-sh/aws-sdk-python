"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetMLConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.uuid


class GetMLConfigurationRequest(TypedDict, closed=True):
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that owns the ML configuration you want to return information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMLConfigurationRequest:
    out: GetMLConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
