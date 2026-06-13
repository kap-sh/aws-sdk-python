"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_finding_list
    import aws_sdk_bedrock.types.automated_reasoning_check_result
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_run_result
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_run_status
    import aws_sdk_bedrock.types.timestamp


class AutomatedReasoningPolicyTestResult(TypedDict):
    test_case: "aws_sdk_bedrock.types.automated_reasoning_policy_test_case.AutomatedReasoningPolicyTestCase"
    """<p>The test case that was executed, including the input content, expected results, and configuration parameters used during validation.</p>"""
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that was tested.</p>"""
    test_run_status: "aws_sdk_bedrock.types.automated_reasoning_policy_test_run_status.AutomatedReasoningPolicyTestRunStatus"
    """<p>The overall status of the test run (e.g., COMPLETED, FAILED, IN_PROGRESS).</p>"""
    test_findings: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_finding_list.AutomatedReasoningCheckFindingList"
    ]
    """<p>Detailed findings from the test run, including any issues, violations, or unexpected behaviors discovered.</p>"""
    test_run_result: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_test_run_result.AutomatedReasoningPolicyTestRunResult"
    ]
    """<p>The overall result of the test run, indicating whether the policy passed or failed validation.</p>"""
    aggregated_test_findings_result: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult"
    ]
    """<p>A summary of all test findings, aggregated to provide an overall assessment of policy quality and correctness.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the test results were last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTestResult) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case

    out["testCase"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_test_case.serialize_json(
            value["test_case"]
        )
    )
    out["policyArn"] = value["policy_arn"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_run_status

    out["testRunStatus"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_test_run_status.serialize_json(
            value["test_run_status"]
        )
    )
    if "test_findings" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_finding_list

        out["testFindings"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_finding_list.serialize_json(
                value["test_findings"]
            )
        )
    if "test_run_result" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_run_result

        out["testRunResult"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_run_result.serialize_json(
                value["test_run_result"]
            )
        )
    if "aggregated_test_findings_result" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_result

        out["aggregatedTestFindingsResult"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_result.serialize_json(
                value["aggregated_test_findings_result"]
            )
        )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyTestResult:
    out: AutomatedReasoningPolicyTestResult = {}  # type: ignore[typeddict-item]
    if "testCase" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_case

        out["test_case"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_case.deserialize_json(
                data["testCase"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyTestResult.test_case required"
        )
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyTestResult.policy_arn required"
        )
    if "testRunStatus" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_run_status

        out["test_run_status"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_run_status.deserialize_json(
                data["testRunStatus"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyTestResult.test_run_status required"
        )
    if "testFindings" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_finding_list

        out["test_findings"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_finding_list.deserialize_json(
                data["testFindings"]
            )
        )
    if "testRunResult" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_run_result

        out["test_run_result"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_run_result.deserialize_json(
                data["testRunResult"]
            )
        )
    if "aggregatedTestFindingsResult" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_result

        out["aggregated_test_findings_result"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_result.deserialize_json(
                data["aggregatedTestFindingsResult"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyTestResult.updated_at required"
        )
    return out
