"""Generated from Smithy shape ``com.amazonaws.devicefarm#ScheduleRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.device_selection_configuration
    import capo_device_farm.types.execution_configuration
    import capo_device_farm.types.name
    import capo_device_farm.types.schedule_run_configuration
    import capo_device_farm.types.schedule_run_test


class ScheduleRunRequest(TypedDict, closed=True):
    project_arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the project for the run to be scheduled.</p>"""
    app_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of an application package to run tests against, created with <a>CreateUpload</a>. See <a>ListUploads</a>.</p>"""
    device_pool_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the device pool for the run to be scheduled.</p>"""
    device_selection_configuration: NotRequired[
        "capo_device_farm.types.device_selection_configuration.DeviceSelectionConfiguration"
    ]
    """<p>The filter criteria used to dynamically select a set of devices for a test run and the maximum number of devices to be included in the run.</p> <p>Either <b> <code>devicePoolArn</code> </b> or <b> <code>deviceSelectionConfiguration</code> </b> is required in a request.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The name for the run to be scheduled.</p>"""
    test: "capo_device_farm.types.schedule_run_test.ScheduleRunTest"
    """<p>Information about the test for the run to be scheduled.</p>"""
    configuration: NotRequired[
        "capo_device_farm.types.schedule_run_configuration.ScheduleRunConfiguration"
    ]
    """<p>Information about the settings for the run to be scheduled.</p>"""
    execution_configuration: NotRequired[
        "capo_device_farm.types.execution_configuration.ExecutionConfiguration"
    ]
    """<p>Specifies configuration information about a test run, such as the execution timeout (in minutes).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleRunRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "device_pool_arn" in value:
        out["devicePoolArn"] = value["device_pool_arn"]
    if "device_selection_configuration" in value:
        import capo_device_farm.types.device_selection_configuration

        out["deviceSelectionConfiguration"] = (
            capo_device_farm.types.device_selection_configuration.serialize_aws_json_1_1(
                value["device_selection_configuration"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    import capo_device_farm.types.schedule_run_test

    out["test"] = capo_device_farm.types.schedule_run_test.serialize_aws_json_1_1(
        value["test"]
    )
    if "configuration" in value:
        import capo_device_farm.types.schedule_run_configuration

        out["configuration"] = (
            capo_device_farm.types.schedule_run_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "execution_configuration" in value:
        import capo_device_farm.types.execution_configuration

        out["executionConfiguration"] = (
            capo_device_farm.types.execution_configuration.serialize_aws_json_1_1(
                value["execution_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduleRunRequest:
    out: ScheduleRunRequest = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("ScheduleRunRequest.project_arn required")
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    if "devicePoolArn" in data:
        out["device_pool_arn"] = data["devicePoolArn"]
    if "deviceSelectionConfiguration" in data:
        import capo_device_farm.types.device_selection_configuration

        out["device_selection_configuration"] = (
            capo_device_farm.types.device_selection_configuration.deserialize_aws_json_1_1(
                data["deviceSelectionConfiguration"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "test" in data:
        import capo_device_farm.types.schedule_run_test

        out["test"] = capo_device_farm.types.schedule_run_test.deserialize_aws_json_1_1(
            data["test"]
        )
    else:
        raise DeserializationError("ScheduleRunRequest.test required")
    if "configuration" in data:
        import capo_device_farm.types.schedule_run_configuration

        out["configuration"] = (
            capo_device_farm.types.schedule_run_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if "executionConfiguration" in data:
        import capo_device_farm.types.execution_configuration

        out["execution_configuration"] = (
            capo_device_farm.types.execution_configuration.deserialize_aws_json_1_1(
                data["executionConfiguration"]
            )
        )
    return out
