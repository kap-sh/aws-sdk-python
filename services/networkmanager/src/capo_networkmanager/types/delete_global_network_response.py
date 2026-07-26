"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteGlobalNetworkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network


class DeleteGlobalNetworkResponse(TypedDict, closed=True):
    global_network: NotRequired[
        "capo_networkmanager.types.global_network.GlobalNetwork"
    ]
    """<p>Information about the global network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGlobalNetworkResponse) -> dict:
    out: dict = {}
    if "global_network" in value:
        import capo_networkmanager.types.global_network

        out["GlobalNetwork"] = capo_networkmanager.types.global_network.serialize_json(
            value["global_network"]
        )
    return out


def deserialize_json(data: dict) -> DeleteGlobalNetworkResponse:
    out: DeleteGlobalNetworkResponse = {}  # type: ignore[typeddict-item]
    if "GlobalNetwork" in data:
        import capo_networkmanager.types.global_network

        out["global_network"] = (
            capo_networkmanager.types.global_network.deserialize_json(
                data["GlobalNetwork"]
            )
        )
    return out
