"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TlsInterceptPropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.tls_intercept_mode


class TlsInterceptPropertiesRequest(TypedDict):
    pca_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>Private Certificate Authority (PCA) used to issue private TLS certificates so that the proxy can present PCA-signed certificates which applications trust through the same root, establishing a secure and consistent trust model for encrypted communication.</p>"""
    tls_intercept_mode: NotRequired[
        "aws_sdk_network_firewall.types.tls_intercept_mode.TlsInterceptMode"
    ]
    """<p>Specifies whether to enable or disable TLS Intercept Mode. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TlsInterceptPropertiesRequest) -> dict:
    out: dict = {}
    if "pca_arn" in value:
        out["PcaArn"] = value["pca_arn"]
    if "tls_intercept_mode" in value:
        import aws_sdk_network_firewall.types.tls_intercept_mode

        out["TlsInterceptMode"] = (
            aws_sdk_network_firewall.types.tls_intercept_mode.serialize_aws_json_1_0(
                value["tls_intercept_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TlsInterceptPropertiesRequest:
    out: TlsInterceptPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "PcaArn" in data:
        out["pca_arn"] = data["PcaArn"]
    if "TlsInterceptMode" in data:
        import aws_sdk_network_firewall.types.tls_intercept_mode

        out["tls_intercept_mode"] = (
            aws_sdk_network_firewall.types.tls_intercept_mode.deserialize_aws_json_1_0(
                data["TlsInterceptMode"]
            )
        )
    return out
