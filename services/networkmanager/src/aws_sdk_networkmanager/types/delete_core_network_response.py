"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteCoreNetworkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network


class DeleteCoreNetworkResponse(TypedDict):
    core_network: NotRequired["aws_sdk_networkmanager.types.core_network.CoreNetwork"]
    """<p>Information about the deleted core network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCoreNetworkResponse) -> dict:
    out: dict = {}
    if "core_network" in value:
        import aws_sdk_networkmanager.types.core_network

        out["CoreNetwork"] = aws_sdk_networkmanager.types.core_network.serialize_json(
            value["core_network"]
        )
    return out


def deserialize_json(data: dict) -> DeleteCoreNetworkResponse:
    out: DeleteCoreNetworkResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetwork" in data:
        import aws_sdk_networkmanager.types.core_network

        out["core_network"] = (
            aws_sdk_networkmanager.types.core_network.deserialize_json(
                data["CoreNetwork"]
            )
        )
    return out
