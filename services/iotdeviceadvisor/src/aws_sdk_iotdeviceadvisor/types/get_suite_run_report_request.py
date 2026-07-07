"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetSuiteRunReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.uuid


class GetSuiteRunReportRequest(TypedDict, closed=True):
    suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite definition ID of the test suite.</p>"""
    suite_run_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite run ID of the test suite run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSuiteRunReportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSuiteRunReportRequest:
    out: GetSuiteRunReportRequest = {}  # type: ignore[typeddict-item]
    return out
