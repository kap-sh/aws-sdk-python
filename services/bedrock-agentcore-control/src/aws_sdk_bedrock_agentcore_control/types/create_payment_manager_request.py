"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePaymentManagerRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_name
    import aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type
    import aws_sdk_bedrock_agentcore_control.types.payments_description
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map

class CreatePaymentManagerRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.payment_manager_name.PaymentManagerName"
    """<p>The name of the payment manager.</p>"""
    description: NotRequired["aws_sdk_bedrock_agentcore_control.types.payments_description.PaymentsDescription"]
    """<p>A description of the payment manager.</p>"""
    authorizer_type: "aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
    """<p>The type of authorizer to use for the payment manager.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>"""
    authorizer_configuration: NotRequired["aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"]
    """<p>The authorizer configuration for the payment manager.</p>"""
    role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the payment manager assumes to access resources on your behalf.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to the payment manager.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentManagerRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type
    out["authorizerType"] = aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.serialize_json(value["authorizer_type"])
    if "authorizer_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
        out["authorizerConfiguration"] = aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(value["authorizer_configuration"])
    out["roleArn"] = value["role_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePaymentManagerRequest:
    out: CreatePaymentManagerRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePaymentManagerRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "authorizerType" in data:
        import aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type
        out["authorizer_type"] = aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.deserialize_json(data["authorizerType"])
    else:
        raise DeserializationError("CreatePaymentManagerRequest.authorizer_type required")
    if "authorizerConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
        out["authorizer_configuration"] = aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(data["authorizerConfiguration"])
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreatePaymentManagerRequest.role_arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map
        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(data["tags"])
    return out