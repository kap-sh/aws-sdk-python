"""Generated from Smithy shape ``com.amazonaws.devicefarm#ScheduleRunTest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.filter
    import aws_sdk_device_farm.types.test_parameters
    import aws_sdk_device_farm.types.test_type


class ScheduleRunTest(TypedDict, closed=True):
    type: "aws_sdk_device_farm.types.test_type.TestType"
    """<p>The test's type.</p> <p>Must be one of the following values:</p> <ul> <li> <p>BUILTIN_FUZZ</p> </li> <li> <p>APPIUM_JAVA_JUNIT</p> </li> <li> <p>APPIUM_JAVA_TESTNG</p> </li> <li> <p>APPIUM_PYTHON</p> </li> <li> <p>APPIUM_NODE</p> </li> <li> <p>APPIUM_RUBY</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG</p> </li> <li> <p>APPIUM_WEB_PYTHON</p> </li> <li> <p>APPIUM_WEB_NODE</p> </li> <li> <p>APPIUM_WEB_RUBY</p> </li> <li> <p>INSTRUMENTATION</p> </li> <li> <p>XCTEST</p> </li> <li> <p>XCTEST_UI</p> </li> </ul>"""
    test_package_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the uploaded test to be run.</p>"""
    test_spec_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the YAML-formatted test specification.</p>"""
    filter: NotRequired["aws_sdk_device_farm.types.filter.Filter"]
    """<p>The test's filter.</p>"""
    parameters: NotRequired["aws_sdk_device_farm.types.test_parameters.TestParameters"]
    """<p>The test's parameters, such as test framework parameters and fixture settings. Parameters are represented by name-value pairs of strings.</p> <p>For all tests:</p> <ul> <li> <p> <code>app_performance_monitoring</code>: Performance monitoring is enabled by default. Set this parameter to false to disable it.</p> </li> </ul> <p>For Appium tests (all types):</p> <ul> <li> <p>appium_version: The Appium version. Currently supported values are 1.6.5 (and later), latest, and default.</p> <ul> <li> <p>latest runs the latest Appium version supported by Device Farm (1.9.1).</p> </li> <li> <p>For default, Device Farm selects a compatible version of Appium for the device. The current behavior is to run 1.7.2 on Android devices and iOS 9 and earlier and 1.7.2 for iOS 10 and later.</p> </li> <li> <p>This behavior is subject to change.</p> </li> </ul> </li> </ul> <p>For fuzz tests (Android only):</p> <ul> <li> <p>event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.</p> </li> <li> <p>throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.</p> </li> <li> <p>seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.</p> </li> </ul> <p>For Instrumentation:</p> <ul> <li> <p>filter: A test filter string. Examples:</p> <ul> <li> <p>Running a single test case: <code>com.android.abc.Test1</code> </p> </li> <li> <p>Running a single test: <code>com.android.abc.Test1#smoke</code> </p> </li> <li> <p>Running multiple tests: <code>com.android.abc.Test1,com.android.abc.Test2</code> </p> </li> </ul> </li> </ul> <p>For XCTest and XCTestUI:</p> <ul> <li> <p>filter: A test filter string. Examples:</p> <ul> <li> <p>Running a single test class: <code>LoginTests</code> </p> </li> <li> <p>Running a multiple test classes: <code>LoginTests,SmokeTests</code> </p> </li> <li> <p>Running a single test: <code>LoginTests/testValid</code> </p> </li> <li> <p>Running multiple tests: <code>LoginTests/testValid,LoginTests/testInvalid</code> </p> </li> </ul> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleRunTest) -> dict:
    out: dict = {}
    import aws_sdk_device_farm.types.test_type

    out["type"] = aws_sdk_device_farm.types.test_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "test_package_arn" in value:
        out["testPackageArn"] = value["test_package_arn"]
    if "test_spec_arn" in value:
        out["testSpecArn"] = value["test_spec_arn"]
    if "filter" in value:
        out["filter"] = value["filter"]
    if "parameters" in value:
        import aws_sdk_device_farm.types.test_parameters

        out["parameters"] = (
            aws_sdk_device_farm.types.test_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduleRunTest:
    out: ScheduleRunTest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_device_farm.types.test_type

        out["type"] = aws_sdk_device_farm.types.test_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("ScheduleRunTest.type required")
    if "testPackageArn" in data:
        out["test_package_arn"] = data["testPackageArn"]
    if "testSpecArn" in data:
        out["test_spec_arn"] = data["testSpecArn"]
    if "filter" in data:
        out["filter"] = data["filter"]
    if "parameters" in data:
        import aws_sdk_device_farm.types.test_parameters

        out["parameters"] = (
            aws_sdk_device_farm.types.test_parameters.deserialize_aws_json_1_1(
                data["parameters"]
            )
        )
    return out
