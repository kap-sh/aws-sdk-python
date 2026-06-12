"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ProblemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.problem

ProblemList: TypeAlias = list["aws_sdk_application_insights.types.problem.Problem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProblemList) -> list:
    import aws_sdk_application_insights.types.problem

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_insights.types.problem.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProblemList:
    import aws_sdk_application_insights.types.problem

    out: ProblemList = []
    for item in data:
        out.append(
            aws_sdk_application_insights.types.problem.deserialize_aws_json_1_1(item)
        )
    return out
