"""Generated from Smithy shape ``com.amazonaws.greengrass#GetConnectivityInfoResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_connectivity_info
    import capo_greengrass.types.__string


class GetConnectivityInfoResponse(TypedDict, closed=True):
    connectivity_info: NotRequired[
        "capo_greengrass.types.__list_of_connectivity_info.__listOfConnectivityInfo"
    ]
    """Connectivity info list."""
    message: NotRequired["capo_greengrass.types.__string.__string"]
    """A message about the connectivity info request."""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectivityInfoResponse) -> dict:
    out: dict = {}
    if "connectivity_info" in value:
        import capo_greengrass.types.__list_of_connectivity_info

        out["ConnectivityInfo"] = (
            capo_greengrass.types.__list_of_connectivity_info.serialize_json(
                value["connectivity_info"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GetConnectivityInfoResponse:
    out: GetConnectivityInfoResponse = {}  # type: ignore[typeddict-item]
    if "ConnectivityInfo" in data:
        import capo_greengrass.types.__list_of_connectivity_info

        out["connectivity_info"] = (
            capo_greengrass.types.__list_of_connectivity_info.deserialize_json(
                data["ConnectivityInfo"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
