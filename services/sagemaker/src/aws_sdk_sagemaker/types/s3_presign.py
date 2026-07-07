"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3Presign``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.iam_policy_constraints


class S3Presign(TypedDict, closed=True):
    iam_policy_constraints: NotRequired[
        "aws_sdk_sagemaker.types.iam_policy_constraints.IamPolicyConstraints"
    ]
    """<p>Use this parameter to specify the allowed request source. Possible sources are either <code>SourceIp</code> or <code>VpcSourceIp</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Presign) -> dict:
    out: dict = {}
    if "iam_policy_constraints" in value:
        import aws_sdk_sagemaker.types.iam_policy_constraints

        out["IamPolicyConstraints"] = (
            aws_sdk_sagemaker.types.iam_policy_constraints.serialize_aws_json_1_1(
                value["iam_policy_constraints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Presign:
    out: S3Presign = {}  # type: ignore[typeddict-item]
    if "IamPolicyConstraints" in data:
        import aws_sdk_sagemaker.types.iam_policy_constraints

        out["iam_policy_constraints"] = (
            aws_sdk_sagemaker.types.iam_policy_constraints.deserialize_aws_json_1_1(
                data["IamPolicyConstraints"]
            )
        )
    return out
