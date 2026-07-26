"""Generated from Smithy shape ``com.amazonaws.devicefarm#Suite``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.counters
    import capo_device_farm.types.date_time
    import capo_device_farm.types.device_minutes
    import capo_device_farm.types.execution_result
    import capo_device_farm.types.execution_status
    import capo_device_farm.types.message
    import capo_device_farm.types.name
    import capo_device_farm.types.test_type


class Suite(TypedDict, closed=True):
    arn: NotRequired["capo_device_farm.types.amazon_resource_name.AmazonResourceName"]
    """<p>The suite's ARN.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The suite's name.</p>"""
    type: NotRequired["capo_device_farm.types.test_type.TestType"]
    """<p>The suite's type.</p> <p>Must be one of the following values:</p> <ul> <li> <p>BUILTIN_FUZZ</p> </li> <li> <p>APPIUM_JAVA_JUNIT</p> </li> <li> <p>APPIUM_JAVA_TESTNG</p> </li> <li> <p>APPIUM_PYTHON</p> </li> <li> <p>APPIUM_NODE</p> </li> <li> <p>APPIUM_RUBY</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG</p> </li> <li> <p>APPIUM_WEB_PYTHON</p> </li> <li> <p>APPIUM_WEB_NODE</p> </li> <li> <p>APPIUM_WEB_RUBY</p> </li> <li> <p>INSTRUMENTATION</p> </li> <li> <p>XCTEST</p> </li> <li> <p>XCTEST_UI</p> </li> </ul>"""
    created: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>When the suite was created.</p>"""
    status: NotRequired["capo_device_farm.types.execution_status.ExecutionStatus"]
    """<p>The suite's status.</p> <p>Allowed values include:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>PENDING_CONCURRENCY</p> </li> <li> <p>PENDING_DEVICE</p> </li> <li> <p>PROCESSING</p> </li> <li> <p>SCHEDULING</p> </li> <li> <p>PREPARING</p> </li> <li> <p>RUNNING</p> </li> <li> <p>COMPLETED</p> </li> <li> <p>STOPPING</p> </li> </ul>"""
    result: NotRequired["capo_device_farm.types.execution_result.ExecutionResult"]
    """<p>The suite's result.</p> <p>Allowed values include:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>PASSED</p> </li> <li> <p>WARNED</p> </li> <li> <p>FAILED</p> </li> <li> <p>SKIPPED</p> </li> <li> <p>ERRORED</p> </li> <li> <p>STOPPED</p> </li> </ul>"""
    started: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The suite's start time.</p>"""
    stopped: NotRequired["capo_device_farm.types.date_time.DateTime"]
    """<p>The suite's stop time.</p>"""
    counters: NotRequired["capo_device_farm.types.counters.Counters"]
    """<p>The suite's result counters.</p>"""
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>A message about the suite's result.</p>"""
    device_minutes: NotRequired["capo_device_farm.types.device_minutes.DeviceMinutes"]
    """<p>Represents the total (metered or unmetered) minutes used by the test suite.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Suite) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_device_farm.types.test_type

        out["type"] = capo_device_farm.types.test_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "created" in value:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    if "status" in value:
        import capo_device_farm.types.execution_status

        out["status"] = capo_device_farm.types.execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "result" in value:
        import capo_device_farm.types.execution_result

        out["result"] = capo_device_farm.types.execution_result.serialize_aws_json_1_1(
            value["result"]
        )
    if "started" in value:
        import capo_device_farm.types.date_time

        out["started"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["started"]
        )
    if "stopped" in value:
        import capo_device_farm.types.date_time

        out["stopped"] = capo_device_farm.types.date_time.serialize_aws_json_1_1(
            value["stopped"]
        )
    if "counters" in value:
        import capo_device_farm.types.counters

        out["counters"] = capo_device_farm.types.counters.serialize_aws_json_1_1(
            value["counters"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "device_minutes" in value:
        import capo_device_farm.types.device_minutes

        out["deviceMinutes"] = (
            capo_device_farm.types.device_minutes.serialize_aws_json_1_1(
                value["device_minutes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Suite:
    out: Suite = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import capo_device_farm.types.test_type

        out["type"] = capo_device_farm.types.test_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "created" in data:
        import capo_device_farm.types.date_time

        out["created"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["created"]
        )
    if "status" in data:
        import capo_device_farm.types.execution_status

        out["status"] = (
            capo_device_farm.types.execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "result" in data:
        import capo_device_farm.types.execution_result

        out["result"] = (
            capo_device_farm.types.execution_result.deserialize_aws_json_1_1(
                data["result"]
            )
        )
    if "started" in data:
        import capo_device_farm.types.date_time

        out["started"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["started"]
        )
    if "stopped" in data:
        import capo_device_farm.types.date_time

        out["stopped"] = capo_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["stopped"]
        )
    if "counters" in data:
        import capo_device_farm.types.counters

        out["counters"] = capo_device_farm.types.counters.deserialize_aws_json_1_1(
            data["counters"]
        )
    if "message" in data:
        out["message"] = data["message"]
    if "deviceMinutes" in data:
        import capo_device_farm.types.device_minutes

        out["device_minutes"] = (
            capo_device_farm.types.device_minutes.deserialize_aws_json_1_1(
                data["deviceMinutes"]
            )
        )
    return out
