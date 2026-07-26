"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDescribeModelPackageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.entity_description
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.inference_specification
    import capo_sagemaker.types.model_approval_status
    import capo_sagemaker.types.model_package_arn
    import capo_sagemaker.types.model_package_registration_type
    import capo_sagemaker.types.model_package_status
    import capo_sagemaker.types.model_package_version


class BatchDescribeModelPackageSummary(TypedDict, closed=True):
    model_package_group_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The group name for the model package</p>"""
    model_package_version: NotRequired[
        "capo_sagemaker.types.model_package_version.ModelPackageVersion"
    ]
    """<p>The version number of a versioned model.</p>"""
    model_package_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model package.</p>"""
    model_package_description: NotRequired[
        "capo_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>The description of the model package.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time of the mortgage package summary.</p>"""
    inference_specification: NotRequired[
        "capo_sagemaker.types.inference_specification.InferenceSpecification"
    ]
    model_package_status: NotRequired[
        "capo_sagemaker.types.model_package_status.ModelPackageStatus"
    ]
    """<p>The status of the mortgage package.</p>"""
    model_approval_status: NotRequired[
        "capo_sagemaker.types.model_approval_status.ModelApprovalStatus"
    ]
    """<p>The approval status of the model.</p>"""
    model_package_registration_type: NotRequired[
        "capo_sagemaker.types.model_package_registration_type.ModelPackageRegistrationType"
    ]
    """<p> The package registration type of the model package summary. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDescribeModelPackageSummary) -> dict:
    out: dict = {}
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
    if "inference_specification" in value:
        import capo_sagemaker.types.inference_specification

        out["InferenceSpecification"] = (
            capo_sagemaker.types.inference_specification.serialize_aws_json_1_1(
                value["inference_specification"]
            )
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
    if "model_package_registration_type" in value:
        import capo_sagemaker.types.model_package_registration_type

        out["ModelPackageRegistrationType"] = (
            capo_sagemaker.types.model_package_registration_type.serialize_aws_json_1_1(
                value["model_package_registration_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDescribeModelPackageSummary:
    out: BatchDescribeModelPackageSummary = {}  # type: ignore[typeddict-item]
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
    if "InferenceSpecification" in data:
        import capo_sagemaker.types.inference_specification

        out["inference_specification"] = (
            capo_sagemaker.types.inference_specification.deserialize_aws_json_1_1(
                data["InferenceSpecification"]
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
    if "ModelPackageRegistrationType" in data:
        import capo_sagemaker.types.model_package_registration_type

        out["model_package_registration_type"] = (
            capo_sagemaker.types.model_package_registration_type.deserialize_aws_json_1_1(
                data["ModelPackageRegistrationType"]
            )
        )
    return out
