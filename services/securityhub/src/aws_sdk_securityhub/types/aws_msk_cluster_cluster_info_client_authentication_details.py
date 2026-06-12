"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details
    import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details
    import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details


class AwsMskClusterClusterInfoClientAuthenticationDetails(TypedDict):
    sasl: NotRequired[
        "aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details.AwsMskClusterClusterInfoClientAuthenticationSaslDetails"
    ]
    """<p> Provides details for client authentication using SASL.</p>"""
    unauthenticated: NotRequired[
        "aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details.AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails"
    ]
    """<p> Provides details for allowing no client authentication.</p>"""
    tls: NotRequired[
        "aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details.AwsMskClusterClusterInfoClientAuthenticationTlsDetails"
    ]
    """<p> Provides details for client authentication using TLS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsMskClusterClusterInfoClientAuthenticationDetails) -> dict:
    out: dict = {}
    if "sasl" in value:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details

        out["Sasl"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details.serialize_json(
                value["sasl"]
            )
        )
    if "unauthenticated" in value:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details

        out["Unauthenticated"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details.serialize_json(
                value["unauthenticated"]
            )
        )
    if "tls" in value:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details

        out["Tls"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details.serialize_json(
                value["tls"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsMskClusterClusterInfoClientAuthenticationDetails:
    out: AwsMskClusterClusterInfoClientAuthenticationDetails = {}  # type: ignore[typeddict-item]
    if "Sasl" in data:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details

        out["sasl"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details.deserialize_json(
                data["Sasl"]
            )
        )
    if "Unauthenticated" in data:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details

        out["unauthenticated"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details.deserialize_json(
                data["Unauthenticated"]
            )
        )
    if "Tls" in data:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details

        out["tls"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details.deserialize_json(
                data["Tls"]
            )
        )
    return out
