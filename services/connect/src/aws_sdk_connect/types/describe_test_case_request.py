"""Generated from Smithy shape ``com.amazonaws.connect#DescribeTestCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id_or_arn
    import aws_sdk_connect.types.test_case_id
    import aws_sdk_connect.types.test_case_status


class DescribeTestCaseRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Amazon Connect instance.</p>"""
    test_case_id: "aws_sdk_connect.types.test_case_id.TestCaseId"
    """<p>The identifier of the test case.</p>"""
    status: NotRequired["aws_sdk_connect.types.test_case_status.TestCaseStatus"]
    """<p>The status of the test case version to retrieve. If not specified, returns the published version if available, otherwise returns the saved version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTestCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTestCaseRequest:
    out: DescribeTestCaseRequest = {}  # type: ignore[typeddict-item]
    return out
