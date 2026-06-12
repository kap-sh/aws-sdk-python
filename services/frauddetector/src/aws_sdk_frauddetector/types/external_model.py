"""Generated from Smithy shape ``com.amazonaws.frauddetector#ExternalModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.model_endpoint_status
    import aws_sdk_frauddetector.types.model_input_configuration
    import aws_sdk_frauddetector.types.model_output_configuration
    import aws_sdk_frauddetector.types.model_source
    import aws_sdk_frauddetector.types.string
    import aws_sdk_frauddetector.types.time


class ExternalModel(TypedDict):
    model_endpoint: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The Amazon SageMaker model endpoints.</p>"""
    model_source: NotRequired["aws_sdk_frauddetector.types.model_source.ModelSource"]
    """<p>The source of the model.</p>"""
    invoke_model_endpoint_role_arn: NotRequired[
        "aws_sdk_frauddetector.types.string.string"
    ]
    """<p>The role used to invoke the model. </p>"""
    input_configuration: NotRequired[
        "aws_sdk_frauddetector.types.model_input_configuration.ModelInputConfiguration"
    ]
    """<p>The input configuration.</p>"""
    output_configuration: NotRequired[
        "aws_sdk_frauddetector.types.model_output_configuration.ModelOutputConfiguration"
    ]
    """<p>The output configuration.</p>"""
    model_endpoint_status: NotRequired[
        "aws_sdk_frauddetector.types.model_endpoint_status.ModelEndpointStatus"
    ]
    """<p>The Amazon Fraud Detector status for the external model endpoint</p>"""
    last_updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the model was last updated.</p>"""
    created_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the model was last created.</p>"""
    arn: NotRequired["aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The model ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalModel) -> dict:
    out: dict = {}
    if "model_endpoint" in value:
        out["modelEndpoint"] = value["model_endpoint"]
    if "model_source" in value:
        import aws_sdk_frauddetector.types.model_source

        out["modelSource"] = (
            aws_sdk_frauddetector.types.model_source.serialize_aws_json_1_1(
                value["model_source"]
            )
        )
    if "invoke_model_endpoint_role_arn" in value:
        out["invokeModelEndpointRoleArn"] = value["invoke_model_endpoint_role_arn"]
    if "input_configuration" in value:
        import aws_sdk_frauddetector.types.model_input_configuration

        out["inputConfiguration"] = (
            aws_sdk_frauddetector.types.model_input_configuration.serialize_aws_json_1_1(
                value["input_configuration"]
            )
        )
    if "output_configuration" in value:
        import aws_sdk_frauddetector.types.model_output_configuration

        out["outputConfiguration"] = (
            aws_sdk_frauddetector.types.model_output_configuration.serialize_aws_json_1_1(
                value["output_configuration"]
            )
        )
    if "model_endpoint_status" in value:
        import aws_sdk_frauddetector.types.model_endpoint_status

        out["modelEndpointStatus"] = (
            aws_sdk_frauddetector.types.model_endpoint_status.serialize_aws_json_1_1(
                value["model_endpoint_status"]
            )
        )
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalModel:
    out: ExternalModel = {}  # type: ignore[typeddict-item]
    if "modelEndpoint" in data:
        out["model_endpoint"] = data["modelEndpoint"]
    if "modelSource" in data:
        import aws_sdk_frauddetector.types.model_source

        out["model_source"] = (
            aws_sdk_frauddetector.types.model_source.deserialize_aws_json_1_1(
                data["modelSource"]
            )
        )
    if "invokeModelEndpointRoleArn" in data:
        out["invoke_model_endpoint_role_arn"] = data["invokeModelEndpointRoleArn"]
    if "inputConfiguration" in data:
        import aws_sdk_frauddetector.types.model_input_configuration

        out["input_configuration"] = (
            aws_sdk_frauddetector.types.model_input_configuration.deserialize_aws_json_1_1(
                data["inputConfiguration"]
            )
        )
    if "outputConfiguration" in data:
        import aws_sdk_frauddetector.types.model_output_configuration

        out["output_configuration"] = (
            aws_sdk_frauddetector.types.model_output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    if "modelEndpointStatus" in data:
        import aws_sdk_frauddetector.types.model_endpoint_status

        out["model_endpoint_status"] = (
            aws_sdk_frauddetector.types.model_endpoint_status.deserialize_aws_json_1_1(
                data["modelEndpointStatus"]
            )
        )
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
