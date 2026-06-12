"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrustedIdentityPropagationSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_status


class TrustedIdentityPropagationSettings(TypedDict):
    status: NotRequired["aws_sdk_sagemaker.types.feature_status.FeatureStatus"]
    """<p>The status of Trusted Identity Propagation (TIP) at the SageMaker domain level. </p> <p>When disabled, standard IAM role-based access is used. </p> <p>When enabled:</p> <ul> <li> <p>User identities from IAM Identity Center are propagated through the application to TIP enabled Amazon Web Services services.</p> </li> <li> <p>New applications or existing applications that are automatically patched, will use the domain level configuration.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedIdentityPropagationSettings) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.feature_status

        out["Status"] = aws_sdk_sagemaker.types.feature_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedIdentityPropagationSettings:
    out: TrustedIdentityPropagationSettings = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.feature_status

        out["status"] = aws_sdk_sagemaker.types.feature_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
