"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateCoreNetworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network


class UpdateCoreNetworkResponse(TypedDict, closed=True):
    core_network: NotRequired["aws_sdk_networkmanager.types.core_network.CoreNetwork"]
    """<p>Returns information about a core network update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCoreNetworkResponse) -> dict:
    out: dict = {}
    if "core_network" in value:
        import aws_sdk_networkmanager.types.core_network

        out["CoreNetwork"] = aws_sdk_networkmanager.types.core_network.serialize_json(
            value["core_network"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCoreNetworkResponse:
    out: UpdateCoreNetworkResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetwork" in data:
        import aws_sdk_networkmanager.types.core_network

        out["core_network"] = (
            aws_sdk_networkmanager.types.core_network.deserialize_json(
                data["CoreNetwork"]
            )
        )
    return out
