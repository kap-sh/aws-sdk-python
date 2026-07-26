"""Generated from Smithy shape ``com.amazonaws.datapipeline#ValidationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.validation_messages


class ValidationError(TypedDict, closed=True):
    id: NotRequired["capo_data_pipeline.types.id.id"]
    """<p>The identifier of the object that contains the validation error.</p>"""
    errors: NotRequired[
        "capo_data_pipeline.types.validation_messages.validationMessages"
    ]
    """<p>A description of the validation error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationError) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "errors" in value:
        import capo_data_pipeline.types.validation_messages

        out["errors"] = (
            capo_data_pipeline.types.validation_messages.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationError:
    out: ValidationError = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "errors" in data:
        import capo_data_pipeline.types.validation_messages

        out["errors"] = (
            capo_data_pipeline.types.validation_messages.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out
