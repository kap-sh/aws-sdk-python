"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppFlowPreviewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_flow_id
    import aws_sdk_socialmessaging.types.meta_flow_preview_info


class GetWhatsAppFlowPreviewOutput(TypedDict, closed=True):
    flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow.</p>"""
    preview: "aws_sdk_socialmessaging.types.meta_flow_preview_info.MetaFlowPreviewInfo"
    """<p>The preview URL and its expiration timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppFlowPreviewOutput) -> dict:
    out: dict = {}
    out["flowId"] = value["flow_id"]
    import aws_sdk_socialmessaging.types.meta_flow_preview_info

    out["preview"] = (
        aws_sdk_socialmessaging.types.meta_flow_preview_info.serialize_json(
            value["preview"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetWhatsAppFlowPreviewOutput:
    out: GetWhatsAppFlowPreviewOutput = {}  # type: ignore[typeddict-item]
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    else:
        raise DeserializationError("GetWhatsAppFlowPreviewOutput.flow_id required")
    if "preview" in data:
        import aws_sdk_socialmessaging.types.meta_flow_preview_info

        out["preview"] = (
            aws_sdk_socialmessaging.types.meta_flow_preview_info.deserialize_json(
                data["preview"]
            )
        )
    else:
        raise DeserializationError("GetWhatsAppFlowPreviewOutput.preview required")
    return out
