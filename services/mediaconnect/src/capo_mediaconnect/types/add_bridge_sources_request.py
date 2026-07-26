"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_add_bridge_source_request
    import capo_mediaconnect.types.bridge_arn


class AddBridgeSourcesRequest(TypedDict, closed=True):
    bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn"
    """<p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>"""
    sources: NotRequired[
        "capo_mediaconnect.types.__list_of_add_bridge_source_request.__listOfAddBridgeSourceRequest"
    ]
    """<p> The sources that you want to add to this bridge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeSourcesRequest) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_mediaconnect.types.__list_of_add_bridge_source_request

        out["sources"] = (
            capo_mediaconnect.types.__list_of_add_bridge_source_request.serialize_json(
                value["sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddBridgeSourcesRequest:
    out: AddBridgeSourcesRequest = {}  # type: ignore[typeddict-item]
    if "sources" in data:
        import capo_mediaconnect.types.__list_of_add_bridge_source_request

        out["sources"] = (
            capo_mediaconnect.types.__list_of_add_bridge_source_request.deserialize_json(
                data["sources"]
            )
        )
    return out
