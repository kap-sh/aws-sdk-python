"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.client_request_token_string
    import aws_sdk_comprehend.types.comprehend_endpoint_name
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.comprehend_model_arn
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.inference_units_integer
    import aws_sdk_comprehend.types.tag_list


class CreateEndpointRequest(TypedDict):
    endpoint_name: (
        "aws_sdk_comprehend.types.comprehend_endpoint_name.ComprehendEndpointName"
    )
    """<p>This is the descriptive suffix that becomes part of the <code>EndpointArn</code> used for all subsequent requests to this resource. </p>"""
    model_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the model to which the endpoint will be attached.</p>"""
    desired_inference_units: (
        "aws_sdk_comprehend.types.inference_units_integer.InferenceUnitsInteger"
    )
    """<p> The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>An idempotency token provided by the customer. If this token matches a previous endpoint creation request, Amazon Comprehend will not return a <code>ResourceInUseException</code>. </p>"""
    tags: NotRequired["aws_sdk_comprehend.types.tag_list.TagList"]
    """<p>Tags to associate with the endpoint. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with \"Sales\" as the key might be added to an endpoint to indicate its use by the sales department. </p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).</p>"""
    flywheel_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel to which the endpoint will be attached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointName"] = value["endpoint_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    out["DesiredInferenceUnits"] = value["desired_inference_units"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_comprehend.types.tag_list

        out["Tags"] = aws_sdk_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointRequest:
    out: CreateEndpointRequest = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    else:
        raise DeserializationError("CreateEndpointRequest.endpoint_name required")
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "DesiredInferenceUnits" in data:
        out["desired_inference_units"] = data["DesiredInferenceUnits"]
    else:
        raise DeserializationError(
            "CreateEndpointRequest.desired_inference_units required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_comprehend.types.tag_list

        out["tags"] = aws_sdk_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
