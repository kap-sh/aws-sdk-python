"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowPreviewInfo``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_flow_preview_url
    import aws_sdk_socialmessaging.types.meta_flow_timestamp


class MetaFlowPreviewInfo(TypedDict):
    preview_url: (
        "aws_sdk_socialmessaging.types.meta_flow_preview_url.MetaFlowPreviewUrl"
    )
    """<p>The web URL for previewing the Flow. Can be shared with stakeholders for review.</p>"""
    expires_at: "aws_sdk_socialmessaging.types.meta_flow_timestamp.MetaFlowTimestamp"
    """<p>The timestamp when the preview URL expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowPreviewInfo) -> dict:
    out: dict = {}
    out["previewUrl"] = value["preview_url"]
    out["expiresAt"] = value["expires_at"]
    return out


def deserialize_json(data: dict) -> MetaFlowPreviewInfo:
    out: MetaFlowPreviewInfo = {}  # type: ignore[typeddict-item]
    if "previewUrl" in data:
        out["preview_url"] = data["previewUrl"]
    else:
        raise DeserializationError("MetaFlowPreviewInfo.preview_url required")
    if "expiresAt" in data:
        out["expires_at"] = data["expiresAt"]
    else:
        raise DeserializationError("MetaFlowPreviewInfo.expires_at required")
    return out
