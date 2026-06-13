"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.aws_ec2_instance_details
    import aws_sdk_inspector2.types.aws_ecr_container_image_details
    import aws_sdk_inspector2.types.aws_lambda_function_details
    import aws_sdk_inspector2.types.code_repository_details


class ResourceDetails(TypedDict):
    aws_ec2_instance: NotRequired[
        "aws_sdk_inspector2.types.aws_ec2_instance_details.AwsEc2InstanceDetails"
    ]
    """<p>An object that contains details about the Amazon EC2 instance involved in the finding.</p>"""
    aws_ecr_container_image: NotRequired[
        "aws_sdk_inspector2.types.aws_ecr_container_image_details.AwsEcrContainerImageDetails"
    ]
    """<p>An object that contains details about the Amazon ECR container image involved in the finding.</p>"""
    aws_lambda_function: NotRequired[
        "aws_sdk_inspector2.types.aws_lambda_function_details.AwsLambdaFunctionDetails"
    ]
    """<p>A summary of the information about an Amazon Web Services Lambda function affected by a finding.</p>"""
    code_repository: NotRequired[
        "aws_sdk_inspector2.types.code_repository_details.CodeRepositoryDetails"
    ]
    """<p>Contains details about a code repository resource associated with a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDetails) -> dict:
    out: dict = {}
    if "aws_ec2_instance" in value:
        import aws_sdk_inspector2.types.aws_ec2_instance_details

        out["awsEc2Instance"] = (
            aws_sdk_inspector2.types.aws_ec2_instance_details.serialize_json(
                value["aws_ec2_instance"]
            )
        )
    if "aws_ecr_container_image" in value:
        import aws_sdk_inspector2.types.aws_ecr_container_image_details

        out["awsEcrContainerImage"] = (
            aws_sdk_inspector2.types.aws_ecr_container_image_details.serialize_json(
                value["aws_ecr_container_image"]
            )
        )
    if "aws_lambda_function" in value:
        import aws_sdk_inspector2.types.aws_lambda_function_details

        out["awsLambdaFunction"] = (
            aws_sdk_inspector2.types.aws_lambda_function_details.serialize_json(
                value["aws_lambda_function"]
            )
        )
    if "code_repository" in value:
        import aws_sdk_inspector2.types.code_repository_details

        out["codeRepository"] = (
            aws_sdk_inspector2.types.code_repository_details.serialize_json(
                value["code_repository"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceDetails:
    out: ResourceDetails = {}  # type: ignore[typeddict-item]
    if "awsEc2Instance" in data:
        import aws_sdk_inspector2.types.aws_ec2_instance_details

        out["aws_ec2_instance"] = (
            aws_sdk_inspector2.types.aws_ec2_instance_details.deserialize_json(
                data["awsEc2Instance"]
            )
        )
    if "awsEcrContainerImage" in data:
        import aws_sdk_inspector2.types.aws_ecr_container_image_details

        out["aws_ecr_container_image"] = (
            aws_sdk_inspector2.types.aws_ecr_container_image_details.deserialize_json(
                data["awsEcrContainerImage"]
            )
        )
    if "awsLambdaFunction" in data:
        import aws_sdk_inspector2.types.aws_lambda_function_details

        out["aws_lambda_function"] = (
            aws_sdk_inspector2.types.aws_lambda_function_details.deserialize_json(
                data["awsLambdaFunction"]
            )
        )
    if "codeRepository" in data:
        import aws_sdk_inspector2.types.code_repository_details

        out["code_repository"] = (
            aws_sdk_inspector2.types.code_repository_details.deserialize_json(
                data["codeRepository"]
            )
        )
    return out
