"""Generated from Smithy shape ``com.amazonaws.sagemaker#EmrServerlessSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_status
    import capo_sagemaker.types.role_arn


class EmrServerlessSettings(TypedDict, closed=True):
    execution_role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services IAM role that is assumed for running Amazon EMR Serverless jobs in SageMaker Canvas. This role should have the necessary permissions to read and write data attached and a trust relationship with EMR Serverless.</p>"""
    status: NotRequired["capo_sagemaker.types.feature_status.FeatureStatus"]
    """<p>Describes whether Amazon EMR Serverless job capabilities are enabled or disabled in the SageMaker Canvas application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmrServerlessSettings) -> dict:
    out: dict = {}
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "status" in value:
        import capo_sagemaker.types.feature_status

        out["Status"] = capo_sagemaker.types.feature_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EmrServerlessSettings:
    out: EmrServerlessSettings = {}  # type: ignore[typeddict-item]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "Status" in data:
        import capo_sagemaker.types.feature_status

        out["status"] = capo_sagemaker.types.feature_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
