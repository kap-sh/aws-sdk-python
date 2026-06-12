"""Generated from Smithy shape ``com.amazonaws.sagemaker#DirectDeploySettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_status


class DirectDeploySettings(TypedDict):
    status: NotRequired["aws_sdk_sagemaker.types.feature_status.FeatureStatus"]
    """<p>Describes whether model deployment permissions are enabled or disabled in the Canvas application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectDeploySettings) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.feature_status

        out["Status"] = aws_sdk_sagemaker.types.feature_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectDeploySettings:
    out: DirectDeploySettings = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.feature_status

        out["status"] = aws_sdk_sagemaker.types.feature_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
