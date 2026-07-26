"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetConnectivityInfoResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.connectivity_info_list
    import capo_greengrassv2.types.string


class GetConnectivityInfoResponse(TypedDict, closed=True):
    connectivity_info: NotRequired[
        "capo_greengrassv2.types.connectivity_info_list.connectivityInfoList"
    ]
    """<p>The connectivity information for the core device.</p>"""
    message: NotRequired["capo_greengrassv2.types.string.String"]
    """<p>A message about the connectivity information request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectivityInfoResponse) -> dict:
    out: dict = {}
    if "connectivity_info" in value:
        import capo_greengrassv2.types.connectivity_info_list

        out["ConnectivityInfo"] = (
            capo_greengrassv2.types.connectivity_info_list.serialize_json(
                value["connectivity_info"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GetConnectivityInfoResponse:
    out: GetConnectivityInfoResponse = {}  # type: ignore[typeddict-item]
    if "ConnectivityInfo" in data:
        import capo_greengrassv2.types.connectivity_info_list

        out["connectivity_info"] = (
            capo_greengrassv2.types.connectivity_info_list.deserialize_json(
                data["ConnectivityInfo"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
