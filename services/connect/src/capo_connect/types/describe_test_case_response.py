"""Generated from Smithy shape ``com.amazonaws.connect#DescribeTestCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.test_case


class DescribeTestCaseResponse(TypedDict, closed=True):
    test_case: NotRequired["capo_connect.types.test_case.TestCase"]
    """<p>The test case object containing all test case information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTestCaseResponse) -> dict:
    out: dict = {}
    if "test_case" in value:
        import capo_connect.types.test_case

        out["TestCase"] = capo_connect.types.test_case.serialize_json(
            value["test_case"]
        )
    return out


def deserialize_json(data: dict) -> DescribeTestCaseResponse:
    out: DescribeTestCaseResponse = {}  # type: ignore[typeddict-item]
    if "TestCase" in data:
        import capo_connect.types.test_case

        out["test_case"] = capo_connect.types.test_case.deserialize_json(
            data["TestCase"]
        )
    return out
