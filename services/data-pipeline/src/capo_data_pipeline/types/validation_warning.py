"""Generated from Smithy shape ``com.amazonaws.datapipeline#ValidationWarning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.validation_messages


class ValidationWarning(TypedDict, closed=True):
    id: NotRequired["capo_data_pipeline.types.id.id"]
    """<p>The identifier of the object that contains the validation warning.</p>"""
    warnings: NotRequired[
        "capo_data_pipeline.types.validation_messages.validationMessages"
    ]
    """<p>A description of the validation warning.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationWarning) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "warnings" in value:
        import capo_data_pipeline.types.validation_messages

        out["warnings"] = (
            capo_data_pipeline.types.validation_messages.serialize_aws_json_1_1(
                value["warnings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationWarning:
    out: ValidationWarning = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "warnings" in data:
        import capo_data_pipeline.types.validation_messages

        out["warnings"] = (
            capo_data_pipeline.types.validation_messages.deserialize_aws_json_1_1(
                data["warnings"]
            )
        )
    return out
