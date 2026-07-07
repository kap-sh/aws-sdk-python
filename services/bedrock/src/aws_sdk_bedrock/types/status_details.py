"""Generated from Smithy shape ``com.amazonaws.bedrock#StatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.data_processing_details
    import aws_sdk_bedrock.types.training_details
    import aws_sdk_bedrock.types.validation_details


class StatusDetails(TypedDict, closed=True):
    validation_details: NotRequired[
        "aws_sdk_bedrock.types.validation_details.ValidationDetails"
    ]
    """<p>The status details for the validation sub-task of the job.</p>"""
    data_processing_details: NotRequired[
        "aws_sdk_bedrock.types.data_processing_details.DataProcessingDetails"
    ]
    """<p>The status details for the data processing sub-task of the job.</p>"""
    training_details: NotRequired[
        "aws_sdk_bedrock.types.training_details.TrainingDetails"
    ]
    """<p>The status details for the training sub-task of the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusDetails) -> dict:
    out: dict = {}
    if "validation_details" in value:
        import aws_sdk_bedrock.types.validation_details

        out["validationDetails"] = (
            aws_sdk_bedrock.types.validation_details.serialize_json(
                value["validation_details"]
            )
        )
    if "data_processing_details" in value:
        import aws_sdk_bedrock.types.data_processing_details

        out["dataProcessingDetails"] = (
            aws_sdk_bedrock.types.data_processing_details.serialize_json(
                value["data_processing_details"]
            )
        )
    if "training_details" in value:
        import aws_sdk_bedrock.types.training_details

        out["trainingDetails"] = aws_sdk_bedrock.types.training_details.serialize_json(
            value["training_details"]
        )
    return out


def deserialize_json(data: dict) -> StatusDetails:
    out: StatusDetails = {}  # type: ignore[typeddict-item]
    if "validationDetails" in data:
        import aws_sdk_bedrock.types.validation_details

        out["validation_details"] = (
            aws_sdk_bedrock.types.validation_details.deserialize_json(
                data["validationDetails"]
            )
        )
    if "dataProcessingDetails" in data:
        import aws_sdk_bedrock.types.data_processing_details

        out["data_processing_details"] = (
            aws_sdk_bedrock.types.data_processing_details.deserialize_json(
                data["dataProcessingDetails"]
            )
        )
    if "trainingDetails" in data:
        import aws_sdk_bedrock.types.training_details

        out["training_details"] = (
            aws_sdk_bedrock.types.training_details.deserialize_json(
                data["trainingDetails"]
            )
        )
    return out
