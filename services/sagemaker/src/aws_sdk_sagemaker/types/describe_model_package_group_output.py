"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelPackageGroupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.entity_description
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.managed_configuration
    import aws_sdk_sagemaker.types.model_package_group_arn
    import aws_sdk_sagemaker.types.model_package_group_status
    import aws_sdk_sagemaker.types.user_context


class DescribeModelPackageGroupOutput(TypedDict, closed=True):
    model_package_group_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the model group.</p>"""
    model_package_group_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_package_group_arn.ModelPackageGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model group.</p>"""
    model_package_group_description: NotRequired[
        "aws_sdk_sagemaker.types.entity_description.EntityDescription"
    ]
    """<p>A description of the model group.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>The time that the model group was created.</p>"""
    created_by: NotRequired["aws_sdk_sagemaker.types.user_context.UserContext"]
    model_package_group_status: NotRequired[
        "aws_sdk_sagemaker.types.model_package_group_status.ModelPackageGroupStatus"
    ]
    """<p>The status of the model group.</p>"""
    managed_configuration: NotRequired[
        "aws_sdk_sagemaker.types.managed_configuration.ManagedConfiguration"
    ]
    """<p>The managed configuration of the model package group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelPackageGroupOutput) -> dict:
    out: dict = {}
    if "model_package_group_name" in value:
        out["ModelPackageGroupName"] = value["model_package_group_name"]
    if "model_package_group_arn" in value:
        out["ModelPackageGroupArn"] = value["model_package_group_arn"]
    if "model_package_group_description" in value:
        out["ModelPackageGroupDescription"] = value["model_package_group_description"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "created_by" in value:
        import aws_sdk_sagemaker.types.user_context

        out["CreatedBy"] = aws_sdk_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "model_package_group_status" in value:
        import aws_sdk_sagemaker.types.model_package_group_status

        out["ModelPackageGroupStatus"] = (
            aws_sdk_sagemaker.types.model_package_group_status.serialize_aws_json_1_1(
                value["model_package_group_status"]
            )
        )
    if "managed_configuration" in value:
        import aws_sdk_sagemaker.types.managed_configuration

        out["ManagedConfiguration"] = (
            aws_sdk_sagemaker.types.managed_configuration.serialize_aws_json_1_1(
                value["managed_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelPackageGroupOutput:
    out: DescribeModelPackageGroupOutput = {}  # type: ignore[typeddict-item]
    if "ModelPackageGroupName" in data:
        out["model_package_group_name"] = data["ModelPackageGroupName"]
    if "ModelPackageGroupArn" in data:
        out["model_package_group_arn"] = data["ModelPackageGroupArn"]
    if "ModelPackageGroupDescription" in data:
        out["model_package_group_description"] = data["ModelPackageGroupDescription"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_sagemaker.types.user_context

        out["created_by"] = (
            aws_sdk_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["CreatedBy"]
            )
        )
    if "ModelPackageGroupStatus" in data:
        import aws_sdk_sagemaker.types.model_package_group_status

        out["model_package_group_status"] = (
            aws_sdk_sagemaker.types.model_package_group_status.deserialize_aws_json_1_1(
                data["ModelPackageGroupStatus"]
            )
        )
    if "ManagedConfiguration" in data:
        import aws_sdk_sagemaker.types.managed_configuration

        out["managed_configuration"] = (
            aws_sdk_sagemaker.types.managed_configuration.deserialize_aws_json_1_1(
                data["ManagedConfiguration"]
            )
        )
    return out
