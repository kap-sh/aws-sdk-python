"""Generated from Smithy shape ``com.amazonaws.machinelearning#DescribeEvaluationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.evaluations
    import aws_sdk_machine_learning.types.string_type


class DescribeEvaluationsOutput(TypedDict):
    results: NotRequired["aws_sdk_machine_learning.types.evaluations.Evaluations"]
    """<p>A list of <code>Evaluation</code> that meet the search criteria. </p>"""
    next_token: NotRequired["aws_sdk_machine_learning.types.string_type.StringType"]
    """<p>The ID of the next page in the paginated results that indicates at least one more page follows.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEvaluationsOutput) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_machine_learning.types.evaluations

        out["Results"] = (
            aws_sdk_machine_learning.types.evaluations.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEvaluationsOutput:
    out: DescribeEvaluationsOutput = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_machine_learning.types.evaluations

        out["results"] = (
            aws_sdk_machine_learning.types.evaluations.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
