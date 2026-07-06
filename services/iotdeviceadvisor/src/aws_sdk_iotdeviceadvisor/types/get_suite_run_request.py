"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetSuiteRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.uuid


class GetSuiteRunRequest(TypedDict, closed=True):
    suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite definition ID for the test suite run.</p>"""
    suite_run_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite run ID for the test suite run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSuiteRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSuiteRunRequest:
    out: GetSuiteRunRequest = {}  # type: ignore[typeddict-item]
    return out
