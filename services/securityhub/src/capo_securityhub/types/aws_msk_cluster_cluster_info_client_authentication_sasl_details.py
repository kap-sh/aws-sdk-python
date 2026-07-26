"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationSaslDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details
    import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details


class AwsMskClusterClusterInfoClientAuthenticationSaslDetails(TypedDict, closed=True):
    iam: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details.AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails"
    ]
    """<p> Provides details for SASL client authentication using IAM. </p>"""
    scram: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details.AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails"
    ]
    """<p> Details for SASL client authentication using SCRAM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsMskClusterClusterInfoClientAuthenticationSaslDetails,
) -> dict:
    out: dict = {}
    if "iam" in value:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details

        out["Iam"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details.serialize_json(
                value["iam"]
            )
        )
    if "scram" in value:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details

        out["Scram"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details.serialize_json(
                value["scram"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsMskClusterClusterInfoClientAuthenticationSaslDetails:
    out: AwsMskClusterClusterInfoClientAuthenticationSaslDetails = {}  # type: ignore[typeddict-item]
    if "Iam" in data:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details

        out["iam"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_iam_details.deserialize_json(
                data["Iam"]
            )
        )
    if "Scram" in data:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details

        out["scram"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_scram_details.deserialize_json(
                data["Scram"]
            )
        )
    return out
