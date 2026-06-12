"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelLifeCycle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.stage_description


class ModelLifeCycle(TypedDict):
    stage: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p> The current stage in the model life cycle. </p>"""
    stage_status: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p> The current status of a stage in model life cycle. </p>"""
    stage_description: NotRequired[
        "aws_sdk_sagemaker.types.stage_description.StageDescription"
    ]
    """<p> Describes the stage related details. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelLifeCycle) -> dict:
    out: dict = {}
    if "stage" in value:
        out["Stage"] = value["stage"]
    if "stage_status" in value:
        out["StageStatus"] = value["stage_status"]
    if "stage_description" in value:
        out["StageDescription"] = value["stage_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelLifeCycle:
    out: ModelLifeCycle = {}  # type: ignore[typeddict-item]
    if "Stage" in data:
        out["stage"] = data["Stage"]
    if "StageStatus" in data:
        out["stage_status"] = data["StageStatus"]
    if "StageDescription" in data:
        out["stage_description"] = data["StageDescription"]
    return out
