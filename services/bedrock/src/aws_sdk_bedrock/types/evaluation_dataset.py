"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationDataset``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.evaluation_dataset_location
    import aws_sdk_bedrock.types.evaluation_dataset_name


class EvaluationDataset(TypedDict):
    name: "aws_sdk_bedrock.types.evaluation_dataset_name.EvaluationDatasetName"
    """<p>Used to specify supported built-in prompt datasets. Valid values are <code>Builtin.Bold</code>, <code>Builtin.BoolQ</code>, <code>Builtin.NaturalQuestions</code>, <code>Builtin.Gigaword</code>, <code>Builtin.RealToxicityPrompts</code>, <code>Builtin.TriviaQA</code>, <code>Builtin.T-Rex</code>, <code>Builtin.WomensEcommerceClothingReviews</code> and <code>Builtin.Wikitext2</code>.</p>"""
    dataset_location: NotRequired[
        "aws_sdk_bedrock.types.evaluation_dataset_location.EvaluationDatasetLocation"
    ]
    """<p>For custom prompt datasets, you must specify the location in Amazon S3 where the prompt dataset is saved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationDataset) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "dataset_location" in value:
        import aws_sdk_bedrock.types.evaluation_dataset_location

        out["datasetLocation"] = (
            aws_sdk_bedrock.types.evaluation_dataset_location.serialize_json(
                value["dataset_location"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationDataset:
    out: EvaluationDataset = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EvaluationDataset.name required")
    if "datasetLocation" in data:
        import aws_sdk_bedrock.types.evaluation_dataset_location

        out["dataset_location"] = (
            aws_sdk_bedrock.types.evaluation_dataset_location.deserialize_json(
                data["datasetLocation"]
            )
        )
    return out
