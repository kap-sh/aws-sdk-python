"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_source


class UpdateBridgeSourceResponse(TypedDict):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the updated bridge source. </p>"""
    source: NotRequired["aws_sdk_mediaconnect.types.bridge_source.BridgeSource"]
    """<p> The updated bridge source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeSourceResponse) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "source" in value:
        import aws_sdk_mediaconnect.types.bridge_source

        out["source"] = aws_sdk_mediaconnect.types.bridge_source.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBridgeSourceResponse:
    out: UpdateBridgeSourceResponse = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "source" in data:
        import aws_sdk_mediaconnect.types.bridge_source

        out["source"] = aws_sdk_mediaconnect.types.bridge_source.deserialize_json(
            data["source"]
        )
    return out
