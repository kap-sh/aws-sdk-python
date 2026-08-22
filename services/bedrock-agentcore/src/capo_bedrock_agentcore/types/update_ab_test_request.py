"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UpdateABTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ab_test_description
    import capo_bedrock_agentcore.types.ab_test_evaluation_config
    import capo_bedrock_agentcore.types.ab_test_execution_status
    import capo_bedrock_agentcore.types.ab_test_id
    import capo_bedrock_agentcore.types.ab_test_name
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.gateway_filter
    import capo_bedrock_agentcore.types.role_arn
    import capo_bedrock_agentcore.types.variant_list


class UpdateABTestRequest(TypedDict, closed=True):
    ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the A/B test to update.</p>"""
    client_token: NotRequired["capo_bedrock_agentcore.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""
    name: NotRequired["capo_bedrock_agentcore.types.ab_test_name.ABTestName"]
    """<p>The updated name of the A/B test.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
    ]
    """<p>The updated description of the A/B test.</p>"""
    variants: NotRequired["capo_bedrock_agentcore.types.variant_list.VariantList"]
    """<p>The updated list of variants.</p>"""
    gateway_filter: NotRequired[
        "capo_bedrock_agentcore.types.gateway_filter.GatewayFilter"
    ]
    """<p>The updated gateway filter.</p>"""
    evaluation_config: NotRequired[
        "capo_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"
    ]
    """<p>The updated evaluation configuration.</p>"""
    role_arn: NotRequired["capo_bedrock_agentcore.types.role_arn.RoleArn"]
    """<p>The updated IAM role ARN.</p>"""
    execution_status: NotRequired[
        "capo_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
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
        import capo_bedrock_agentcore.types.variant_list

        out["variants"] = capo_bedrock_agentcore.types.variant_list.serialize_json(
            value["variants"]
        )
    if "gateway_filter" in value:
        import capo_bedrock_agentcore.types.gateway_filter

        out["gatewayFilter"] = (
            capo_bedrock_agentcore.types.gateway_filter.serialize_json(
                value["gateway_filter"]
            )
        )
    if "evaluation_config" in value:
        import capo_bedrock_agentcore.types.ab_test_evaluation_config

        out["evaluationConfig"] = (
            capo_bedrock_agentcore.types.ab_test_evaluation_config.serialize_json(
                value["evaluation_config"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "execution_status" in value:
        import capo_bedrock_agentcore.types.ab_test_execution_status

        out["executionStatus"] = (
            capo_bedrock_agentcore.types.ab_test_execution_status.serialize_json(
                value["execution_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateABTestRequest:
    out: UpdateABTestRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("variants") is not None:
        import capo_bedrock_agentcore.types.variant_list

        out["variants"] = capo_bedrock_agentcore.types.variant_list.deserialize_json(
            data["variants"]
        )
    if data.get("gatewayFilter") is not None:
        import capo_bedrock_agentcore.types.gateway_filter

        out["gateway_filter"] = (
            capo_bedrock_agentcore.types.gateway_filter.deserialize_json(
                data["gatewayFilter"]
            )
        )
    if data.get("evaluationConfig") is not None:
        import capo_bedrock_agentcore.types.ab_test_evaluation_config

        out["evaluation_config"] = (
            capo_bedrock_agentcore.types.ab_test_evaluation_config.deserialize_json(
                data["evaluationConfig"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("executionStatus") is not None:
        import capo_bedrock_agentcore.types.ab_test_execution_status

        out["execution_status"] = (
            capo_bedrock_agentcore.types.ab_test_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    return out
