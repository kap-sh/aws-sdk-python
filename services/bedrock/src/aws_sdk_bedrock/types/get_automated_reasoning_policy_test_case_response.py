"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyTestCaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case


class GetAutomatedReasoningPolicyTestCaseResponse(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy that contains the test.</p>"""
    test_case: "aws_sdk_bedrock.types.automated_reasoning_policy_test_case.AutomatedReasoningPolicyTestCase"
    """<p>The test details including the content, query, expected result, and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyTestCaseResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case

    out["testCase"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_test_case.serialize_json(
            value["test_case"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyTestCaseResponse:
    out: GetAutomatedReasoningPolicyTestCaseResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyTestCaseResponse.policy_arn required"
        )
    if "testCase" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_case

        out["test_case"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_case.deserialize_json(
                data["testCase"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyTestCaseResponse.test_case required"
        )
    return out
