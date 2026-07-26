"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobStoppingConditions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_human_labeled_object_count
    import capo_sagemaker.types.max_percentage_of_input_dataset_labeled


class LabelingJobStoppingConditions(TypedDict, closed=True):
    max_human_labeled_object_count: NotRequired[
        "capo_sagemaker.types.max_human_labeled_object_count.MaxHumanLabeledObjectCount"
    ]
    """<p>The maximum number of objects that can be labeled by human workers.</p>"""
    max_percentage_of_input_dataset_labeled: NotRequired[
        "capo_sagemaker.types.max_percentage_of_input_dataset_labeled.MaxPercentageOfInputDatasetLabeled"
    ]
    """<p>The maximum number of input data objects that should be labeled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobStoppingConditions) -> dict:
    out: dict = {}
    if "max_human_labeled_object_count" in value:
        out["MaxHumanLabeledObjectCount"] = value["max_human_labeled_object_count"]
    if "max_percentage_of_input_dataset_labeled" in value:
        out["MaxPercentageOfInputDatasetLabeled"] = value[
            "max_percentage_of_input_dataset_labeled"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobStoppingConditions:
    out: LabelingJobStoppingConditions = {}  # type: ignore[typeddict-item]
    if "MaxHumanLabeledObjectCount" in data:
        out["max_human_labeled_object_count"] = data["MaxHumanLabeledObjectCount"]
    if "MaxPercentageOfInputDatasetLabeled" in data:
        out["max_percentage_of_input_dataset_labeled"] = data[
            "MaxPercentageOfInputDatasetLabeled"
        ]
    return out
