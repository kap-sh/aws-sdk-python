"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtendTrainingPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_plan_extension_offering_id


class ExtendTrainingPlanRequest(TypedDict, closed=True):
    training_plan_extension_offering_id: NotRequired[
        "capo_sagemaker.types.training_plan_extension_offering_id.TrainingPlanExtensionOfferingId"
    ]
    """<p>The unique identifier of the extension offering to purchase. You can retrieve this ID from the <code>TrainingPlanExtensionOfferings</code> in the response of the <code>SearchTrainingPlanOfferings</code> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendTrainingPlanRequest) -> dict:
    out: dict = {}
    if "training_plan_extension_offering_id" in value:
        out["TrainingPlanExtensionOfferingId"] = value[
            "training_plan_extension_offering_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtendTrainingPlanRequest:
    out: ExtendTrainingPlanRequest = {}  # type: ignore[typeddict-item]
    if "TrainingPlanExtensionOfferingId" in data:
        out["training_plan_extension_offering_id"] = data[
            "TrainingPlanExtensionOfferingId"
        ]
    return out
