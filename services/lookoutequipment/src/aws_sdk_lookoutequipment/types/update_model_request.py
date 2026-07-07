"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UpdateModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.iam_role_arn
    import aws_sdk_lookoutequipment.types.labels_input_configuration
    import aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration
    import aws_sdk_lookoutequipment.types.model_name


class UpdateModelRequest(TypedDict, closed=True):
    model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the model to update.</p>"""
    labels_input_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.labels_input_configuration.LabelsInputConfiguration"
    ]
    role_arn: NotRequired["aws_sdk_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the model to update.</p>"""
    model_diagnostics_output_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration.ModelDiagnosticsOutputConfiguration"
    ]
    """<p>The Amazon S3 location where you want Amazon Lookout for Equipment to save the pointwise model diagnostics for the model. You must also specify the <code>RoleArn</code> request parameter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateModelRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    if "labels_input_configuration" in value:
        import aws_sdk_lookoutequipment.types.labels_input_configuration

        out["LabelsInputConfiguration"] = (
            aws_sdk_lookoutequipment.types.labels_input_configuration.serialize_aws_json_1_0(
                value["labels_input_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "model_diagnostics_output_configuration" in value:
        import aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration

        out["ModelDiagnosticsOutputConfiguration"] = (
            aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration.serialize_aws_json_1_0(
                value["model_diagnostics_output_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateModelRequest:
    out: UpdateModelRequest = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError("UpdateModelRequest.model_name required")
    if "LabelsInputConfiguration" in data:
        import aws_sdk_lookoutequipment.types.labels_input_configuration

        out["labels_input_configuration"] = (
            aws_sdk_lookoutequipment.types.labels_input_configuration.deserialize_aws_json_1_0(
                data["LabelsInputConfiguration"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ModelDiagnosticsOutputConfiguration" in data:
        import aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration

        out["model_diagnostics_output_configuration"] = (
            aws_sdk_lookoutequipment.types.model_diagnostics_output_configuration.deserialize_aws_json_1_0(
                data["ModelDiagnosticsOutputConfiguration"]
            )
        )
    return out
