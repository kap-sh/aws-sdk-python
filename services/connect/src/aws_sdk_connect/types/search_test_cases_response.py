"""Generated from Smithy shape ``com.amazonaws.connect#SearchTestCasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.approximate_total_count
    import aws_sdk_connect.types.next_token2500
    import aws_sdk_connect.types.test_case_search_summary_list


class SearchTestCasesResponse(TypedDict):
    test_cases: NotRequired[
        "aws_sdk_connect.types.test_case_search_summary_list.TestCaseSearchSummaryList"
    ]
    """<p>Information about the test cases.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "aws_sdk_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of test cases which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchTestCasesResponse) -> dict:
    out: dict = {}
    if "test_cases" in value:
        import aws_sdk_connect.types.test_case_search_summary_list

        out["TestCases"] = (
            aws_sdk_connect.types.test_case_search_summary_list.serialize_json(
                value["test_cases"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchTestCasesResponse:
    out: SearchTestCasesResponse = {}  # type: ignore[typeddict-item]
    if "TestCases" in data:
        import aws_sdk_connect.types.test_case_search_summary_list

        out["test_cases"] = (
            aws_sdk_connect.types.test_case_search_summary_list.deserialize_json(
                data["TestCases"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
