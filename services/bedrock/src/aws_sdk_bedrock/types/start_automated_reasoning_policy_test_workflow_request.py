"""Generated from Smithy shape ``com.amazonaws.bedrock#StartAutomatedReasoningPolicyTestWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id_list
    import aws_sdk_bedrock.types.idempotency_token


class StartAutomatedReasoningPolicyTestWorkflowRequest(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to test.</p>"""
    build_workflow_id: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The build workflow identifier. The build workflow must show a <code>COMPLETED</code> status before running tests.</p>"""
    test_case_ids: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id_list.AutomatedReasoningPolicyTestCaseIdList"
    ]
    """<p>The list of test identifiers to run. If not provided, all tests for the policy are run.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAutomatedReasoningPolicyTestWorkflowRequest) -> dict:
    out: dict = {}
    if "test_case_ids" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id_list

        out["testCaseIds"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id_list.serialize_json(
                value["test_case_ids"]
            )
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> StartAutomatedReasoningPolicyTestWorkflowRequest:
    out: StartAutomatedReasoningPolicyTestWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "testCaseIds" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id_list

        out["test_case_ids"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id_list.deserialize_json(
                data["testCaseIds"]
            )
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
