"""Generated from Smithy shape ``com.amazonaws.sagemaker#AmazonQSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_status
    import aws_sdk_sagemaker.types.q_profile_arn


class AmazonQSettings(TypedDict):
    status: NotRequired["aws_sdk_sagemaker.types.feature_status.FeatureStatus"]
    """<p>Whether Amazon Q has been enabled within the domain.</p>"""
    q_profile_arn: NotRequired["aws_sdk_sagemaker.types.q_profile_arn.QProfileArn"]
    """<p>The ARN of the Amazon Q profile used within the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonQSettings) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.feature_status

        out["Status"] = aws_sdk_sagemaker.types.feature_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "q_profile_arn" in value:
        out["QProfileArn"] = value["q_profile_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AmazonQSettings:
    out: AmazonQSettings = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.feature_status

        out["status"] = aws_sdk_sagemaker.types.feature_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "QProfileArn" in data:
        out["q_profile_arn"] = data["QProfileArn"]
    return out
