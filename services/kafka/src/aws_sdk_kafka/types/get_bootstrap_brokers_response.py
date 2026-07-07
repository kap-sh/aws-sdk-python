"""Generated from Smithy shape ``com.amazonaws.kafka#GetBootstrapBrokersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class GetBootstrapBrokersResponse(TypedDict, closed=True):
    bootstrap_broker_string: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>A string containing one or more hostname:port pairs.</p>"""
    bootstrap_broker_string_tls: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>A string containing one or more DNS names (or IP) and TLS port pairs.</p>"""
    bootstrap_broker_string_sasl_scram: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string containing one or more DNS names (or IP) and Sasl Scram port pairs.</p>"""
    bootstrap_broker_string_sasl_iam: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string that contains one or more DNS names (or IP addresses) and SASL IAM port pairs.</p>"""
    bootstrap_broker_string_public_tls: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string containing one or more DNS names (or IP) and TLS port pairs.</p>"""
    bootstrap_broker_string_public_sasl_scram: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string containing one or more DNS names (or IP) and Sasl Scram port pairs.</p>"""
    bootstrap_broker_string_public_sasl_iam: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string that contains one or more DNS names (or IP addresses) and SASL IAM port pairs.</p>"""
    bootstrap_broker_string_vpc_connectivity_tls: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string containing one or more DNS names (or IP) and TLS port pairs for VPC connectivity.</p>"""
    bootstrap_broker_string_vpc_connectivity_sasl_scram: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string containing one or more DNS names (or IP) and SASL/SCRAM port pairs for VPC connectivity.</p>"""
    bootstrap_broker_string_vpc_connectivity_sasl_iam: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string containing one or more DNS names (or IP) and SASL/IAM port pairs for VPC connectivity.</p>"""
    bootstrap_broker_string_ipv6: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>A string that contains one or more DNS names (or IP) and port pairs for IPv6 connectivity.</p>"""
    bootstrap_broker_string_tls_ipv6: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string that contains one or more DNS names (or IP) and TLS port pairs for IPv6 connectivity.</p>"""
    bootstrap_broker_string_sasl_scram_ipv6: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string that contains one or more DNS names (or IP) and SASL SCRAM port pairs for IPv6 connectivity.</p>"""
    bootstrap_broker_string_sasl_iam_ipv6: NotRequired[
        "aws_sdk_kafka.types.__string.__string"
    ]
    """<p>A string that contains one or more DNS names (or IP) and SASL IAM port pairs for IPv6 connectivity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBootstrapBrokersResponse) -> dict:
    out: dict = {}
    if "bootstrap_broker_string" in value:
        out["bootstrapBrokerString"] = value["bootstrap_broker_string"]
    if "bootstrap_broker_string_tls" in value:
        out["bootstrapBrokerStringTls"] = value["bootstrap_broker_string_tls"]
    if "bootstrap_broker_string_sasl_scram" in value:
        out["bootstrapBrokerStringSaslScram"] = value[
            "bootstrap_broker_string_sasl_scram"
        ]
    if "bootstrap_broker_string_sasl_iam" in value:
        out["bootstrapBrokerStringSaslIam"] = value["bootstrap_broker_string_sasl_iam"]
    if "bootstrap_broker_string_public_tls" in value:
        out["bootstrapBrokerStringPublicTls"] = value[
            "bootstrap_broker_string_public_tls"
        ]
    if "bootstrap_broker_string_public_sasl_scram" in value:
        out["bootstrapBrokerStringPublicSaslScram"] = value[
            "bootstrap_broker_string_public_sasl_scram"
        ]
    if "bootstrap_broker_string_public_sasl_iam" in value:
        out["bootstrapBrokerStringPublicSaslIam"] = value[
            "bootstrap_broker_string_public_sasl_iam"
        ]
    if "bootstrap_broker_string_vpc_connectivity_tls" in value:
        out["bootstrapBrokerStringVpcConnectivityTls"] = value[
            "bootstrap_broker_string_vpc_connectivity_tls"
        ]
    if "bootstrap_broker_string_vpc_connectivity_sasl_scram" in value:
        out["bootstrapBrokerStringVpcConnectivitySaslScram"] = value[
            "bootstrap_broker_string_vpc_connectivity_sasl_scram"
        ]
    if "bootstrap_broker_string_vpc_connectivity_sasl_iam" in value:
        out["bootstrapBrokerStringVpcConnectivitySaslIam"] = value[
            "bootstrap_broker_string_vpc_connectivity_sasl_iam"
        ]
    if "bootstrap_broker_string_ipv6" in value:
        out["bootstrapBrokerStringIpv6"] = value["bootstrap_broker_string_ipv6"]
    if "bootstrap_broker_string_tls_ipv6" in value:
        out["bootstrapBrokerStringTlsIpv6"] = value["bootstrap_broker_string_tls_ipv6"]
    if "bootstrap_broker_string_sasl_scram_ipv6" in value:
        out["bootstrapBrokerStringSaslScramIpv6"] = value[
            "bootstrap_broker_string_sasl_scram_ipv6"
        ]
    if "bootstrap_broker_string_sasl_iam_ipv6" in value:
        out["bootstrapBrokerStringSaslIamIpv6"] = value[
            "bootstrap_broker_string_sasl_iam_ipv6"
        ]
    return out


def deserialize_json(data: dict) -> GetBootstrapBrokersResponse:
    out: GetBootstrapBrokersResponse = {}  # type: ignore[typeddict-item]
    if "bootstrapBrokerString" in data:
        out["bootstrap_broker_string"] = data["bootstrapBrokerString"]
    if "bootstrapBrokerStringTls" in data:
        out["bootstrap_broker_string_tls"] = data["bootstrapBrokerStringTls"]
    if "bootstrapBrokerStringSaslScram" in data:
        out["bootstrap_broker_string_sasl_scram"] = data[
            "bootstrapBrokerStringSaslScram"
        ]
    if "bootstrapBrokerStringSaslIam" in data:
        out["bootstrap_broker_string_sasl_iam"] = data["bootstrapBrokerStringSaslIam"]
    if "bootstrapBrokerStringPublicTls" in data:
        out["bootstrap_broker_string_public_tls"] = data[
            "bootstrapBrokerStringPublicTls"
        ]
    if "bootstrapBrokerStringPublicSaslScram" in data:
        out["bootstrap_broker_string_public_sasl_scram"] = data[
            "bootstrapBrokerStringPublicSaslScram"
        ]
    if "bootstrapBrokerStringPublicSaslIam" in data:
        out["bootstrap_broker_string_public_sasl_iam"] = data[
            "bootstrapBrokerStringPublicSaslIam"
        ]
    if "bootstrapBrokerStringVpcConnectivityTls" in data:
        out["bootstrap_broker_string_vpc_connectivity_tls"] = data[
            "bootstrapBrokerStringVpcConnectivityTls"
        ]
    if "bootstrapBrokerStringVpcConnectivitySaslScram" in data:
        out["bootstrap_broker_string_vpc_connectivity_sasl_scram"] = data[
            "bootstrapBrokerStringVpcConnectivitySaslScram"
        ]
    if "bootstrapBrokerStringVpcConnectivitySaslIam" in data:
        out["bootstrap_broker_string_vpc_connectivity_sasl_iam"] = data[
            "bootstrapBrokerStringVpcConnectivitySaslIam"
        ]
    if "bootstrapBrokerStringIpv6" in data:
        out["bootstrap_broker_string_ipv6"] = data["bootstrapBrokerStringIpv6"]
    if "bootstrapBrokerStringTlsIpv6" in data:
        out["bootstrap_broker_string_tls_ipv6"] = data["bootstrapBrokerStringTlsIpv6"]
    if "bootstrapBrokerStringSaslScramIpv6" in data:
        out["bootstrap_broker_string_sasl_scram_ipv6"] = data[
            "bootstrapBrokerStringSaslScramIpv6"
        ]
    if "bootstrapBrokerStringSaslIamIpv6" in data:
        out["bootstrap_broker_string_sasl_iam_ipv6"] = data[
            "bootstrapBrokerStringSaslIamIpv6"
        ]
    return out
