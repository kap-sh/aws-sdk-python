"""Generated from Smithy shape ``com.amazonaws.connect#ListTestCasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.test_case_summary_list


class ListTestCasesResponse(TypedDict, closed=True):
    test_case_summary_list: NotRequired[
        "aws_sdk_connect.types.test_case_summary_list.TestCaseSummaryList"
    ]
    """<p>Information about the tests.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestCasesResponse) -> dict:
    out: dict = {}
    if "test_case_summary_list" in value:
        import aws_sdk_connect.types.test_case_summary_list

        out["TestCaseSummaryList"] = (
            aws_sdk_connect.types.test_case_summary_list.serialize_json(
                value["test_case_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestCasesResponse:
    out: ListTestCasesResponse = {}  # type: ignore[typeddict-item]
    if "TestCaseSummaryList" in data:
        import aws_sdk_connect.types.test_case_summary_list

        out["test_case_summary_list"] = (
            aws_sdk_connect.types.test_case_summary_list.deserialize_json(
                data["TestCaseSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
