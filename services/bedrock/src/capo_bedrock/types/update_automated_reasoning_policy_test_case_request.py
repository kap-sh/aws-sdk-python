"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateAutomatedReasoningPolicyTestCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_result
    import capo_bedrock.types.automated_reasoning_check_translation_confidence
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_test_case_id
    import capo_bedrock.types.automated_reasoning_policy_test_guard_content
    import capo_bedrock.types.automated_reasoning_policy_test_query_content
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.timestamp


class UpdateAutomatedReasoningPolicyTestCaseRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>"""
    test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId"
    """<p>The unique identifier of the test to update.</p>"""
    guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent"
    """<p>The updated content to be validated by the Automated Reasoning policy.</p>"""
    query_content: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
    ]
    """<p>The updated input query or prompt that generated the content.</p>"""
    last_updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the test was last updated. This is used as a concurrency token to prevent conflicting modifications.</p>"""
    expected_aggregated_findings_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult"
    """<p>The updated expected result of the Automated Reasoning check.</p>"""
    confidence_threshold: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
    ]
    """<p>The updated minimum confidence level for logic validation. If null is provided, the threshold will be removed.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomatedReasoningPolicyTestCaseRequest) -> dict:
    out: dict = {}
    out["guardContent"] = value["guard_content"]
    if "query_content" in value:
        out["queryContent"] = value["query_content"]
    import capo_bedrock.types.timestamp

    out["lastUpdatedAt"] = capo_bedrock.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    import capo_bedrock.types.automated_reasoning_check_result

    out["expectedAggregatedFindingsResult"] = (
        capo_bedrock.types.automated_reasoning_check_result.serialize_json(
            value["expected_aggregated_findings_result"]
        )
    )
    if "confidence_threshold" in value:
        out["confidenceThreshold"] = value["confidence_threshold"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpdateAutomatedReasoningPolicyTestCaseRequest:
    out: UpdateAutomatedReasoningPolicyTestCaseRequest = {}  # type: ignore[typeddict-item]
    if "guardContent" in data:
        out["guard_content"] = data["guardContent"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyTestCaseRequest.guard_content required"
        )
    if "queryContent" in data:
        out["query_content"] = data["queryContent"]
    if "lastUpdatedAt" in data:
        import capo_bedrock.types.timestamp

        out["last_updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyTestCaseRequest.last_updated_at required"
        )
    if "expectedAggregatedFindingsResult" in data:
        import capo_bedrock.types.automated_reasoning_check_result

        out["expected_aggregated_findings_result"] = (
            capo_bedrock.types.automated_reasoning_check_result.deserialize_json(
                data["expectedAggregatedFindingsResult"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyTestCaseRequest.expected_aggregated_findings_result required"
        )
    if "confidenceThreshold" in data:
        out["confidence_threshold"] = data["confidenceThreshold"]
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
