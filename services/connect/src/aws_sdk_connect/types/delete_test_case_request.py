"""Generated from Smithy shape ``com.amazonaws.connect#DeleteTestCaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id_or_arn
    import aws_sdk_connect.types.test_case_id


class DeleteTestCaseRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Amazon Connect instance.</p>"""
    test_case_id: "aws_sdk_connect.types.test_case_id.TestCaseId"
    """<p>The identifier of the test case to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTestCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTestCaseRequest:
    out: DeleteTestCaseRequest = {}  # type: ignore[typeddict-item]
    return out
