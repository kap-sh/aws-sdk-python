"""Generated from Smithy shape ``com.amazonaws.directconnect#DisassociateMacSecKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.mac_sec_key_list


class DisassociateMacSecKeyResponse(TypedDict):
    connection_id: NotRequired[
        "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    ]
    """<p>The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).</p>"""
    mac_sec_keys: NotRequired[
        "aws_sdk_direct_connect.types.mac_sec_key_list.MacSecKeyList"
    ]
    """<p>The MAC Security (MACsec) security keys no longer associated with the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateMacSecKeyResponse) -> dict:
    out: dict = {}
    if "connection_id" in value:
        out["connectionId"] = value["connection_id"]
    if "mac_sec_keys" in value:
        import aws_sdk_direct_connect.types.mac_sec_key_list

        out["macSecKeys"] = (
            aws_sdk_direct_connect.types.mac_sec_key_list.serialize_aws_json_1_1(
                value["mac_sec_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateMacSecKeyResponse:
    out: DisassociateMacSecKeyResponse = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    if "macSecKeys" in data:
        import aws_sdk_direct_connect.types.mac_sec_key_list

        out["mac_sec_keys"] = (
            aws_sdk_direct_connect.types.mac_sec_key_list.deserialize_aws_json_1_1(
                data["macSecKeys"]
            )
        )
    return out
