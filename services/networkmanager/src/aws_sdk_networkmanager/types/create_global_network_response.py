"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateGlobalNetworkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network


class CreateGlobalNetworkResponse(TypedDict):
    global_network: NotRequired[
        "aws_sdk_networkmanager.types.global_network.GlobalNetwork"
    ]
    """<p>Information about the global network object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGlobalNetworkResponse) -> dict:
    out: dict = {}
    if "global_network" in value:
        import aws_sdk_networkmanager.types.global_network

        out["GlobalNetwork"] = (
            aws_sdk_networkmanager.types.global_network.serialize_json(
                value["global_network"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGlobalNetworkResponse:
    out: CreateGlobalNetworkResponse = {}  # type: ignore[typeddict-item]
    if "GlobalNetwork" in data:
        import aws_sdk_networkmanager.types.global_network

        out["global_network"] = (
            aws_sdk_networkmanager.types.global_network.deserialize_json(
                data["GlobalNetwork"]
            )
        )
    return out
