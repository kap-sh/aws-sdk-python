"""Generated from Smithy shape ``com.amazonaws.securityagent#AWSResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.iam_roles
    import aws_sdk_securityagent.types.lambda_function_arns
    import aws_sdk_securityagent.types.log_group_arns
    import aws_sdk_securityagent.types.s3_bucket_arns
    import aws_sdk_securityagent.types.secret_arns
    import aws_sdk_securityagent.types.vpc_configs


class AWSResources(TypedDict, closed=True):
    vpcs: NotRequired["aws_sdk_securityagent.types.vpc_configs.VpcConfigs"]
    """<p>The VPC configurations associated with the agent space.</p>"""
    log_groups: NotRequired["aws_sdk_securityagent.types.log_group_arns.LogGroupArns"]
    """<p>The Amazon Resource Names (ARNs) of the CloudWatch log groups associated with the agent space.</p>"""
    s3_buckets: NotRequired["aws_sdk_securityagent.types.s3_bucket_arns.S3BucketArns"]
    """<p>The Amazon Resource Names (ARNs) of the S3 buckets associated with the agent space.</p>"""
    secret_arns: NotRequired["aws_sdk_securityagent.types.secret_arns.SecretArns"]
    """<p>The Amazon Resource Names (ARNs) of the Secrets Manager secrets associated with the agent space.</p>"""
    lambda_function_arns: NotRequired[
        "aws_sdk_securityagent.types.lambda_function_arns.LambdaFunctionArns"
    ]
    """<p>The Amazon Resource Names (ARNs) of the Lambda functions associated with the agent space.</p>"""
    iam_roles: NotRequired["aws_sdk_securityagent.types.iam_roles.IamRoles"]
    """<p>The IAM roles associated with the agent space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AWSResources) -> dict:
    out: dict = {}
    if "vpcs" in value:
        import aws_sdk_securityagent.types.vpc_configs

        out["vpcs"] = aws_sdk_securityagent.types.vpc_configs.serialize_json(
            value["vpcs"]
        )
    if "log_groups" in value:
        import aws_sdk_securityagent.types.log_group_arns

        out["logGroups"] = aws_sdk_securityagent.types.log_group_arns.serialize_json(
            value["log_groups"]
        )
    if "s3_buckets" in value:
        import aws_sdk_securityagent.types.s3_bucket_arns

        out["s3Buckets"] = aws_sdk_securityagent.types.s3_bucket_arns.serialize_json(
            value["s3_buckets"]
        )
    if "secret_arns" in value:
        import aws_sdk_securityagent.types.secret_arns

        out["secretArns"] = aws_sdk_securityagent.types.secret_arns.serialize_json(
            value["secret_arns"]
        )
    if "lambda_function_arns" in value:
        import aws_sdk_securityagent.types.lambda_function_arns

        out["lambdaFunctionArns"] = (
            aws_sdk_securityagent.types.lambda_function_arns.serialize_json(
                value["lambda_function_arns"]
            )
        )
    if "iam_roles" in value:
        import aws_sdk_securityagent.types.iam_roles

        out["iamRoles"] = aws_sdk_securityagent.types.iam_roles.serialize_json(
            value["iam_roles"]
        )
    return out


def deserialize_json(data: dict) -> AWSResources:
    out: AWSResources = {}  # type: ignore[typeddict-item]
    if "vpcs" in data:
        import aws_sdk_securityagent.types.vpc_configs

        out["vpcs"] = aws_sdk_securityagent.types.vpc_configs.deserialize_json(
            data["vpcs"]
        )
    if "logGroups" in data:
        import aws_sdk_securityagent.types.log_group_arns

        out["log_groups"] = aws_sdk_securityagent.types.log_group_arns.deserialize_json(
            data["logGroups"]
        )
    if "s3Buckets" in data:
        import aws_sdk_securityagent.types.s3_bucket_arns

        out["s3_buckets"] = aws_sdk_securityagent.types.s3_bucket_arns.deserialize_json(
            data["s3Buckets"]
        )
    if "secretArns" in data:
        import aws_sdk_securityagent.types.secret_arns

        out["secret_arns"] = aws_sdk_securityagent.types.secret_arns.deserialize_json(
            data["secretArns"]
        )
    if "lambdaFunctionArns" in data:
        import aws_sdk_securityagent.types.lambda_function_arns

        out["lambda_function_arns"] = (
            aws_sdk_securityagent.types.lambda_function_arns.deserialize_json(
                data["lambdaFunctionArns"]
            )
        )
    if "iamRoles" in data:
        import aws_sdk_securityagent.types.iam_roles

        out["iam_roles"] = aws_sdk_securityagent.types.iam_roles.deserialize_json(
            data["iamRoles"]
        )
    return out
