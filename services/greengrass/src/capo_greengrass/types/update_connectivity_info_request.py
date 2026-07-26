"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateConnectivityInfoRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__list_of_connectivity_info
    import capo_greengrass.types.__string


class UpdateConnectivityInfoRequest(TypedDict, closed=True):
    connectivity_info: NotRequired[
        "capo_greengrass.types.__list_of_connectivity_info.__listOfConnectivityInfo"
    ]
    """A list of connectivity info."""
    thing_name: "capo_greengrass.types.__string.__string"
    """The thing name."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectivityInfoRequest) -> dict:
    out: dict = {}
    if "connectivity_info" in value:
        import capo_greengrass.types.__list_of_connectivity_info

        out["ConnectivityInfo"] = (
            capo_greengrass.types.__list_of_connectivity_info.serialize_json(
                value["connectivity_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectivityInfoRequest:
    out: UpdateConnectivityInfoRequest = {}  # type: ignore[typeddict-item]
    if "ConnectivityInfo" in data:
        import capo_greengrass.types.__list_of_connectivity_info

        out["connectivity_info"] = (
            capo_greengrass.types.__list_of_connectivity_info.deserialize_json(
                data["ConnectivityInfo"]
            )
        )
    return out
