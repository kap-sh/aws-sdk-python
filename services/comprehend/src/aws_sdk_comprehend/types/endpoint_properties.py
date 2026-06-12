"""Generated from Smithy shape ``com.amazonaws.comprehend#EndpointProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.any_length_string
    import aws_sdk_comprehend.types.comprehend_endpoint_arn
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.comprehend_model_arn
    import aws_sdk_comprehend.types.endpoint_status
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.inference_units_integer
    import aws_sdk_comprehend.types.timestamp


class EndpointProperties(TypedDict):
    endpoint_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_endpoint_arn.ComprehendEndpointArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the endpoint.</p>"""
    status: NotRequired["aws_sdk_comprehend.types.endpoint_status.EndpointStatus"]
    """<p>Specifies the status of the endpoint. Because the endpoint updates and creation are asynchronous, so customers will need to wait for the endpoint to be <code>Ready</code> status before making inference requests.</p>"""
    message: NotRequired["aws_sdk_comprehend.types.any_length_string.AnyLengthString"]
    """<p>Specifies a reason for failure in cases of <code>Failed</code> status.</p>"""
    model_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the model to which the endpoint is attached.</p>"""
    desired_model_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>ARN of the new model to use for updating an existing endpoint. This ARN is going to be different from the model ARN when the update is in progress</p>"""
    desired_inference_units: NotRequired[
        "aws_sdk_comprehend.types.inference_units_integer.InferenceUnitsInteger"
    ]
    """<p>The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.</p>"""
    current_inference_units: NotRequired[
        "aws_sdk_comprehend.types.inference_units_integer.InferenceUnitsInteger"
    ]
    """<p>The number of inference units currently used by the model using this endpoint.</p>"""
    creation_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The creation date and time of the endpoint.</p>"""
    last_modified_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The date and time that the endpoint was last modified.</p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).</p>"""
    desired_data_access_role_arn: NotRequired[
        "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p>Data access role ARN to use in case the new model is encrypted with a customer KMS key.</p>"""
    flywheel_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointProperties) -> dict:
    out: dict = {}
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "status" in value:
        import aws_sdk_comprehend.types.endpoint_status

        out["Status"] = aws_sdk_comprehend.types.endpoint_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "desired_model_arn" in value:
        out["DesiredModelArn"] = value["desired_model_arn"]
    if "desired_inference_units" in value:
        out["DesiredInferenceUnits"] = value["desired_inference_units"]
    if "current_inference_units" in value:
        out["CurrentInferenceUnits"] = value["current_inference_units"]
    if "creation_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "desired_data_access_role_arn" in value:
        out["DesiredDataAccessRoleArn"] = value["desired_data_access_role_arn"]
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointProperties:
    out: EndpointProperties = {}  # type: ignore[typeddict-item]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    if "Status" in data:
        import aws_sdk_comprehend.types.endpoint_status

        out["status"] = (
            aws_sdk_comprehend.types.endpoint_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "DesiredModelArn" in data:
        out["desired_model_arn"] = data["DesiredModelArn"]
    if "DesiredInferenceUnits" in data:
        out["desired_inference_units"] = data["DesiredInferenceUnits"]
    if "CurrentInferenceUnits" in data:
        out["current_inference_units"] = data["CurrentInferenceUnits"]
    if "CreationTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "DesiredDataAccessRoleArn" in data:
        out["desired_data_access_role_arn"] = data["DesiredDataAccessRoleArn"]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
