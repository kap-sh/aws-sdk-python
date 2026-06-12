"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UpdateWhatsAppFlowInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.meta_flow_category_list
    import aws_sdk_socialmessaging.types.meta_flow_id
    import aws_sdk_socialmessaging.types.meta_flow_name


class UpdateWhatsAppFlowInput(TypedDict):
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this Flow.</p>"""
    flow_id: "aws_sdk_socialmessaging.types.meta_flow_id.MetaFlowId"
    """<p>The unique identifier of the Flow to update.</p>"""
    flow_name: NotRequired["aws_sdk_socialmessaging.types.meta_flow_name.MetaFlowName"]
    """<p>The updated name for the Flow.</p>"""
    categories: NotRequired[
        "aws_sdk_socialmessaging.types.meta_flow_category_list.MetaFlowCategoryList"
    ]
    """<p>The updated categories for the Flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWhatsAppFlowInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["flowId"] = value["flow_id"]
    if "flow_name" in value:
        out["flowName"] = value["flow_name"]
    if "categories" in value:
        import aws_sdk_socialmessaging.types.meta_flow_category_list

        out["categories"] = (
            aws_sdk_socialmessaging.types.meta_flow_category_list.serialize_json(
                value["categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWhatsAppFlowInput:
    out: UpdateWhatsAppFlowInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateWhatsAppFlowInput.id required")
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    else:
        raise DeserializationError("UpdateWhatsAppFlowInput.flow_id required")
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    if "categories" in data:
        import aws_sdk_socialmessaging.types.meta_flow_category_list

        out["categories"] = (
            aws_sdk_socialmessaging.types.meta_flow_category_list.deserialize_json(
                data["categories"]
            )
        )
    return out
