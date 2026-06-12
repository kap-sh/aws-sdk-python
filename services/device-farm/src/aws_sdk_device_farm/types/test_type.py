"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: TestType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TestType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestType value: {data!r}")
    return cast(TestType, data)
