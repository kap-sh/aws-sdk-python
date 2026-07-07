"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UpdateWhatsAppFlowAssetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.meta_flow_id
    import aws_sdk_socialmessaging.types.meta_flow_json_blob


class UpdateWhatsAppFlowAssetsInput(TypedDict, closed=True):
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this Flow.</p>"""
    flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow whose assets to update.</p>"""
    flow_json: "aws_sdk_socialmessaging.types.meta_flow_json_blob.MetaFlowJsonBlob"
    """<p>The updated Flow JSON definition. Maximum size is 10 MB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWhatsAppFlowAssetsInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["flowId"] = value["flow_id"]
    import aws_sdk_socialmessaging.types.meta_flow_json_blob

    out["flowJson"] = aws_sdk_socialmessaging.types.meta_flow_json_blob.serialize_json(
        value["flow_json"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWhatsAppFlowAssetsInput:
    out: UpdateWhatsAppFlowAssetsInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateWhatsAppFlowAssetsInput.id required")
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    else:
        raise DeserializationError("UpdateWhatsAppFlowAssetsInput.flow_id required")
    if "flowJson" in data:
        import aws_sdk_socialmessaging.types.meta_flow_json_blob

        out["flow_json"] = (
            aws_sdk_socialmessaging.types.meta_flow_json_blob.deserialize_json(
                data["flowJson"]
            )
        )
    else:
        raise DeserializationError("UpdateWhatsAppFlowAssetsInput.flow_json required")
    return out
