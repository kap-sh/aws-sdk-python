"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#CloseTunnelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.delete_flag
    import aws_sdk_iotsecuretunneling.types.tunnel_id


class CloseTunnelRequest(TypedDict):
    tunnel_id: "aws_sdk_iotsecuretunneling.types.tunnel_id.TunnelId"
    """<p>The ID of the tunnel to close.</p>"""
    delete: NotRequired["aws_sdk_iotsecuretunneling.types.delete_flag.DeleteFlag"]
    """<p>When set to true, IoT Secure Tunneling deletes the tunnel data immediately.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloseTunnelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CloseTunnelRequest:
    out: CloseTunnelRequest = {}  # type: ignore[typeddict-item]
    return out
