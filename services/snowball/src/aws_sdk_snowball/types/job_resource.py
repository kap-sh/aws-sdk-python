"""Generated from Smithy shape ``com.amazonaws.snowball#JobResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.ec2_ami_resource_list
    import aws_sdk_snowball.types.lambda_resource_list
    import aws_sdk_snowball.types.s3_resource_list


class JobResource(TypedDict):
    s3_resources: NotRequired["aws_sdk_snowball.types.s3_resource_list.S3ResourceList"]
    """<p>An array of <code>S3Resource</code> objects.</p>"""
    lambda_resources: NotRequired[
        "aws_sdk_snowball.types.lambda_resource_list.LambdaResourceList"
    ]
    """<p>The Python-language Lambda functions for this job.</p>"""
    ec2_ami_resources: NotRequired[
        "aws_sdk_snowball.types.ec2_ami_resource_list.Ec2AmiResourceList"
    ]
    """<p>The Amazon Machine Images (AMIs) associated with this job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobResource) -> dict:
    out: dict = {}
    if "s3_resources" in value:
        import aws_sdk_snowball.types.s3_resource_list

        out["S3Resources"] = (
            aws_sdk_snowball.types.s3_resource_list.serialize_aws_json_1_1(
                value["s3_resources"]
            )
        )
    if "lambda_resources" in value:
        import aws_sdk_snowball.types.lambda_resource_list

        out["LambdaResources"] = (
            aws_sdk_snowball.types.lambda_resource_list.serialize_aws_json_1_1(
                value["lambda_resources"]
            )
        )
    if "ec2_ami_resources" in value:
        import aws_sdk_snowball.types.ec2_ami_resource_list

        out["Ec2AmiResources"] = (
            aws_sdk_snowball.types.ec2_ami_resource_list.serialize_aws_json_1_1(
                value["ec2_ami_resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobResource:
    out: JobResource = {}  # type: ignore[typeddict-item]
    if "S3Resources" in data:
        import aws_sdk_snowball.types.s3_resource_list

        out["s3_resources"] = (
            aws_sdk_snowball.types.s3_resource_list.deserialize_aws_json_1_1(
                data["S3Resources"]
            )
        )
    if "LambdaResources" in data:
        import aws_sdk_snowball.types.lambda_resource_list

        out["lambda_resources"] = (
            aws_sdk_snowball.types.lambda_resource_list.deserialize_aws_json_1_1(
                data["LambdaResources"]
            )
        )
    if "Ec2AmiResources" in data:
        import aws_sdk_snowball.types.ec2_ami_resource_list

        out["ec2_ami_resources"] = (
            aws_sdk_snowball.types.ec2_ami_resource_list.deserialize_aws_json_1_1(
                data["Ec2AmiResources"]
            )
        )
    return out
