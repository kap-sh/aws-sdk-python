"""Generated from Smithy shape ``com.amazonaws.sesv2#GetDedicatedIpResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.dedicated_ip


class GetDedicatedIpResponse(TypedDict, closed=True):
    dedicated_ip: NotRequired["aws_sdk_sesv2.types.dedicated_ip.DedicatedIp"]
    """<p>An object that contains information about a dedicated IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDedicatedIpResponse) -> dict:
    out: dict = {}
    if "dedicated_ip" in value:
        import aws_sdk_sesv2.types.dedicated_ip

        out["DedicatedIp"] = aws_sdk_sesv2.types.dedicated_ip.serialize_json(
            value["dedicated_ip"]
        )
    return out


def deserialize_json(data: dict) -> GetDedicatedIpResponse:
    out: GetDedicatedIpResponse = {}  # type: ignore[typeddict-item]
    if "DedicatedIp" in data:
        import aws_sdk_sesv2.types.dedicated_ip

        out["dedicated_ip"] = aws_sdk_sesv2.types.dedicated_ip.deserialize_json(
            data["DedicatedIp"]
        )
    return out
