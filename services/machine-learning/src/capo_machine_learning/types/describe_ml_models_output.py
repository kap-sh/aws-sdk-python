"""Generated from Smithy shape ``com.amazonaws.machinelearning#DescribeMLModelsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.ml_models
    import capo_machine_learning.types.string_type


class DescribeMLModelsOutput(TypedDict, closed=True):
    results: NotRequired["capo_machine_learning.types.ml_models.MLModels"]
    """<p>A list of <code>MLModel</code> that meet the search criteria.</p>"""
    next_token: NotRequired["capo_machine_learning.types.string_type.StringType"]
    """<p>The ID of the next page in the paginated results that indicates at least one more page follows.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMLModelsOutput) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_machine_learning.types.ml_models

        out["Results"] = capo_machine_learning.types.ml_models.serialize_aws_json_1_1(
            value["results"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMLModelsOutput:
    out: DescribeMLModelsOutput = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_machine_learning.types.ml_models

        out["results"] = capo_machine_learning.types.ml_models.deserialize_aws_json_1_1(
            data["Results"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
