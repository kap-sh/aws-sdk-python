"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPolicyTestResultsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_list
    import aws_sdk_bedrock.types.pagination_token


class ListAutomatedReasoningPolicyTestResultsResponse(TypedDict):
    test_results: "aws_sdk_bedrock.types.automated_reasoning_policy_test_list.AutomatedReasoningPolicyTestList"
    """<p>A list of test results, each containing information about how the policy performed on specific test scenarios.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>A pagination token to use in subsequent requests to retrieve additional test results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPolicyTestResultsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_list

    out["testResults"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_test_list.serialize_json(
            value["test_results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPolicyTestResultsResponse:
    out: ListAutomatedReasoningPolicyTestResultsResponse = {}  # type: ignore[typeddict-item]
    if "testResults" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_list

        out["test_results"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_list.deserialize_json(
                data["testResults"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutomatedReasoningPolicyTestResultsResponse.test_results required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
