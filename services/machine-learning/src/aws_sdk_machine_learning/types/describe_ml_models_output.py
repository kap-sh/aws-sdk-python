"""Generated from Smithy shape ``com.amazonaws.machinelearning#DescribeMLModelsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.ml_models
    import aws_sdk_machine_learning.types.string_type


class DescribeMLModelsOutput(TypedDict):
    results: NotRequired["aws_sdk_machine_learning.types.ml_models.MLModels"]
    """<p>A list of <code>MLModel</code> that meet the search criteria.</p>"""
    next_token: NotRequired["aws_sdk_machine_learning.types.string_type.StringType"]
    """<p>The ID of the next page in the paginated results that indicates at least one more page follows.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMLModelsOutput) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_machine_learning.types.ml_models

        out["Results"] = (
            aws_sdk_machine_learning.types.ml_models.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMLModelsOutput:
    out: DescribeMLModelsOutput = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_machine_learning.types.ml_models

        out["results"] = (
            aws_sdk_machine_learning.types.ml_models.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
