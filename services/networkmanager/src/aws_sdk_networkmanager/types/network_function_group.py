"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkFunctionGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string


class NetworkFunctionGroup(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The name of the network function group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkFunctionGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> NetworkFunctionGroup:
    out: NetworkFunctionGroup = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
