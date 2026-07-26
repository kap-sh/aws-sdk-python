"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteModelPackageGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.arn_or_name


class DeleteModelPackageGroupInput(TypedDict, closed=True):
    model_package_group_name: NotRequired["capo_sagemaker.types.arn_or_name.ArnOrName"]
    """<p>The name of the model group to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteModelPackageGroupInput) -> dict:
    out: dict = {}
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteModelPackageGroupInput:
    out: DeleteModelPackageGroupInput = {}  # type: ignore[typeddict-item]
    if "ModelPackageGroupName" in data:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    return out
