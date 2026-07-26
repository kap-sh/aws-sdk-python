"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.connect_peer_error_code
    import capo_networkmanager.types.resource_arn
    import capo_networkmanager.types.server_side_string


class ConnectPeerError(TypedDict, closed=True):
    code: NotRequired[
        "capo_networkmanager.types.connect_peer_error_code.ConnectPeerErrorCode"
    ]
    """<p>The error code for the Connect peer request.</p>"""
    message: NotRequired[
        "capo_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The message associated with the error <code>code</code>.</p>"""
    resource_arn: NotRequired["capo_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the requested Connect peer resource.</p>"""
    request_id: NotRequired[
        "capo_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The ID of the Connect peer request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerError) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_networkmanager.types.connect_peer_error_code

        out["Code"] = capo_networkmanager.types.connect_peer_error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ConnectPeerError:
    out: ConnectPeerError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_networkmanager.types.connect_peer_error_code

        out["code"] = (
            capo_networkmanager.types.connect_peer_error_code.deserialize_json(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
