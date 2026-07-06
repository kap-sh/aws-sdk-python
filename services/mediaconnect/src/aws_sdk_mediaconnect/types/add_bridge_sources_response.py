"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_bridge_source


class AddBridgeSourcesResponse(TypedDict, closed=True):
    bridge_arn: NotRequired["str"]
    """<p> The ARN of the bridge that you added sources to.</p>"""
    sources: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_bridge_source.__listOfBridgeSource"
    ]
    """<p> The sources that you added to this bridge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeSourcesResponse) -> dict:
    out: dict = {}
    if "bridge_arn" in value:
        out["bridgeArn"] = value["bridge_arn"]
    if "sources" in value:
        import aws_sdk_mediaconnect.types.__list_of_bridge_source

        out["sources"] = (
            aws_sdk_mediaconnect.types.__list_of_bridge_source.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddBridgeSourcesResponse:
    out: AddBridgeSourcesResponse = {}  # type: ignore[typeddict-item]
    if "bridgeArn" in data:
        out["bridge_arn"] = data["bridgeArn"]
    if "sources" in data:
        import aws_sdk_mediaconnect.types.__list_of_bridge_source

        out["sources"] = (
            aws_sdk_mediaconnect.types.__list_of_bridge_source.deserialize_json(
                data["sources"]
            )
        )
    return out
