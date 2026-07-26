"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string64
    import capo_sagemaker.types.training_plan_filter_name


class TrainingPlanFilter(TypedDict, closed=True):
    name: NotRequired[
        "capo_sagemaker.types.training_plan_filter_name.TrainingPlanFilterName"
    ]
    """<p>The name of the filter field (e.g., Status, InstanceType).</p>"""
    value: NotRequired["capo_sagemaker.types.string64.String64"]
    """<p>The value to filter by for the specified field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_sagemaker.types.training_plan_filter_name

        out["Name"] = (
            capo_sagemaker.types.training_plan_filter_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingPlanFilter:
    out: TrainingPlanFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_sagemaker.types.training_plan_filter_name

        out["name"] = (
            capo_sagemaker.types.training_plan_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
