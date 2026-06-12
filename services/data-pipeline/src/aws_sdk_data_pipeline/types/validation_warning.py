"""Generated from Smithy shape ``com.amazonaws.datapipeline#ValidationWarning``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.validation_messages


class ValidationWarning(TypedDict):
    id: NotRequired["aws_sdk_data_pipeline.types.id.id"]
    """<p>The identifier of the object that contains the validation warning.</p>"""
    warnings: NotRequired[
        "aws_sdk_data_pipeline.types.validation_messages.validationMessages"
    ]
    """<p>A description of the validation warning.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationWarning) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "warnings" in value:
        import aws_sdk_data_pipeline.types.validation_messages

        out["warnings"] = (
            aws_sdk_data_pipeline.types.validation_messages.serialize_aws_json_1_1(
                value["warnings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationWarning:
    out: ValidationWarning = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "warnings" in data:
        import aws_sdk_data_pipeline.types.validation_messages

        out["warnings"] = (
            aws_sdk_data_pipeline.types.validation_messages.deserialize_aws_json_1_1(
                data["warnings"]
            )
        )
    return out
