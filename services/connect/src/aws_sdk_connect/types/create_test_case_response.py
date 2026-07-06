"""Generated from Smithy shape ``com.amazonaws.connect#CreateTestCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.test_case_id


class CreateTestCaseResponse(TypedDict, closed=True):
    test_case_id: NotRequired["aws_sdk_connect.types.test_case_id.TestCaseId"]
    """<p>The identifier of the test.</p>"""
    test_case_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTestCaseResponse) -> dict:
    out: dict = {}
    if "test_case_id" in value:
        out["TestCaseId"] = value["test_case_id"]
    if "test_case_arn" in value:
        out["TestCaseArn"] = value["test_case_arn"]
    return out


def deserialize_json(data: dict) -> CreateTestCaseResponse:
    out: CreateTestCaseResponse = {}  # type: ignore[typeddict-item]
    if "TestCaseId" in data:
        out["test_case_id"] = data["TestCaseId"]
    if "TestCaseArn" in data:
        out["test_case_arn"] = data["TestCaseArn"]
    return out
