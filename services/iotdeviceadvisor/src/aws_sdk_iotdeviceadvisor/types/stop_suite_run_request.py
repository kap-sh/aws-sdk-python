"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#StopSuiteRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.uuid


class StopSuiteRunRequest(TypedDict):
    suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite definition ID of the test suite run to be stopped.</p>"""
    suite_run_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite run ID of the test suite run to be stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopSuiteRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopSuiteRunRequest:
    out: StopSuiteRunRequest = {}  # type: ignore[typeddict-item]
    return out
