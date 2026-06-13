"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestCase``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_result
    import aws_sdk_bedrock.types.automated_reasoning_check_translation_confidence
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_guard_content
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_query_content
    import aws_sdk_bedrock.types.timestamp


class AutomatedReasoningPolicyTestCase(TypedDict):
    test_case_id: "aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId"
    """<p>The unique identifier of the test.</p>"""
    guard_content: "aws_sdk_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent"
    """<p>The output content to be validated by the policy, typically representing a foundation model response.</p>"""
    query_content: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
    ]
    """<p>The input query or prompt that generated the content. This provides context for the validation.</p>"""
    expected_aggregated_findings_result: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult"
    ]
    """<p>The expected result of the Automated Reasoning check for this test.</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the test was created.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the test was last updated.</p>"""
    confidence_threshold: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
    ]
    """<p>The minimum confidence level for logic validation. Content meeting this threshold is considered high-confidence and can be validated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTestCase) -> dict:
    out: dict = {}
    out["testCaseId"] = value["test_case_id"]
    out["guardContent"] = value["guard_content"]
    if "query_content" in value:
        out["queryContent"] = value["query_content"]
    if "expected_aggregated_findings_result" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_result

        out["expectedAggregatedFindingsResult"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_result.serialize_json(
                value["expected_aggregated_findings_result"]
            )
        )
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    if "confidence_threshold" in value:
        out["confidenceThreshold"] = value["confidence_threshold"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyTestCase:
    out: AutomatedReasoningPolicyTestCase = {}  # type: ignore[typeddict-item]
    if "testCaseId" in data:
        out["test_case_id"] = data["testCaseId"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyTestCase.test_case_id required"
        )
    if "guardContent" in data:
        out["guard_content"] = data["guardContent"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyTestCase.guard_content required"
        )
    if "queryContent" in data:
        out["query_content"] = data["queryContent"]
    if "expectedAggregatedFindingsResult" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_result

        out["expected_aggregated_findings_result"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_result.deserialize_json(
                data["expectedAggregatedFindingsResult"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyTestCase.created_at required"
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyTestCase.updated_at required"
        )
    if "confidenceThreshold" in data:
        out["confidence_threshold"] = data["confidenceThreshold"]
    return out
