"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetDedicatedIpResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.dedicated_ip


class GetDedicatedIpResponse(TypedDict):
    dedicated_ip: NotRequired["aws_sdk_pinpoint_email.types.dedicated_ip.DedicatedIp"]
    """<p>An object that contains information about a dedicated IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDedicatedIpResponse) -> dict:
    out: dict = {}
    if "dedicated_ip" in value:
        import aws_sdk_pinpoint_email.types.dedicated_ip

        out["DedicatedIp"] = aws_sdk_pinpoint_email.types.dedicated_ip.serialize_json(
            value["dedicated_ip"]
        )
    return out


def deserialize_json(data: dict) -> GetDedicatedIpResponse:
    out: GetDedicatedIpResponse = {}  # type: ignore[typeddict-item]
    if "DedicatedIp" in data:
        import aws_sdk_pinpoint_email.types.dedicated_ip

        out["dedicated_ip"] = (
            aws_sdk_pinpoint_email.types.dedicated_ip.deserialize_json(
                data["DedicatedIp"]
            )
        )
    return out
