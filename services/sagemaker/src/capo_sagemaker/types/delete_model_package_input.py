"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteModelPackageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.versioned_arn_or_name


class DeleteModelPackageInput(TypedDict, closed=True):
    model_package_name: NotRequired[
        "capo_sagemaker.types.versioned_arn_or_name.VersionedArnOrName"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the model package to delete.</p> <p>When you specify a name, the name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteModelPackageInput) -> dict:
    out: dict = {}
    if "model_package_name" in value:
        out["ModelPackageName"] = value["model_package_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteModelPackageInput:
    out: DeleteModelPackageInput = {}  # type: ignore[typeddict-item]
    if "ModelPackageName" in data:
        out["model_package_name"] = data["ModelPackageName"]
    return out
