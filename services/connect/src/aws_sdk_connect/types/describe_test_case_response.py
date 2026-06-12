"""Generated from Smithy shape ``com.amazonaws.connect#DescribeTestCaseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.test_case


class DescribeTestCaseResponse(TypedDict):
    test_case: NotRequired["aws_sdk_connect.types.test_case.TestCase"]
    """<p>The test case object containing all test case information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTestCaseResponse) -> dict:
    out: dict = {}
    if "test_case" in value:
        import aws_sdk_connect.types.test_case

        out["TestCase"] = aws_sdk_connect.types.test_case.serialize_json(
            value["test_case"]
        )
    return out


def deserialize_json(data: dict) -> DescribeTestCaseResponse:
    out: DescribeTestCaseResponse = {}  # type: ignore[typeddict-item]
    if "TestCase" in data:
        import aws_sdk_connect.types.test_case

        out["test_case"] = aws_sdk_connect.types.test_case.deserialize_json(
            data["TestCase"]
        )
    return out
