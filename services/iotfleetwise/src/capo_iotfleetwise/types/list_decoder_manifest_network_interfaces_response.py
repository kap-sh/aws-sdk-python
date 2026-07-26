"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListDecoderManifestNetworkInterfacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.network_interfaces
    import capo_iotfleetwise.types.next_token


class ListDecoderManifestNetworkInterfacesResponse(TypedDict, closed=True):
    network_interfaces: NotRequired[
        "capo_iotfleetwise.types.network_interfaces.NetworkInterfaces"
    ]
    """<p> A list of information about network interfaces. </p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDecoderManifestNetworkInterfacesResponse) -> dict:
    out: dict = {}
    if "network_interfaces" in value:
        import capo_iotfleetwise.types.network_interfaces

        out["networkInterfaces"] = (
            capo_iotfleetwise.types.network_interfaces.serialize_aws_json_1_0(
                value["network_interfaces"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListDecoderManifestNetworkInterfacesResponse:
    out: ListDecoderManifestNetworkInterfacesResponse = {}  # type: ignore[typeddict-item]
    if "networkInterfaces" in data:
        import capo_iotfleetwise.types.network_interfaces

        out["network_interfaces"] = (
            capo_iotfleetwise.types.network_interfaces.deserialize_aws_json_1_0(
                data["networkInterfaces"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
