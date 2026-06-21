"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestType``."""

from typing import Literal, TypeAlias, cast

TestType: TypeAlias = Literal[
    "BUILTIN_FUZZ",
    "APPIUM_JAVA_JUNIT",
    "APPIUM_JAVA_TESTNG",
    "APPIUM_PYTHON",
    "APPIUM_NODE",
    "APPIUM_RUBY",
    "APPIUM_WEB_JAVA_JUNIT",
    "APPIUM_WEB_JAVA_TESTNG",
    "APPIUM_WEB_PYTHON",
    "APPIUM_WEB_NODE",
    "APPIUM_WEB_RUBY",
    "INSTRUMENTATION",
    "XCTEST",
    "XCTEST_UI",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TestType:
    return cast(TestType, data)
