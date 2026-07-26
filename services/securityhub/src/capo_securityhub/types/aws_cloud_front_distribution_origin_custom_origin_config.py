"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginCustomOriginConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_ssl_protocols
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsCloudFrontDistributionOriginCustomOriginConfig(TypedDict, closed=True):
    http_port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The HTTP port that CloudFront uses to connect to the origin. </p>"""
    https_port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The HTTPS port that CloudFront uses to connect to the origin. </p>"""
    origin_keepalive_timeout: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>Specifies how long, in seconds, CloudFront persists its connection to the origin. </p>"""
    origin_protocol_policy: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. </p>"""
    origin_read_timeout: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>Specifies how long, in seconds, CloudFront waits for a response from the origin. </p>"""
    origin_ssl_protocols: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_origin_ssl_protocols.AwsCloudFrontDistributionOriginSslProtocols"
    ]
    """<p>Specifies the minimum SSL/TLS protocol that CloudFront uses when connecting to your origin over HTTPS. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginCustomOriginConfig) -> dict:
    out: dict = {}
    if "http_port" in value:
        out["HttpPort"] = value["http_port"]
    if "https_port" in value:
        out["HttpsPort"] = value["https_port"]
    if "origin_keepalive_timeout" in value:
        out["OriginKeepaliveTimeout"] = value["origin_keepalive_timeout"]
    if "origin_protocol_policy" in value:
        out["OriginProtocolPolicy"] = value["origin_protocol_policy"]
    if "origin_read_timeout" in value:
        out["OriginReadTimeout"] = value["origin_read_timeout"]
    if "origin_ssl_protocols" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_ssl_protocols

        out["OriginSslProtocols"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_ssl_protocols.serialize_json(
                value["origin_ssl_protocols"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionOriginCustomOriginConfig:
    out: AwsCloudFrontDistributionOriginCustomOriginConfig = {}  # type: ignore[typeddict-item]
    if "HttpPort" in data:
        out["http_port"] = data["HttpPort"]
    if "HttpsPort" in data:
        out["https_port"] = data["HttpsPort"]
    if "OriginKeepaliveTimeout" in data:
        out["origin_keepalive_timeout"] = data["OriginKeepaliveTimeout"]
    if "OriginProtocolPolicy" in data:
        out["origin_protocol_policy"] = data["OriginProtocolPolicy"]
    if "OriginReadTimeout" in data:
        out["origin_read_timeout"] = data["OriginReadTimeout"]
    if "OriginSslProtocols" in data:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_ssl_protocols

        out["origin_ssl_protocols"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_ssl_protocols.deserialize_json(
                data["OriginSslProtocols"]
            )
        )
    return out
