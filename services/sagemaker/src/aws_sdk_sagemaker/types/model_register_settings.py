"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelRegisterSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_status
    import aws_sdk_sagemaker.types.role_arn


class ModelRegisterSettings(TypedDict):
    status: NotRequired["aws_sdk_sagemaker.types.feature_status.FeatureStatus"]
    """<p>Describes whether the integration to the model registry is enabled or disabled in the Canvas application.</p>"""
    cross_account_model_register_role_arn: NotRequired[
        "aws_sdk_sagemaker.types.role_arn.RoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the SageMaker model registry account. Required only to register model versions created by a different SageMaker Canvas Amazon Web Services account than the Amazon Web Services account in which SageMaker model registry is set up.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelRegisterSettings) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.feature_status

        out["Status"] = aws_sdk_sagemaker.types.feature_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "cross_account_model_register_role_arn" in value:
        out["CrossAccountModelRegisterRoleArn"] = value[
            "cross_account_model_register_role_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelRegisterSettings:
    out: ModelRegisterSettings = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.feature_status

        out["status"] = aws_sdk_sagemaker.types.feature_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "CrossAccountModelRegisterRoleArn" in data:
        out["cross_account_model_register_role_arn"] = data[
            "CrossAccountModelRegisterRoleArn"
        ]
    return out
