"""Generated from Smithy shape ``com.amazonaws.codebuild#TestCases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.test_case

TestCases: TypeAlias = list["aws_sdk_codebuild.types.test_case.TestCase"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestCases) -> list:
    import aws_sdk_codebuild.types.test_case

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.test_case.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TestCases:
    import aws_sdk_codebuild.types.test_case

    out: TestCases = []
    for item in data:
        out.append(aws_sdk_codebuild.types.test_case.deserialize_aws_json_1_1(item))
    return out
