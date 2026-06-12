"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UpdateWhatsAppFlowAssetsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.validation_error_list


class UpdateWhatsAppFlowAssetsOutput(TypedDict):
    validation_errors: NotRequired[
        "aws_sdk_socialmessaging.types.validation_error_list.ValidationErrorList"
    ]
    """<p>A list of validation errors returned by Meta, if any. Validation errors must be resolved before the Flow can be published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWhatsAppFlowAssetsOutput) -> dict:
    out: dict = {}
    if "validation_errors" in value:
        import aws_sdk_socialmessaging.types.validation_error_list

        out["validationErrors"] = (
            aws_sdk_socialmessaging.types.validation_error_list.serialize_json(
                value["validation_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWhatsAppFlowAssetsOutput:
    out: UpdateWhatsAppFlowAssetsOutput = {}  # type: ignore[typeddict-item]
    if "validationErrors" in data:
        import aws_sdk_socialmessaging.types.validation_error_list

        out["validation_errors"] = (
            aws_sdk_socialmessaging.types.validation_error_list.deserialize_json(
                data["validationErrors"]
            )
        )
    return out
