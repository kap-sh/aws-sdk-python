"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#DescribeTunnelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.tunnel


class DescribeTunnelResponse(TypedDict, closed=True):
    tunnel: NotRequired["capo_iotsecuretunneling.types.tunnel.Tunnel"]
    """<p>The tunnel being described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTunnelResponse) -> dict:
    out: dict = {}
    if "tunnel" in value:
        import capo_iotsecuretunneling.types.tunnel

        out["tunnel"] = capo_iotsecuretunneling.types.tunnel.serialize_aws_json_1_1(
            value["tunnel"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTunnelResponse:
    out: DescribeTunnelResponse = {}  # type: ignore[typeddict-item]
    if "tunnel" in data:
        import capo_iotsecuretunneling.types.tunnel

        out["tunnel"] = capo_iotsecuretunneling.types.tunnel.deserialize_aws_json_1_1(
            data["tunnel"]
        )
    return out
