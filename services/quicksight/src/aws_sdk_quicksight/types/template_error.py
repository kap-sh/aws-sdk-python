"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.entity_list
    import aws_sdk_quicksight.types.non_empty_string
    import aws_sdk_quicksight.types.template_error_type


class TemplateError(TypedDict, closed=True):
    type: NotRequired["aws_sdk_quicksight.types.template_error_type.TemplateErrorType"]
    """<p>Type of error.</p>"""
    message: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>Description of the error type.</p>"""
    violated_entities: NotRequired["aws_sdk_quicksight.types.entity_list.EntityList"]
    """<p>An error path that shows which entities caused the template error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateError) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_quicksight.types.template_error_type

        out["Type"] = aws_sdk_quicksight.types.template_error_type.serialize_json(
            value["type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "violated_entities" in value:
        import aws_sdk_quicksight.types.entity_list

        out["ViolatedEntities"] = aws_sdk_quicksight.types.entity_list.serialize_json(
            value["violated_entities"]
        )
    return out


def deserialize_json(data: dict) -> TemplateError:
    out: TemplateError = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_quicksight.types.template_error_type

        out["type"] = aws_sdk_quicksight.types.template_error_type.deserialize_json(
            data["Type"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ViolatedEntities" in data:
        import aws_sdk_quicksight.types.entity_list

        out["violated_entities"] = (
            aws_sdk_quicksight.types.entity_list.deserialize_json(
                data["ViolatedEntities"]
            )
        )
    return out
