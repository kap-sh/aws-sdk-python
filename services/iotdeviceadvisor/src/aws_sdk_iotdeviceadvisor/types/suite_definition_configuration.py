"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#SuiteDefinitionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.amazon_resource_name
    import aws_sdk_iotdeviceadvisor.types.device_under_test_list
    import aws_sdk_iotdeviceadvisor.types.intended_for_qualification_boolean
    import aws_sdk_iotdeviceadvisor.types.is_long_duration_test_boolean
    import aws_sdk_iotdeviceadvisor.types.protocol
    import aws_sdk_iotdeviceadvisor.types.root_group
    import aws_sdk_iotdeviceadvisor.types.suite_definition_name


class SuiteDefinitionConfiguration(TypedDict):
    suite_definition_name: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.suite_definition_name.SuiteDefinitionName"
    ]
    """<p>Gets the suite definition name. This is a required parameter.</p>"""
    devices: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.device_under_test_list.DeviceUnderTestList"
    ]
    """<p>Gets the devices configured.</p>"""
    intended_for_qualification: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.intended_for_qualification_boolean.IntendedForQualificationBoolean"
    ]
    """<p>Gets the tests intended for qualification in a suite.</p>"""
    is_long_duration_test: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.is_long_duration_test_boolean.IsLongDurationTestBoolean"
    ]
    """<p>Verifies if the test suite is a long duration test.</p>"""
    root_group: NotRequired["aws_sdk_iotdeviceadvisor.types.root_group.RootGroup"]
    """<p>Gets the test suite root group. This is a required parameter. For updating or creating the latest qualification suite, if <code>intendedForQualification</code> is set to true, <code>rootGroup</code> can be an empty string. If <code>intendedForQualification</code> is false, <code>rootGroup</code> cannot be an empty string. If <code>rootGroup</code> is empty, and <code>intendedForQualification</code> is set to true, all the qualification tests are included, and the configuration is default.</p> <p> For a qualification suite, the minimum length is 0, and the maximum is 2048. For a non-qualification suite, the minimum length is 1, and the maximum is 2048. </p>"""
    device_permission_role_arn: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Gets the device permission ARN. This is a required parameter.</p>"""
    protocol: NotRequired["aws_sdk_iotdeviceadvisor.types.protocol.Protocol"]
    """<p>Sets the MQTT protocol that is configured in the suite definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuiteDefinitionConfiguration) -> dict:
    out: dict = {}
    if "suite_definition_name" in value:
        out["suiteDefinitionName"] = value["suite_definition_name"]
    if "devices" in value:
        import aws_sdk_iotdeviceadvisor.types.device_under_test_list

        out["devices"] = (
            aws_sdk_iotdeviceadvisor.types.device_under_test_list.serialize_json(
                value["devices"]
            )
        )
    if "intended_for_qualification" in value:
        out["intendedForQualification"] = value["intended_for_qualification"]
    if "is_long_duration_test" in value:
        out["isLongDurationTest"] = value["is_long_duration_test"]
    if "root_group" in value:
        out["rootGroup"] = value["root_group"]
    if "device_permission_role_arn" in value:
        out["devicePermissionRoleArn"] = value["device_permission_role_arn"]
    if "protocol" in value:
        import aws_sdk_iotdeviceadvisor.types.protocol

        out["protocol"] = aws_sdk_iotdeviceadvisor.types.protocol.serialize_json(
            value["protocol"]
        )
    return out


def deserialize_json(data: dict) -> SuiteDefinitionConfiguration:
    out: SuiteDefinitionConfiguration = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionName" in data:
        out["suite_definition_name"] = data["suiteDefinitionName"]
    if "devices" in data:
        import aws_sdk_iotdeviceadvisor.types.device_under_test_list

        out["devices"] = (
            aws_sdk_iotdeviceadvisor.types.device_under_test_list.deserialize_json(
                data["devices"]
            )
        )
    if "intendedForQualification" in data:
        out["intended_for_qualification"] = data["intendedForQualification"]
    if "isLongDurationTest" in data:
        out["is_long_duration_test"] = data["isLongDurationTest"]
    if "rootGroup" in data:
        out["root_group"] = data["rootGroup"]
    if "devicePermissionRoleArn" in data:
        out["device_permission_role_arn"] = data["devicePermissionRoleArn"]
    if "protocol" in data:
        import aws_sdk_iotdeviceadvisor.types.protocol

        out["protocol"] = aws_sdk_iotdeviceadvisor.types.protocol.deserialize_json(
            data["protocol"]
        )
    return out
