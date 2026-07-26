"""Generated from Smithy shape ``com.amazonaws.osis#ValidatePipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.boolean
    import capo_osis.types.validation_message_list


class ValidatePipelineResponse(TypedDict, closed=True):
    is_valid: NotRequired["capo_osis.types.boolean.Boolean"]
    """<p>A boolean indicating whether or not the pipeline configuration is valid.</p>"""
    errors: NotRequired["capo_osis.types.validation_message_list.ValidationMessageList"]
    """<p>A list of errors if the configuration is invalid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidatePipelineResponse) -> dict:
    out: dict = {}
    if "is_valid" in value:
        out["isValid"] = value["is_valid"]
    if "errors" in value:
        import capo_osis.types.validation_message_list

        out["Errors"] = capo_osis.types.validation_message_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> ValidatePipelineResponse:
    out: ValidatePipelineResponse = {}  # type: ignore[typeddict-item]
    if "isValid" in data:
        out["is_valid"] = data["isValid"]
    if "Errors" in data:
        import capo_osis.types.validation_message_list

        out["errors"] = capo_osis.types.validation_message_list.deserialize_json(
            data["Errors"]
        )
    return out
