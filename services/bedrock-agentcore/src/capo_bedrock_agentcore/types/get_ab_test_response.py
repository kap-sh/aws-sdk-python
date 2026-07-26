"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetABTestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.ab_test_arn
    import capo_bedrock_agentcore.types.ab_test_description
    import capo_bedrock_agentcore.types.ab_test_evaluation_config
    import capo_bedrock_agentcore.types.ab_test_execution_status
    import capo_bedrock_agentcore.types.ab_test_id
    import capo_bedrock_agentcore.types.ab_test_name
    import capo_bedrock_agentcore.types.ab_test_results
    import capo_bedrock_agentcore.types.ab_test_status
    import capo_bedrock_agentcore.types.error_details_list
    import capo_bedrock_agentcore.types.gateway_arn
    import capo_bedrock_agentcore.types.gateway_filter
    import capo_bedrock_agentcore.types.role_arn
    import capo_bedrock_agentcore.types.variant_list


class GetABTestResponse(TypedDict, closed=True):
    ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the A/B test.</p>"""
    ab_test_arn: "capo_bedrock_agentcore.types.ab_test_arn.ABTestArn"
    """<p>The Amazon Resource Name (ARN) of the A/B test.</p>"""
    name: "capo_bedrock_agentcore.types.ab_test_name.ABTestName"
    """<p>The name of the A/B test.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
    ]
    """<p>The description of the A/B test.</p>"""
    status: "capo_bedrock_agentcore.types.ab_test_status.ABTestStatus"
    """<p>The current status of the A/B test.</p>"""
    execution_status: (
        "capo_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
    )
    """<p>The execution status indicating whether the A/B test is currently running.</p>"""
    gateway_arn: "capo_bedrock_agentcore.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway used for traffic splitting.</p>"""
    variants: "capo_bedrock_agentcore.types.variant_list.VariantList"
    """<p>The list of variants in the A/B test.</p>"""
    gateway_filter: NotRequired[
        "capo_bedrock_agentcore.types.gateway_filter.GatewayFilter"
    ]
    """<p>The gateway filter restricting which target paths are included.</p>"""
    evaluation_config: (
        "capo_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"
    )
    """<p>The evaluation configuration for measuring variant performance.</p>"""
    role_arn: NotRequired["capo_bedrock_agentcore.types.role_arn.RoleArn"]
    """<p>The IAM role ARN used by the A/B test.</p>"""
    current_run_id: NotRequired["str"]
    """<p>The identifier of the current run of the A/B test.</p>"""
    error_details: NotRequired[
        "capo_bedrock_agentcore.types.error_details_list.ErrorDetailsList"
    ]
    """<p>The error details if the A/B test encountered failures.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the A/B test was started.</p>"""
    stopped_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the A/B test was stopped.</p>"""
    max_duration_expires_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the A/B test will automatically expire.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the A/B test was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the A/B test was last updated.</p>"""
    results: NotRequired["capo_bedrock_agentcore.types.ab_test_results.ABTestResults"]
    """<p>The statistical results of the A/B test, including per-evaluator metrics and significance analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetABTestResponse) -> dict:
    out: dict = {}
    out["abTestId"] = value["ab_test_id"]
    out["abTestArn"] = value["ab_test_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore.types.ab_test_status

    out["status"] = capo_bedrock_agentcore.types.ab_test_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore.types.ab_test_execution_status

    out["executionStatus"] = (
        capo_bedrock_agentcore.types.ab_test_execution_status.serialize_json(
            value["execution_status"]
        )
    )
    out["gatewayArn"] = value["gateway_arn"]
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
    import capo_bedrock_agentcore.types.ab_test_evaluation_config

    out["evaluationConfig"] = (
        capo_bedrock_agentcore.types.ab_test_evaluation_config.serialize_json(
            value["evaluation_config"]
        )
    )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "current_run_id" in value:
        out["currentRunId"] = value["current_run_id"]
    if "error_details" in value:
        import capo_bedrock_agentcore.types.error_details_list

        out["errorDetails"] = (
            capo_bedrock_agentcore.types.error_details_list.serialize_json(
                value["error_details"]
            )
        )
    if "started_at" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["startedAt"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["started_at"]
            )
        )
    if "stopped_at" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["stoppedAt"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["stopped_at"]
            )
        )
    if "max_duration_expires_at" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["maxDurationExpiresAt"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["max_duration_expires_at"]
            )
        )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["createdAt"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["updatedAt"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "results" in value:
        import capo_bedrock_agentcore.types.ab_test_results

        out["results"] = capo_bedrock_agentcore.types.ab_test_results.serialize_json(
            value["results"]
        )
    return out


def deserialize_json(data: dict) -> GetABTestResponse:
    out: GetABTestResponse = {}  # type: ignore[typeddict-item]
    if "abTestId" in data:
        out["ab_test_id"] = data["abTestId"]
    else:
        raise DeserializationError("GetABTestResponse.ab_test_id required")
    if "abTestArn" in data:
        out["ab_test_arn"] = data["abTestArn"]
    else:
        raise DeserializationError("GetABTestResponse.ab_test_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetABTestResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import capo_bedrock_agentcore.types.ab_test_status

        out["status"] = capo_bedrock_agentcore.types.ab_test_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetABTestResponse.status required")
    if "executionStatus" in data:
        import capo_bedrock_agentcore.types.ab_test_execution_status

        out["execution_status"] = (
            capo_bedrock_agentcore.types.ab_test_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError("GetABTestResponse.execution_status required")
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("GetABTestResponse.gateway_arn required")
    if "variants" in data:
        import capo_bedrock_agentcore.types.variant_list

        out["variants"] = capo_bedrock_agentcore.types.variant_list.deserialize_json(
            data["variants"]
        )
    else:
        raise DeserializationError("GetABTestResponse.variants required")
    if "gatewayFilter" in data:
        import capo_bedrock_agentcore.types.gateway_filter

        out["gateway_filter"] = (
            capo_bedrock_agentcore.types.gateway_filter.deserialize_json(
                data["gatewayFilter"]
            )
        )
    if "evaluationConfig" in data:
        import capo_bedrock_agentcore.types.ab_test_evaluation_config

        out["evaluation_config"] = (
            capo_bedrock_agentcore.types.ab_test_evaluation_config.deserialize_json(
                data["evaluationConfig"]
            )
        )
    else:
        raise DeserializationError("GetABTestResponse.evaluation_config required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "currentRunId" in data:
        out["current_run_id"] = data["currentRunId"]
    if "errorDetails" in data:
        import capo_bedrock_agentcore.types.error_details_list

        out["error_details"] = (
            capo_bedrock_agentcore.types.error_details_list.deserialize_json(
                data["errorDetails"]
            )
        )
    if "startedAt" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["started_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["startedAt"]
            )
        )
    if "stoppedAt" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["stopped_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["stoppedAt"]
            )
        )
    if "maxDurationExpiresAt" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["max_duration_expires_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["maxDurationExpiresAt"]
            )
        )
    if "createdAt" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetABTestResponse.created_at required")
    if "updatedAt" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetABTestResponse.updated_at required")
    if "results" in data:
        import capo_bedrock_agentcore.types.ab_test_results

        out["results"] = capo_bedrock_agentcore.types.ab_test_results.deserialize_json(
            data["results"]
        )
    return out
