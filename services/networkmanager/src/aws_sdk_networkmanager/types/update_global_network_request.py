"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateGlobalNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.global_network_id


class UpdateGlobalNetworkRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of your global network.</p>"""
    description: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
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
