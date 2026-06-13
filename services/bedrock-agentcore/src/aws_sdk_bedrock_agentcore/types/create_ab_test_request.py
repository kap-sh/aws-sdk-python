"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreateABTestRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.ab_test_description
    import aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config
    import aws_sdk_bedrock_agentcore.types.ab_test_name
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.gateway_arn
    import aws_sdk_bedrock_agentcore.types.gateway_filter
    import aws_sdk_bedrock_agentcore.types.role_arn
    import aws_sdk_bedrock_agentcore.types.variant_list

class CreateABTestRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore.types.ab_test_name.ABTestName"
    """<p>The name of the A/B test. Must be unique within your account.</p>"""
    description: NotRequired["aws_sdk_bedrock_agentcore.types.ab_test_description.ABTestDescription"]
    """<p>The description of the A/B test.</p>"""
    gateway_arn: "aws_sdk_bedrock_agentcore.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.</p>"""
    variants: "aws_sdk_bedrock_agentcore.types.variant_list.VariantList"
    """<p>The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.</p>"""
    gateway_filter: NotRequired["aws_sdk_bedrock_agentcore.types.gateway_filter.GatewayFilter"]
    """<p>Optional filter to restrict which gateway target paths are included in the A/B test.</p>"""
    evaluation_config: "aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"
    """<p>The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.</p>"""
    role_arn: "aws_sdk_bedrock_agentcore.types.role_arn.RoleArn"
    """<p>The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.</p>"""
    enable_on_create: NotRequired["bool"]
    """<p>Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateABTestRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["gatewayArn"] = value["gateway_arn"]
    import aws_sdk_bedrock_agentcore.types.variant_list
    out["variants"] = aws_sdk_bedrock_agentcore.types.variant_list.serialize_json(value["variants"])
    if "gateway_filter" in value:
        import aws_sdk_bedrock_agentcore.types.gateway_filter
        out["gatewayFilter"] = aws_sdk_bedrock_agentcore.types.gateway_filter.serialize_json(value["gateway_filter"])
    import aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config
    out["evaluationConfig"] = aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.serialize_json(value["evaluation_config"])
    out["roleArn"] = value["role_arn"]
    if "enable_on_create" in value:
        out["enableOnCreate"] = value["enable_on_create"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateABTestRequest:
    out: CreateABTestRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateABTestRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("CreateABTestRequest.gateway_arn required")
    if "variants" in data:
        import aws_sdk_bedrock_agentcore.types.variant_list
        out["variants"] = aws_sdk_bedrock_agentcore.types.variant_list.deserialize_json(data["variants"])
    else:
        raise DeserializationError("CreateABTestRequest.variants required")
    if "gatewayFilter" in data:
        import aws_sdk_bedrock_agentcore.types.gateway_filter
        out["gateway_filter"] = aws_sdk_bedrock_agentcore.types.gateway_filter.deserialize_json(data["gatewayFilter"])
    if "evaluationConfig" in data:
        import aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config
        out["evaluation_config"] = aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.deserialize_json(data["evaluationConfig"])
    else:
        raise DeserializationError("CreateABTestRequest.evaluation_config required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateABTestRequest.role_arn required")
    if "enableOnCreate" in data:
        out["enable_on_create"] = data["enableOnCreate"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out