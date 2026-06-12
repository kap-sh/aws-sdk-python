"""Generated from Smithy shape ``com.amazonaws.sagemaker#EmrSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.assumable_role_arns
    import aws_sdk_sagemaker.types.execution_role_arns


class EmrSettings(TypedDict):
    assumable_role_arns: NotRequired[
        "aws_sdk_sagemaker.types.assumable_role_arns.AssumableRoleArns"
    ]
    """<p>An array of Amazon Resource Names (ARNs) of the IAM roles that the execution role of SageMaker can assume for performing operations or tasks related to Amazon EMR clusters or Amazon EMR Serverless applications. These roles define the permissions and access policies required when performing Amazon EMR-related operations, such as listing, connecting to, or terminating Amazon EMR clusters or Amazon EMR Serverless applications. They are typically used in cross-account access scenarios, where the Amazon EMR resources (clusters or serverless applications) are located in a different Amazon Web Services account than the SageMaker domain.</p>"""
    execution_role_arns: NotRequired[
        "aws_sdk_sagemaker.types.execution_role_arns.ExecutionRoleArns"
    ]
    """<p>An array of Amazon Resource Names (ARNs) of the IAM roles used by the Amazon EMR cluster instances or job execution environments to access other Amazon Web Services services and resources needed during the runtime of your Amazon EMR or Amazon EMR Serverless workloads, such as Amazon S3 for data access, Amazon CloudWatch for logging, or other Amazon Web Services services based on the particular workload requirements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmrSettings) -> dict:
    out: dict = {}
    if "assumable_role_arns" in value:
        import aws_sdk_sagemaker.types.assumable_role_arns

        out["AssumableRoleArns"] = (
            aws_sdk_sagemaker.types.assumable_role_arns.serialize_aws_json_1_1(
                value["assumable_role_arns"]
            )
        )
    if "execution_role_arns" in value:
        import aws_sdk_sagemaker.types.execution_role_arns

        out["ExecutionRoleArns"] = (
            aws_sdk_sagemaker.types.execution_role_arns.serialize_aws_json_1_1(
                value["execution_role_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EmrSettings:
    out: EmrSettings = {}  # type: ignore[typeddict-item]
    if "AssumableRoleArns" in data:
        import aws_sdk_sagemaker.types.assumable_role_arns

        out["assumable_role_arns"] = (
            aws_sdk_sagemaker.types.assumable_role_arns.deserialize_aws_json_1_1(
                data["AssumableRoleArns"]
            )
        )
    if "ExecutionRoleArns" in data:
        import aws_sdk_sagemaker.types.execution_role_arns

        out["execution_role_arns"] = (
            aws_sdk_sagemaker.types.execution_role_arns.deserialize_aws_json_1_1(
                data["ExecutionRoleArns"]
            )
        )
    return out
