"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceFilterCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.resource_map_filter_list
    import aws_sdk_inspector2.types.resource_string_filter_list


class ResourceFilterCriteria(TypedDict):
    account_id: NotRequired[
        "aws_sdk_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The account IDs used as resource filter criteria.</p>"""
    resource_id: NotRequired[
        "aws_sdk_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The resource IDs used as resource filter criteria.</p>"""
    resource_type: NotRequired[
        "aws_sdk_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The resource types used as resource filter criteria.</p>"""
    ecr_repository_name: NotRequired[
        "aws_sdk_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The ECR repository names used as resource filter criteria.</p>"""
    lambda_function_name: NotRequired[
        "aws_sdk_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The Amazon Web Services Lambda function name used as resource filter criteria.</p>"""
    ecr_image_tags: NotRequired[
        "aws_sdk_inspector2.types.resource_string_filter_list.ResourceStringFilterList"
    ]
    """<p>The ECR image tags used as resource filter criteria.</p>"""
    ec2_instance_tags: NotRequired[
        "aws_sdk_inspector2.types.resource_map_filter_list.ResourceMapFilterList"
    ]
    """<p>The EC2 instance tags used as resource filter criteria.</p>"""
    lambda_function_tags: NotRequired[
        "aws_sdk_inspector2.types.resource_map_filter_list.ResourceMapFilterList"
    ]
    """<p>The Amazon Web Services Lambda function tags used as resource filter criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceFilterCriteria) -> dict:
    out: dict = {}
    if "account_id" in value:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["accountId"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.serialize_json(
                value["account_id"]
            )
        )
    if "resource_id" in value:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["resourceId"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.serialize_json(
                value["resource_id"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["resourceType"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.serialize_json(
                value["resource_type"]
            )
        )
    if "ecr_repository_name" in value:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["ecrRepositoryName"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.serialize_json(
                value["ecr_repository_name"]
            )
        )
    if "lambda_function_name" in value:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["lambdaFunctionName"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.serialize_json(
                value["lambda_function_name"]
            )
        )
    if "ecr_image_tags" in value:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["ecrImageTags"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.serialize_json(
                value["ecr_image_tags"]
            )
        )
    if "ec2_instance_tags" in value:
        import aws_sdk_inspector2.types.resource_map_filter_list

        out["ec2InstanceTags"] = (
            aws_sdk_inspector2.types.resource_map_filter_list.serialize_json(
                value["ec2_instance_tags"]
            )
        )
    if "lambda_function_tags" in value:
        import aws_sdk_inspector2.types.resource_map_filter_list

        out["lambdaFunctionTags"] = (
            aws_sdk_inspector2.types.resource_map_filter_list.serialize_json(
                value["lambda_function_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceFilterCriteria:
    out: ResourceFilterCriteria = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["account_id"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.deserialize_json(
                data["accountId"]
            )
        )
    if "resourceId" in data:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["resource_id"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.deserialize_json(
                data["resourceId"]
            )
        )
    if "resourceType" in data:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["resource_type"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.deserialize_json(
                data["resourceType"]
            )
        )
    if "ecrRepositoryName" in data:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["ecr_repository_name"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.deserialize_json(
                data["ecrRepositoryName"]
            )
        )
    if "lambdaFunctionName" in data:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["lambda_function_name"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.deserialize_json(
                data["lambdaFunctionName"]
            )
        )
    if "ecrImageTags" in data:
        import aws_sdk_inspector2.types.resource_string_filter_list

        out["ecr_image_tags"] = (
            aws_sdk_inspector2.types.resource_string_filter_list.deserialize_json(
                data["ecrImageTags"]
            )
        )
    if "ec2InstanceTags" in data:
        import aws_sdk_inspector2.types.resource_map_filter_list

        out["ec2_instance_tags"] = (
            aws_sdk_inspector2.types.resource_map_filter_list.deserialize_json(
                data["ec2InstanceTags"]
            )
        )
    if "lambdaFunctionTags" in data:
        import aws_sdk_inspector2.types.resource_map_filter_list

        out["lambda_function_tags"] = (
            aws_sdk_inspector2.types.resource_map_filter_list.deserialize_json(
                data["lambdaFunctionTags"]
            )
        )
    return out
