"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#UpdateSuiteDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.suite_definition_configuration
    import aws_sdk_iotdeviceadvisor.types.uuid


class UpdateSuiteDefinitionRequest(TypedDict, closed=True):
    suite_definition_id: "aws_sdk_iotdeviceadvisor.types.uuid.UUID"
    """<p>Suite definition ID of the test suite to be updated.</p>"""
    suite_definition_configuration: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.suite_definition_configuration.SuiteDefinitionConfiguration"
    ]
    """<p>Updates a Device Advisor test suite with suite definition configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSuiteDefinitionRequest) -> dict:
    out: dict = {}
    if "suite_definition_configuration" in value:
        import aws_sdk_iotdeviceadvisor.types.suite_definition_configuration

        out["suiteDefinitionConfiguration"] = (
            aws_sdk_iotdeviceadvisor.types.suite_definition_configuration.serialize_json(
                value["suite_definition_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSuiteDefinitionRequest:
    out: UpdateSuiteDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionConfiguration" in data:
        import aws_sdk_iotdeviceadvisor.types.suite_definition_configuration

        out["suite_definition_configuration"] = (
            aws_sdk_iotdeviceadvisor.types.suite_definition_configuration.deserialize_json(
                data["suiteDefinitionConfiguration"]
            )
        )
    return out
