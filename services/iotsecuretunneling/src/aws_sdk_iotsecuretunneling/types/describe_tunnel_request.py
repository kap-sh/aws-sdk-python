"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#DescribeTunnelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.tunnel_id


class DescribeTunnelRequest(TypedDict):
    tunnel_id: "aws_sdk_iotsecuretunneling.types.tunnel_id.TunnelId"
    """<p>The tunnel to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTunnelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTunnelRequest:
    out: DescribeTunnelRequest = {}  # type: ignore[typeddict-item]
    return out
