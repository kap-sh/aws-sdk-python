"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateCoreNetworkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network


class CreateCoreNetworkResponse(TypedDict):
    core_network: NotRequired["aws_sdk_networkmanager.types.core_network.CoreNetwork"]
    """<p>Returns details about a core network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCoreNetworkResponse) -> dict:
    out: dict = {}
    if "core_network" in value:
        import aws_sdk_networkmanager.types.core_network

        out["CoreNetwork"] = aws_sdk_networkmanager.types.core_network.serialize_json(
            value["core_network"]
        )
    return out


def deserialize_json(data: dict) -> CreateCoreNetworkResponse:
    out: CreateCoreNetworkResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetwork" in data:
        import aws_sdk_networkmanager.types.core_network

        out["core_network"] = (
            aws_sdk_networkmanager.types.core_network.deserialize_json(
                data["CoreNetwork"]
            )
        )
    return out
