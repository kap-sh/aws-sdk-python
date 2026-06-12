"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#SuiteDefinitionInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.device_under_test_list
    import aws_sdk_iotdeviceadvisor.types.intended_for_qualification_boolean
    import aws_sdk_iotdeviceadvisor.types.is_long_duration_test_boolean
    import aws_sdk_iotdeviceadvisor.types.protocol
    import aws_sdk_iotdeviceadvisor.types.suite_definition_name
    import aws_sdk_iotdeviceadvisor.types.timestamp
    import aws_sdk_iotdeviceadvisor.types.uuid


class SuiteDefinitionInformation(TypedDict):
    suite_definition_id: NotRequired["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Suite definition ID of the test suite.</p>"""
    suite_definition_name: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.suite_definition_name.SuiteDefinitionName"
    ]
    """<p>Suite name of the test suite.</p>"""
    default_devices: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.device_under_test_list.DeviceUnderTestList"
    ]
    """<p>Specifies the devices that are under test for the test suite.</p>"""
    intended_for_qualification: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.intended_for_qualification_boolean.IntendedForQualificationBoolean"
    ]
    """<p>Specifies if the test suite is intended for qualification.</p>"""
    is_long_duration_test: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.is_long_duration_test_boolean.IsLongDurationTestBoolean"
    ]
    """<p>Verifies if the test suite is a long duration test.</p>"""
    protocol: NotRequired["aws_sdk_iotdeviceadvisor.types.protocol.Protocol"]
    """<p>Gets the MQTT protocol that is configured in the suite definition.</p>"""
    created_at: NotRequired["aws_sdk_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Date (in Unix epoch time) when the test suite was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuiteDefinitionInformation) -> dict:
    out: dict = {}
    if "suite_definition_id" in value:
        out["suiteDefinitionId"] = value["suite_definition_id"]
    if "suite_definition_name" in value:
        out["suiteDefinitionName"] = value["suite_definition_name"]
    if "default_devices" in value:
        import aws_sdk_iotdeviceadvisor.types.device_under_test_list

        out["defaultDevices"] = (
            aws_sdk_iotdeviceadvisor.types.device_under_test_list.serialize_json(
                value["default_devices"]
            )
        )
    if "intended_for_qualification" in value:
        out["intendedForQualification"] = value["intended_for_qualification"]
    if "is_long_duration_test" in value:
        out["isLongDurationTest"] = value["is_long_duration_test"]
    if "protocol" in value:
        import aws_sdk_iotdeviceadvisor.types.protocol

        out["protocol"] = aws_sdk_iotdeviceadvisor.types.protocol.serialize_json(
            value["protocol"]
        )
    if "created_at" in value:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["createdAt"] = aws_sdk_iotdeviceadvisor.types.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> SuiteDefinitionInformation:
    out: SuiteDefinitionInformation = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionId" in data:
        out["suite_definition_id"] = data["suiteDefinitionId"]
    if "suiteDefinitionName" in data:
        out["suite_definition_name"] = data["suiteDefinitionName"]
    if "defaultDevices" in data:
        import aws_sdk_iotdeviceadvisor.types.device_under_test_list

        out["default_devices"] = (
            aws_sdk_iotdeviceadvisor.types.device_under_test_list.deserialize_json(
                data["defaultDevices"]
            )
        )
    if "intendedForQualification" in data:
        out["intended_for_qualification"] = data["intendedForQualification"]
    if "isLongDurationTest" in data:
        out["is_long_duration_test"] = data["isLongDurationTest"]
    if "protocol" in data:
        import aws_sdk_iotdeviceadvisor.types.protocol

        out["protocol"] = aws_sdk_iotdeviceadvisor.types.protocol.deserialize_json(
            data["protocol"]
        )
    if "createdAt" in data:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["created_at"] = aws_sdk_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    return out
