"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateCustomModelDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_arn
    import aws_sdk_bedrock.types.custom_model_deployment_description
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.model_deployment_name
    import aws_sdk_bedrock.types.tag_list


class CreateCustomModelDeploymentRequest(TypedDict):
    model_deployment_name: (
        "aws_sdk_bedrock.types.model_deployment_name.ModelDeploymentName"
    )
    """<p>The name for the custom model deployment. The name must be unique within your Amazon Web Services account and Region.</p>"""
    model_arn: "aws_sdk_bedrock.types.custom_model_arn.CustomModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model to deploy for on-demand inference. The custom model must be in the <code>Active</code> state.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.custom_model_deployment_description.CustomModelDeploymentDescription"
    ]
    """<p>A description for the custom model deployment to help you identify its purpose.</p>"""
    tags: NotRequired["aws_sdk_bedrock.types.tag_list.TagList"]
    """<p>Tags to assign to the custom model deployment. You can use tags to organize and track your Amazon Web Services resources for cost allocation and management purposes.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-idempotency.html\">Ensuring idempotency</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomModelDeploymentRequest) -> dict:
    out: dict = {}
    out["modelDeploymentName"] = value["model_deployment_name"]
    out["modelArn"] = value["model_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateCustomModelDeploymentRequest:
    out: CreateCustomModelDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "modelDeploymentName" in data:
        out["model_deployment_name"] = data["modelDeploymentName"]
    else:
        raise DeserializationError(
            "CreateCustomModelDeploymentRequest.model_deployment_name required"
        )
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "CreateCustomModelDeploymentRequest.model_arn required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.deserialize_json(data["tags"])
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
