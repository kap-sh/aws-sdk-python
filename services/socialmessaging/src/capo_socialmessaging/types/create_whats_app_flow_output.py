"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppFlowOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_id
    import capo_socialmessaging.types.validation_error_list


class CreateWhatsAppFlowOutput(TypedDict, closed=True):
    flow_id: NotRequired["capo_socialmessaging.types.meta_flow_id.MetaFlowId"]
    """<p>The unique identifier assigned to the Flow by Meta.</p>"""
    validation_errors: NotRequired[
        "capo_socialmessaging.types.validation_error_list.ValidationErrorList"
    ]
    """<p>A list of validation errors returned by Meta, if any. Validation errors must be resolved before the Flow can be published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppFlowOutput) -> dict:
    out: dict = {}
    if "flow_id" in value:
        out["flowId"] = value["flow_id"]
    if "validation_errors" in value:
        import capo_socialmessaging.types.validation_error_list

        out["validationErrors"] = (
            capo_socialmessaging.types.validation_error_list.serialize_json(
                value["validation_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateWhatsAppFlowOutput:
    out: CreateWhatsAppFlowOutput = {}  # type: ignore[typeddict-item]
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    if "validationErrors" in data:
        import capo_socialmessaging.types.validation_error_list

        out["validation_errors"] = (
            capo_socialmessaging.types.validation_error_list.deserialize_json(
                data["validationErrors"]
            )
        )
    return out
