"""Generated from Smithy shape ``com.amazonaws.codebuild#TestCase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.string
    import capo_codebuild.types.timestamp
    import capo_codebuild.types.wrapper_long


class TestCase(TypedDict, closed=True):
    report_arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The ARN of the report to which the test case belongs. </p>"""
    test_raw_data_path: NotRequired["capo_codebuild.types.string.String"]
    """<p> The path to the raw data file that contains the test result. </p>"""
    prefix: NotRequired["capo_codebuild.types.string.String"]
    """<p> A string that is applied to a series of related test cases. CodeBuild generates the prefix. The prefix depends on the framework used to generate the tests. </p>"""
    name: NotRequired["capo_codebuild.types.string.String"]
    """<p> The name of the test case. </p>"""
    status: NotRequired["capo_codebuild.types.string.String"]
    """<p> The status returned by the test case after it was run. Valid statuses are <code>SUCCEEDED</code>, <code>FAILED</code>, <code>ERROR</code>, <code>SKIPPED</code>, and <code>UNKNOWN</code>. </p>"""
    duration_in_nano_seconds: NotRequired[
        "capo_codebuild.types.wrapper_long.WrapperLong"
    ]
    """<p> The number of nanoseconds it took to run this test case. </p>"""
    message: NotRequired["capo_codebuild.types.string.String"]
    """<p> A message associated with a test case. For example, an error message or stack trace. </p>"""
    expired: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p> The date and time a test case expires. A test case expires 30 days after it is created. An expired test case is not available to view in CodeBuild. </p>"""
    test_suite_name: NotRequired["capo_codebuild.types.string.String"]
    """<p>The name of the test suite that the test case is a part of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestCase) -> dict:
    out: dict = {}
    if "report_arn" in value:
        out["reportArn"] = value["report_arn"]
    if "test_raw_data_path" in value:
        out["testRawDataPath"] = value["test_raw_data_path"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "duration_in_nano_seconds" in value:
        out["durationInNanoSeconds"] = value["duration_in_nano_seconds"]
    if "message" in value:
        out["message"] = value["message"]
    if "expired" in value:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["expired"]
        )
    if "test_suite_name" in value:
        out["testSuiteName"] = value["test_suite_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestCase:
    out: TestCase = {}  # type: ignore[typeddict-item]
    if "reportArn" in data:
        out["report_arn"] = data["reportArn"]
    if "testRawDataPath" in data:
        out["test_raw_data_path"] = data["testRawDataPath"]
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "durationInNanoSeconds" in data:
        out["duration_in_nano_seconds"] = data["durationInNanoSeconds"]
    if "message" in data:
        out["message"] = data["message"]
    if "expired" in data:
        import capo_codebuild.types.timestamp

        out["expired"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["expired"]
        )
    if "testSuiteName" in data:
        out["test_suite_name"] = data["testSuiteName"]
    return out
