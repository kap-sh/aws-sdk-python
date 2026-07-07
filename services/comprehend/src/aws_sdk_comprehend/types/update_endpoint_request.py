"""Generated from Smithy shape ``com.amazonaws.comprehend#UpdateEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_endpoint_arn
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.comprehend_model_arn
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.inference_units_integer


class UpdateEndpointRequest(TypedDict, closed=True):
    endpoint_arn: (
        "aws_sdk_comprehend.types.comprehend_endpoint_arn.ComprehendEndpointArn"
    )
    """<p>The Amazon Resource Number (ARN) of the endpoint being updated.</p>"""
    desired_model_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The ARN of the new model to use when updating an existing endpoint.</p>"""
    desired_inference_units: NotRequired[
        "aws_sdk_comprehend.types.inference_units_integer.InferenceUnitsInteger"
    ]
    """<p> The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.</p>"""
    desired_data_access_role_arn: NotRequired[
        "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p>Data access role ARN to use in case the new model is encrypted with a customer CMK.</p>"""
    flywheel_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointArn"] = value["endpoint_arn"]
    if "desired_model_arn" in value:
        out["DesiredModelArn"] = value["desired_model_arn"]
    if "desired_inference_units" in value:
        out["DesiredInferenceUnits"] = value["desired_inference_units"]
    if "desired_data_access_role_arn" in value:
        out["DesiredDataAccessRoleArn"] = value["desired_data_access_role_arn"]
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointRequest:
    out: UpdateEndpointRequest = {}  # type: ignore[typeddict-item]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    else:
        raise DeserializationError("UpdateEndpointRequest.endpoint_arn required")
    if "DesiredModelArn" in data:
        out["desired_model_arn"] = data["DesiredModelArn"]
    if "DesiredInferenceUnits" in data:
        out["desired_inference_units"] = data["DesiredInferenceUnits"]
    if "DesiredDataAccessRoleArn" in data:
        out["desired_data_access_role_arn"] = data["DesiredDataAccessRoleArn"]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
