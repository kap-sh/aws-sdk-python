"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#StartTrainedModelExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.trained_model_arn
    import aws_sdk_cleanroomsml.types.trained_model_export_output_configuration
    import aws_sdk_cleanroomsml.types.uuid


class StartTrainedModelExportJobRequest(TypedDict, closed=True):
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model export job.</p>"""
    trained_model_arn: "aws_sdk_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model that you want to export.</p>"""
    trained_model_version_identifier: NotRequired[
        "aws_sdk_cleanroomsml.types.uuid.UUID"
    ]
    """<p>The version identifier of the trained model to export. This specifies which version of the trained model should be exported to the specified destination.</p>"""
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that is receiving the exported trained model artifacts.</p>"""
    output_configuration: "aws_sdk_cleanroomsml.types.trained_model_export_output_configuration.TrainedModelExportOutputConfiguration"
    """<p>The output configuration information for the trained model export job.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTrainedModelExportJobRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "trained_model_version_identifier" in value:
        out["trainedModelVersionIdentifier"] = value["trained_model_version_identifier"]
    import aws_sdk_cleanroomsml.types.trained_model_export_output_configuration

    out["outputConfiguration"] = (
        aws_sdk_cleanroomsml.types.trained_model_export_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StartTrainedModelExportJobRequest:
    out: StartTrainedModelExportJobRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartTrainedModelExportJobRequest.name required")
    if "trainedModelVersionIdentifier" in data:
        out["trained_model_version_identifier"] = data["trainedModelVersionIdentifier"]
    if "outputConfiguration" in data:
        import aws_sdk_cleanroomsml.types.trained_model_export_output_configuration

        out["output_configuration"] = (
            aws_sdk_cleanroomsml.types.trained_model_export_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartTrainedModelExportJobRequest.output_configuration required"
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
