"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.model_approval_status
    import capo_sagemaker.types.model_life_cycle
    import capo_sagemaker.types.model_package_arn
    import capo_sagemaker.types.model_package_registration_type
    import capo_sagemaker.types.model_package_status
    import capo_sagemaker.types.model_package_version


class ModelPackageSummary(TypedDict, closed=True):
    model_package_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model package.</p>"""
    model_package_group_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>If the model package is a versioned model, the model group that the versioned model belongs to.</p>"""
    model_package_version: NotRequired[
        "capo_sagemaker.types.model_package_version.ModelPackageVersion"
    ]
    """<p>If the model package is a versioned model, the version of the model.</p>"""
    model_package_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model package.</p>"""
    model_package_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A brief description of the model package.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp that shows when the model package was created.</p>"""
    model_package_status: NotRequired[
        "capo_sagemaker.types.model_package_status.ModelPackageStatus"
    ]
    """<p>The overall status of the model package.</p>"""
    model_approval_status: NotRequired[
        "capo_sagemaker.types.model_approval_status.ModelApprovalStatus"
    ]
    """<p>The approval status of the model. This can be one of the following values.</p> <ul> <li> <p> <code>APPROVED</code> - The model is approved</p> </li> <li> <p> <code>REJECTED</code> - The model is rejected.</p> </li> <li> <p> <code>PENDING_MANUAL_APPROVAL</code> - The model is waiting for manual approval.</p> </li> </ul>"""
    model_life_cycle: NotRequired[
        "capo_sagemaker.types.model_life_cycle.ModelLifeCycle"
    ]
    model_package_registration_type: NotRequired[
        "capo_sagemaker.types.model_package_registration_type.ModelPackageRegistrationType"
    ]
    """<p> The package registration type of the model package summary. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageSummary) -> dict:
    out: dict = {}
    if "model_package_name" in value:
        out["ModelPackageName"] = value["model_package_name"]
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    if "model_package_version" in value:
        out["ModelPackageVersion"] = value["model_package_version"]
    if "model_package_arn" in value:
        out["ModelPackageArn"] = value["model_package_arn"]
    if "model_package_description" in value:
        out["ModelPackageDescription"] = value["model_package_description"]
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "model_package_status" in value:
        import capo_sagemaker.types.model_package_status

        out["ModelPackageStatus"] = (
            capo_sagemaker.types.model_package_status.serialize_aws_json_1_1(
                value["model_package_status"]
            )
        )
    if "model_approval_status" in value:
        import capo_sagemaker.types.model_approval_status

        out["ModelApprovalStatus"] = (
            capo_sagemaker.types.model_approval_status.serialize_aws_json_1_1(
                value["model_approval_status"]
            )
        )
    if "model_life_cycle" in value:
        import capo_sagemaker.types.model_life_cycle

        out["ModelLifeCycle"] = (
            capo_sagemaker.types.model_life_cycle.serialize_aws_json_1_1(
                value["model_life_cycle"]
            )
        )
    if "model_package_registration_type" in value:
        import capo_sagemaker.types.model_package_registration_type

        out["ModelPackageRegistrationType"] = (
            capo_sagemaker.types.model_package_registration_type.serialize_aws_json_1_1(
                value["model_package_registration_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelPackageSummary:
    out: ModelPackageSummary = {}  # type: ignore[typeddict-item]
    if "ModelPackageName" in data:
        out["model_package_name"] = data["ModelPackageName"]
    if "ModelPackageGroupName" in data:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    if "ModelPackageVersion" in data:
        out["model_package_version"] = data["ModelPackageVersion"]
    if "ModelPackageArn" in data:
        out["model_package_arn"] = data["ModelPackageArn"]
    if "ModelPackageDescription" in data:
        out["model_package_description"] = data["ModelPackageDescription"]
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "ModelPackageStatus" in data:
        import capo_sagemaker.types.model_package_status

        out["model_package_status"] = (
            capo_sagemaker.types.model_package_status.deserialize_aws_json_1_1(
                data["ModelPackageStatus"]
            )
        )
    if "ModelApprovalStatus" in data:
        import capo_sagemaker.types.model_approval_status

        out["model_approval_status"] = (
            capo_sagemaker.types.model_approval_status.deserialize_aws_json_1_1(
                data["ModelApprovalStatus"]
            )
        )
    if "ModelLifeCycle" in data:
        import capo_sagemaker.types.model_life_cycle

        out["model_life_cycle"] = (
            capo_sagemaker.types.model_life_cycle.deserialize_aws_json_1_1(
                data["ModelLifeCycle"]
            )
        )
    if "ModelPackageRegistrationType" in data:
        import capo_sagemaker.types.model_package_registration_type

        out["model_package_registration_type"] = (
            capo_sagemaker.types.model_package_registration_type.deserialize_aws_json_1_1(
                data["ModelPackageRegistrationType"]
            )
        )
    return out
