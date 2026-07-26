"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageValidationProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.transform_job_definition


class ModelPackageValidationProfile(TypedDict, closed=True):
    profile_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the profile for the model package.</p>"""
    transform_job_definition: NotRequired[
        "capo_sagemaker.types.transform_job_definition.TransformJobDefinition"
    ]
    """<p>The <code>TransformJobDefinition</code> object that describes the transform job used for the validation of the model package.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageValidationProfile) -> dict:
    out: dict = {}
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "transform_job_definition" in value:
        import capo_sagemaker.types.transform_job_definition

        out["TransformJobDefinition"] = (
            capo_sagemaker.types.transform_job_definition.serialize_aws_json_1_1(
                value["transform_job_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageValidationProfile:
    out: ModelPackageValidationProfile = {}  # type: ignore[typeddict-item]
    if "ProfileName" in data:
        out["profile_name"] = data["ProfileName"]
    if "TransformJobDefinition" in data:
        import capo_sagemaker.types.transform_job_definition

        out["transform_job_definition"] = (
            capo_sagemaker.types.transform_job_definition.deserialize_aws_json_1_1(
                data["TransformJobDefinition"]
            )
        )
    return out
