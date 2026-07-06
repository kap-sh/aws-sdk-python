"""Generated from Smithy shape ``com.amazonaws.odb#ListOdbNetworksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.odb_network_list


class ListOdbNetworksOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    odb_networks: "aws_sdk_odb.types.odb_network_list.OdbNetworkList"
    """<p>The list of ODB networks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOdbNetworksOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.odb_network_list

    out["odbNetworks"] = aws_sdk_odb.types.odb_network_list.serialize_aws_json_1_0(
        value["odb_networks"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOdbNetworksOutput:
    out: ListOdbNetworksOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "odbNetworks" in data:
        import aws_sdk_odb.types.odb_network_list

        out["odb_networks"] = (
            aws_sdk_odb.types.odb_network_list.deserialize_aws_json_1_0(
                data["odbNetworks"]
            )
        )
    else:
        raise DeserializationError("ListOdbNetworksOutput.odb_networks required")
    return out
