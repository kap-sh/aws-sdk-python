"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateGlobalNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.global_network_id


class UpdateGlobalNetworkRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of your global network.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of the global network.</p> <p>Constraints: Maximum length of 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGlobalNetworkRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateGlobalNetworkRequest:
    out: UpdateGlobalNetworkRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
