"""Generated from Smithy shape ``com.amazonaws.workmail#TestAvailabilityConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.boolean
    import capo_workmail.types.string


class TestAvailabilityConfigurationResponse(TypedDict, closed=True):
    test_passed: "capo_workmail.types.boolean.Boolean"
    """<p>Boolean indicating whether the test passed or failed.</p>"""
    failure_reason: NotRequired["capo_workmail.types.string.String"]
    """<p>String containing the reason for a failed test if <code>TestPassed</code> is false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestAvailabilityConfigurationResponse) -> dict:
    out: dict = {}
    out["TestPassed"] = value.get("test_passed", False)
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestAvailabilityConfigurationResponse:
    out: TestAvailabilityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "TestPassed" in data:
        out["test_passed"] = data["TestPassed"]
    else:
        out["test_passed"] = False
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
