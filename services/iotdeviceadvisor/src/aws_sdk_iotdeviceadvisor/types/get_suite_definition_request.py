"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#GetSuiteDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.suite_definition_version
    import aws_sdk_iotdeviceadvisor.types.uuid


class GetSuiteDefinitionRequest(TypedDict):
    suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite definition ID of the test suite to get.</p>"""
    suite_definition_version: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
    ]
    """<p>Suite definition version of the test suite to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSuiteDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSuiteDefinitionRequest:
    out: GetSuiteDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
