"""Generated from Smithy shape ``com.amazonaws.sfn#MockErrorOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.sensitive_cause
    import aws_sdk_sfn.types.sensitive_error


class MockErrorOutput(TypedDict):
    error: NotRequired["aws_sdk_sfn.types.sensitive_error.SensitiveError"]
    """<p>A string denoting the error code of the exception thrown when invoking the tested state. This field is required if <code>mock.errorOutput</code> is specified.</p>"""
    cause: NotRequired["aws_sdk_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A string containing the cause of the exception thrown when executing the state's logic.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MockErrorOutput) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MockErrorOutput:
    out: MockErrorOutput = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "cause" in data:
        out["cause"] = data["cause"]
    return out
