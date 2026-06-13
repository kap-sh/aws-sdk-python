"""Generated from Smithy shape ``com.amazonaws.mediaconnect#InputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.interface


class InputConfiguration(TypedDict):
    input_ip: NotRequired["str"]
    """<p> The IP address that the flow listens on for incoming content for a media stream.</p>"""
    input_port: NotRequired["int"]
    """<p> The port that the flow listens on for an incoming media stream.</p>"""
    interface: NotRequired["aws_sdk_mediaconnect.types.interface.Interface"]
    """<p> The VPC interface where the media stream comes in from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputConfiguration) -> dict:
    out: dict = {}
    if "input_ip" in value:
        out["inputIp"] = value["input_ip"]
    if "input_port" in value:
        out["inputPort"] = value["input_port"]
    if "interface" in value:
        import aws_sdk_mediaconnect.types.interface

        out["interface"] = aws_sdk_mediaconnect.types.interface.serialize_json(
            value["interface"]
        )
    return out


def deserialize_json(data: dict) -> InputConfiguration:
    out: InputConfiguration = {}  # type: ignore[typeddict-item]
    if "inputIp" in data:
        out["input_ip"] = data["inputIp"]
    if "inputPort" in data:
        out["input_port"] = data["inputPort"]
    if "interface" in data:
        import aws_sdk_mediaconnect.types.interface

        out["interface"] = aws_sdk_mediaconnect.types.interface.deserialize_json(
            data["interface"]
        )
    return out
