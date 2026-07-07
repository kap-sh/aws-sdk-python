"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyTestResultResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_result


class GetAutomatedReasoningPolicyTestResultResponse(TypedDict, closed=True):
    test_result: "aws_sdk_bedrock.types.automated_reasoning_policy_test_result.AutomatedReasoningPolicyTestResult"
    """<p>The test result containing validation findings, execution status, and detailed analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyTestResultResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_result

    out["testResult"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_test_result.serialize_json(
            value["test_result"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyTestResultResponse:
    out: GetAutomatedReasoningPolicyTestResultResponse = {}  # type: ignore[typeddict-item]
    if "testResult" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_result

        out["test_result"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_result.deserialize_json(
                data["testResult"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyTestResultResponse.test_result required"
        )
    return out
