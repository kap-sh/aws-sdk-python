"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UpdateABTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.ab_test_description
    import aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config
    import aws_sdk_bedrock_agentcore.types.ab_test_execution_status
    import aws_sdk_bedrock_agentcore.types.ab_test_id
    import aws_sdk_bedrock_agentcore.types.ab_test_name
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.gateway_filter
    import aws_sdk_bedrock_agentcore.types.role_arn
    import aws_sdk_bedrock_agentcore.types.variant_list


class UpdateABTestRequest(TypedDict, closed=True):
    ab_test_id: "aws_sdk_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the A/B test to update.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""
    name: NotRequired["aws_sdk_bedrock_agentcore.types.ab_test_name.ABTestName"]
    """<p>The updated name of the A/B test.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore.types.ab_test_description.ABTestDescription"
    ]
    """<p>The updated description of the A/B test.</p>"""
    variants: NotRequired["aws_sdk_bedrock_agentcore.types.variant_list.VariantList"]
    """<p>The updated list of variants.</p>"""
    gateway_filter: NotRequired[
        "aws_sdk_bedrock_agentcore.types.gateway_filter.GatewayFilter"
    ]
    """<p>The updated gateway filter.</p>"""
    evaluation_config: NotRequired[
        "aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"
    ]
    """<p>The updated evaluation configuration.</p>"""
    role_arn: NotRequired["aws_sdk_bedrock_agentcore.types.role_arn.RoleArn"]
    """<p>The updated IAM role ARN.</p>"""
    execution_status: NotRequired[
        "aws_sdk_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
    ]
    """<p>The updated execution status to enable or disable the A/B test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateABTestRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "variants" in value:
        import aws_sdk_bedrock_agentcore.types.variant_list

        out["variants"] = aws_sdk_bedrock_agentcore.types.variant_list.serialize_json(
            value["variants"]
        )
    if "gateway_filter" in value:
        import aws_sdk_bedrock_agentcore.types.gateway_filter

        out["gatewayFilter"] = (
            aws_sdk_bedrock_agentcore.types.gateway_filter.serialize_json(
                value["gateway_filter"]
            )
        )
    if "evaluation_config" in value:
        import aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config

        out["evaluationConfig"] = (
            aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.serialize_json(
                value["evaluation_config"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "execution_status" in value:
        import aws_sdk_bedrock_agentcore.types.ab_test_execution_status

        out["executionStatus"] = (
            aws_sdk_bedrock_agentcore.types.ab_test_execution_status.serialize_json(
                value["execution_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateABTestRequest:
    out: UpdateABTestRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "variants" in data:
        import aws_sdk_bedrock_agentcore.types.variant_list

        out["variants"] = aws_sdk_bedrock_agentcore.types.variant_list.deserialize_json(
            data["variants"]
        )
    if "gatewayFilter" in data:
        import aws_sdk_bedrock_agentcore.types.gateway_filter

        out["gateway_filter"] = (
            aws_sdk_bedrock_agentcore.types.gateway_filter.deserialize_json(
                data["gatewayFilter"]
            )
        )
    if "evaluationConfig" in data:
        import aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config

        out["evaluation_config"] = (
            aws_sdk_bedrock_agentcore.types.ab_test_evaluation_config.deserialize_json(
                data["evaluationConfig"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "executionStatus" in data:
        import aws_sdk_bedrock_agentcore.types.ab_test_execution_status

        out["execution_status"] = (
            aws_sdk_bedrock_agentcore.types.ab_test_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    return out
