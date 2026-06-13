"""Generated from Smithy shape ``com.amazonaws.mediaconnect#InputConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.interface_request


class InputConfigurationRequest(TypedDict):
    input_port: NotRequired["int"]
    """<p> The port that you want the flow to listen on for an incoming media stream.</p>"""
    interface: NotRequired[
        "aws_sdk_mediaconnect.types.interface_request.InterfaceRequest"
    ]
    """<p> The VPC interface that you want to use for the incoming media stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputConfigurationRequest) -> dict:
    out: dict = {}
    if "input_port" in value:
        out["inputPort"] = value["input_port"]
    if "interface" in value:
        import aws_sdk_mediaconnect.types.interface_request

        out["interface"] = aws_sdk_mediaconnect.types.interface_request.serialize_json(
            value["interface"]
        )
    return out


def deserialize_json(data: dict) -> InputConfigurationRequest:
    out: InputConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "inputPort" in data:
        out["input_port"] = data["inputPort"]
    if "interface" in data:
        import aws_sdk_mediaconnect.types.interface_request

        out["interface"] = (
            aws_sdk_mediaconnect.types.interface_request.deserialize_json(
                data["interface"]
            )
        )
    return out
