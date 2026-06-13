"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPolicyTestCasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_list
    import aws_sdk_bedrock.types.pagination_token


class ListAutomatedReasoningPolicyTestCasesResponse(TypedDict):
    test_cases: "aws_sdk_bedrock.types.automated_reasoning_policy_test_case_list.AutomatedReasoningPolicyTestCaseList"
    """<p>A list of tests for the specified policy.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>The pagination token to use in a subsequent request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPolicyTestCasesResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_list

    out["testCases"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_test_case_list.serialize_json(
            value["test_cases"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPolicyTestCasesResponse:
    out: ListAutomatedReasoningPolicyTestCasesResponse = {}  # type: ignore[typeddict-item]
    if "testCases" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_list

        out["test_cases"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_test_case_list.deserialize_json(
                data["testCases"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutomatedReasoningPolicyTestCasesResponse.test_cases required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
