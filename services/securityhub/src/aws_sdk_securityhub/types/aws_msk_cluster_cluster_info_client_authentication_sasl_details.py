"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationSaslDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details
    import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details


class AwsMskClusterClusterInfoClientAuthenticationSaslDetails(TypedDict, closed=True):
    iam: NotRequired[
        "aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details.AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails"
    ]
    """<p> Provides details for SASL client authentication using IAM. </p>"""
    scram: NotRequired[
        "aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details.AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails"
    ]
    """<p> Details for SASL client authentication using SCRAM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsMskClusterClusterInfoClientAuthenticationSaslDetails,
) -> dict:
    out: dict = {}
    if "iam" in value:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details

        out["Iam"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details.serialize_json(
                value["iam"]
            )
        )
    if "scram" in value:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details

        out["Scram"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details.serialize_json(
                value["scram"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsMskClusterClusterInfoClientAuthenticationSaslDetails:
    out: AwsMskClusterClusterInfoClientAuthenticationSaslDetails = {}  # type: ignore[typeddict-item]
    if "Iam" in data:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details

        out["iam"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details.deserialize_json(
                data["Iam"]
            )
        )
    if "Scram" in data:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details

        out["scram"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details.deserialize_json(
                data["Scram"]
            )
        )
    return out
